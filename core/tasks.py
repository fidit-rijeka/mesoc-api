import pickle

import numpy
import celery

from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string

from core import nlp
from .models import Cell, Document, DocumentImpact, DocumentKeyword, Impact, ImpactKeyword
from .nlp.keyword_extraction import NgramImpactExtractor
from .nlp.processing.text_processing import (
    StopsProcessor, MinSentenceLengthProcessor, PunctuationProcessor, DigitProcessor
)

logger = celery.utils.log.get_task_logger(__name__)


class LoggedTask(celery.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('An error occured while executing task {}'.format(task_id))
        logger.error(exc)


@celery.shared_task
def fail_document(document_id):
    document = Document.objects.filter(id=document_id).get()
    document.state = document.FAILED
    document.save()

    send_mail(
        render_to_string('core/document_processed_subject.txt'),
        render_to_string(
            'core/document_processed_fail_message.txt',
            context={'document_title': document.file_title, 'upload_url': settings.CORE_PROCESSING_FAIL_URL}
        ),
        None,
        (document.user.email,),
    )


@celery.shared_task(base=LoggedTask)
def send_mail(subject, message, from_, to):
    mail.send_mail(subject, message, from_, to)


@celery.shared_task(base=LoggedTask)
def send_feedback_mail(subject, message, from_, to):
    msg = mail.EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, to, headers={'From': from_})
    msg.send()


@celery.shared_task(base=LoggedTask)
def read_contents(document_id):
    document = Document.objects.filter(id=document_id).get()

    processors = [
        nlp.processing.CompoundEntitiesProcessor(),
        nlp.processing.StopsProcessor(),
        nlp.processing.MinSentenceLengthProcessor(settings.CORE_MIN_SENTENCE_LENGTH)
    ]

    text = document.contents
    for p in processors:
        text = p.process(text)

    return text


@celery.shared_task(base=LoggedTask)
def translate(text):
    gt = nlp.language.GoogleTranslator()
    lang = gt.detect(text)
    logger.debug('Detected language: {}'.format(lang))
    if lang != 'en':
        text = gt.translate(text)

    return text


@celery.shared_task(base=LoggedTask)
def extract_keywords(text):
    extractor = nlp.keyword_extraction.YAKEKeywordExtractor(
        settings.CORE_NUM_KEYWORDS,
        settings.CORE_YAKE_CANDIDATE_NGRAM,
        settings.CORE_YAKE_CANDIDATE_WINDOW_SIZE,
        settings.CORE_YAKE_THRESHOLD
    )

    keywords = extractor.extract_keywords(text)

    return keywords


@celery.shared_task(base=LoggedTask)
def classify_document(keywords):
    with open(settings.CORE_CRP_ROW_MODEL, 'rb') as f:
        row_model = pickle.load(f)

    with open(settings.CORE_CRP_COLUMN_MODEL, 'rb') as f:
        column_model = pickle.load(f)

    with open(settings.CORE_CRP_TFIDF_VECTORIZER, 'rb') as f:
        tfidf_vectorizer = pickle.load(f)

    keyword_processor = nlp.processing.KeyphraseToKeywordProcessor()
    classifier = nlp.classification.ColumnRowProbabilityClassifier(
        row_model,
        column_model,
        tfidf_vectorizer,
        settings.CORE_CRP_ROW_THRESHOLD,
        settings.CORE_CRP_COLUMN_THRESHOLD,
        pre_processors=(keyword_processor,)
    )

    return keywords, classifier.classify_keywords(keywords)


@celery.shared_task(base=LoggedTask)
def extract_impacts(results, document_id):
    impacts = Impact.objects.values_list('lemma', 'keywords__value')
    impact_map = {}
    for lemma, kw in impacts:
        try:
            impact_map[lemma].append(kw)
        except KeyError:
            impact_map[lemma] = [kw]

    extractor = NgramImpactExtractor(
        impact_map,
        pre_processors=(
            StopsProcessor(),
            DigitProcessor(),
            MinSentenceLengthProcessor(settings.CORE_MIN_SENTENCE_LENGTH),
            PunctuationProcessor()
        )
    )

    impacts = extractor.extract_keywords(Document.objects.filter(id=document_id).get().contents)

    return (*results, impacts)


@celery.shared_task(base=LoggedTask)
def commit_results(results, document_id):
    keywords = results[0]
    heatmap = numpy.array(results[1]).reshape(-1, order='F')  # reorder so we get column-major indices

    document = Document.objects.filter(id=document_id).get()

    cells = []
    nonzero = heatmap.nonzero()[0]
    for index in nonzero:
        cell = Cell(classification=heatmap[index], cell=index, document=document)
        cells.append(cell)

    document_keywords = []
    for keyword in set(keywords):
        dk = DocumentKeyword(value=keyword, document=document)
        document_keywords.append(dk)

    Cell.objects.bulk_create(cells)
    DocumentKeyword.objects.bulk_create(document_keywords)

    impacts = results[2]
    impacts_db = Impact.objects.filter(lemma__in=impacts.keys()).all()

    document_impacts = []
    for i in impacts_db:
        strength = impacts[i.lemma]['strength']
        document_impacts.append(DocumentImpact(document=document, impact=i, strength=strength))

    DocumentImpact.objects.bulk_create(document_impacts)
    document_impacts = DocumentImpact.objects.select_related('impact').filter(document=document).all()

    keywords_db = {k.value: k for k in ImpactKeyword.objects.all()}
    impact_keywords = []
    Through = DocumentImpact.keywords.through
    for i in document_impacts:
        for kw in impacts[i.impact.lemma]['keywords']:
            k = Through(documentimpact=i, impactkeyword=keywords_db[kw])
            impact_keywords.append(k)

    Through.objects.bulk_create(impact_keywords)

    document.state = document.PROCESSED
    document.save()


@celery.shared_task(base=LoggedTask)
def mail_results(document_id):
    document = Document.objects.filter(id=document_id).select_related('user').get()

    send_mail(
        render_to_string('core/document_processed_subject.txt'),
        render_to_string(
            'core/document_processed_success_message.txt',
            context={'document_title': document.file_title, 'my_documents_url': settings.CORE_PROCESSING_SUCCESS_URL}
        ),
        None,
        (document.user.email,),
    )

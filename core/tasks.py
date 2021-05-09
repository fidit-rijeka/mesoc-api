import logging
import pickle

import numpy

from celery import shared_task, Task
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string

from core import nlp
from .models import Cell, Document, DocumentKeyword

logger = logging.getLogger(__name__)


class LoggedTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('An error occured while executing task {}'.format(task_id))
        logger.error(exc)


@shared_task
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


@shared_task(base=LoggedTask)
def send_mail(subject, message, from_, to):
    mail.send_mail(subject, message, from_, to)


@shared_task(base=LoggedTask)
def convert_to_pdf(document_id):
    document = Document.objects.filter(id=document_id).get()

    entities_processor = nlp.processing.CompoundEntitiesProcessor()
    stops_processor = nlp.processing.StopsProcessor()
    min_length_processor = nlp.processing.MinSentenceLengthProcessor(settings.CORE_MIN_SENTENCE_LENGTH)
    pdf_converter = nlp.pdf_conversion.FitzPDFConverter(
        post_processors=(entities_processor, stops_processor, min_length_processor)
    )

    text = pdf_converter.convert_to_text(document.file.path)

    return text


@shared_task(base=LoggedTask)
def extract_keywords(text):
    extractor = nlp.keyword_extraction.YAKEKeywordExtractor(
        settings.CORE_NUM_KEYWORDS,
        settings.CORE_YAKE_CANDIDATE_NGRAM,
        settings.CORE_YAKE_CANDIDATE_WINDOW_SIZE,
        settings.CORE_YAKE_THRESHOLD
    )

    keywords = extractor.extract_keywords(text)

    return keywords


@shared_task(base=LoggedTask)
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


@shared_task(base=LoggedTask)
def commit_results(results, document_id):
    keywords = results[0]
    heatmap = numpy.array(results[1]).reshape(-1, order='F')  # reorder so we get column-major indices

    document = Document.objects.filter(id=document_id).get()

    cells = []
    nonzero = heatmap.nonzero()[0]
    for index in nonzero:
        cell = Cell(classification=heatmap[index], order=index, document=document)
        cells.append(cell)

    document_keywords = []
    for keyword in set(keywords):
        dk = DocumentKeyword(value=keyword, document=document)
        document_keywords.append(dk)

    Cell.objects.bulk_create(cells)
    DocumentKeyword.objects.bulk_create(document_keywords)
    document.state = document.PROCESSED
    document.save()


@shared_task(base=LoggedTask)
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

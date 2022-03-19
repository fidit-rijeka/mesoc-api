import abc

import nltk
import pke

from core.nlp.processing import misc
from core.nlp.processing import keyword_processing, text_processing


class BaseKeywordExtractor(abc.ABC):
    def extract_keywords(self, text):
        raise NotImplementedError


class YAKEKeywordExtractor(BaseKeywordExtractor):
    def __init__(
            self,
            num_keywords,
            candidate_ngram,
            candidate_window_size,
            threshold,
            stopwords=nltk.corpus.stopwords.words('english'),
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._num_keywords = num_keywords
        self._candidate_ngram = candidate_ngram
        self._candidate_window_size = candidate_window_size
        self._threshold = threshold
        self._stopwords = stopwords
        self._extractor = pke.unsupervised.YAKE()

    def extract_keywords(self, text):
        self._extractor.load_document(input=text, language='en', normalization=None)

        self._extractor.candidate_selection(n=self._candidate_ngram, stoplist=self._stopwords)
        self._extractor.candidate_weighting(
            window=self._candidate_window_size,
            stoplist=self._stopwords,
            use_stems=True
        )

        keywords_yake_pke = self._extractor.get_n_best(
            n=self._num_keywords,
            threshold=self._threshold
        )

        keywords = [x[0] for x in keywords_yake_pke]

        return keywords


class NgramImpactExtractor(misc.PreProcessing, BaseKeywordExtractor):
    def __init__(
            self,
            impact_kw_map,
            ngrams=(2, 3),
            *args,
            tokenizer=text_processing.default_word_tokenizer,
            lemmatizer=keyword_processing.default_lemmatizer,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._tokenizer = tokenizer
        self._lemmatizer = lemmatizer
        self._impact_kw_map = impact_kw_map
        self._ngrams = ngrams

    def _extract_ngrams(self, text, n):
        tokens = self._tokenizer.tokenize(text)
        tokens = [self._lemmatizer.lemmatize(t) for t in tokens] if self._lemmatizer else tokens

        return [' '.join(ngram) for ngram in nltk.ngrams(tokens, n)]

    def extract_keywords(self, text):
        for processor in self.pre_processors:
            text = processor.process(text)

        ngrams = [set(self._extract_ngrams(text, n)) for n in self._ngrams]

        impacts = {}
        for impact, keywords in self._impact_kw_map.items():
            kw_list = []
            for ngram in ngrams:
                for kw in keywords:
                    if kw in ngram:
                        kw_list.append(kw)

            if not kw_list:
                continue

            strength = len(kw_list) / len(keywords)
            impacts[impact] = {'strength': strength, 'keywords': kw_list}

        return impacts

import abc

import nltk
import pke

from .processing import PostProcessing


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

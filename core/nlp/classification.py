import abc

import numpy

from core.nlp.processing import PreProcessing


class BaseClassifier(abc.ABC):
    def classify_keywords(self, keywords):
        raise NotImplementedError


class ColumnRowProbabilityClassifier(PreProcessing, BaseClassifier):
    def __init__(self, row_model, column_model, tfidf_vectorizer, row_threshold, column_threshold, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._row_model = row_model
        self._column_model = column_model
        self._tfidf_vectorizer = tfidf_vectorizer

        self._row_threshold = row_threshold
        self._column_threshold = column_threshold

    def classify_keywords(self, keywords):
        for processor in self.pre_processors:
            keywords = processor.process(keywords)

        tfidf = self._tfidf_vectorizer.transform([' '.join(keywords)])

        row_probabilities = self._row_model.predict_proba(tfidf)
        below_threshold = row_probabilities < self._row_threshold

        boost = row_probabilities[below_threshold].sum() / row_probabilities[~below_threshold].shape[0]
        row_probabilities = numpy.add(row_probabilities, boost, where=~below_threshold)
        row_probabilities[below_threshold] = 0.0

        column_probabilities = self._column_model.predict_proba(tfidf)
        below_threshold = column_probabilities < self._column_threshold

        boost = column_probabilities[below_threshold].sum() / column_probabilities[~below_threshold].shape[0]
        column_probabilities = numpy.add(column_probabilities, boost, where=~below_threshold)
        column_probabilities[below_threshold] = 0.0

        heatmap = column_probabilities.reshape(3, 1) * row_probabilities

        return heatmap.transpose().tolist()

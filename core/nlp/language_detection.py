import abc

import fasttext


class BaseLanguageDetector(abc.ABC):
    @abc.abstractmethod
    def detect(self, text):
        raise NotImplementedError


class FastTextLanguageDetector(BaseLanguageDetector):
    def __init__(self, path_to_model):
        self._model = fasttext.load_model(path_to_model)

    def detect(self, text):
        text = text.replace('\n', ' ')
        return self._model.predict(text)[0][0].replace('__label__', '')

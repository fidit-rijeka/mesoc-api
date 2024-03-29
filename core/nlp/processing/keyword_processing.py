import abc

import nltk

from . import text_processing


class BaseKeywordsProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, keywords):
        raise NotImplementedError


class WordNetLemmatizer(nltk.WordNetLemmatizer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nltk.corpus.wordnet.ensure_loaded()


default_lemmatizer = WordNetLemmatizer()


class KeyphraseToKeywordProcessor(BaseKeywordsProcessor):
    def __init__(
            self,
            *args,
            word_tokenizer=text_processing.default_word_tokenizer,
            lemmatizer=default_lemmatizer,
            stopwords=nltk.corpus.stopwords.words('english'),
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._word_tokenizer = word_tokenizer
        self._lemmatizer = lemmatizer
        self._stopwords = stopwords

    def process(self, keywords):
        keywords = [kw for kp in keywords for kw in self._word_tokenizer.tokenize(kp)]
        keywords = [self._lemmatizer.lemmatize(kw.strip()) for kw in keywords]
        return [kw for kw in keywords if kw not in self._stopwords]

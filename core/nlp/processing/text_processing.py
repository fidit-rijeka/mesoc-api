import abc
import re
import string

import nltk

from textacy.preprocessing.replace import urls, emails
from textacy.preprocessing.normalize import hyphenated_words
from textacy.preprocessing.normalize import whitespace
from textacy.preprocessing.normalize import quotation_marks

from . import misc


class BaseTextProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, text):
        raise NotImplementedError


class CompoundEntitiesProcessor(BaseTextProcessor):
    def process(self, text):
        text = urls(text, '')
        # text = misc.RE_URL.sub('', text)

        text = emails(text, '')
        # text = misc.RE_EMAIL.sub('', text)

        text = misc.RE_PHONE_NUMBER.sub('', text)

        text = text.split('\n')
        text = [misc.RE_DOI.sub('', line) for line in text]
        text = '\n'.join([t for t in text if t])

        return text


class MinSentenceLengthProcessor(BaseTextProcessor):
    def __init__(self, min_sentence_length, *args, sent_tokenizer=misc.default_sent_tokenizer, **kwargs):
        super().__init__(*args, **kwargs)

        if min_sentence_length < 1:
            raise ValueError('Minimum sentence length must exceed 0.')

        self._min_sentence_length = min_sentence_length
        self._sent_tokenizer = sent_tokenizer

    def process(self, text):
        keywords = self._sent_tokenizer.tokenize(text)
        keywords = list(set(keywords))
        keywords = [x for x in keywords if len(x) >= self._min_sentence_length]
        keywords = ' '.join(keywords)

        return keywords


class StopsProcessor(BaseTextProcessor):
    def __init__(self, stopwords=misc.STOPWORDS, stopchars=misc.STOPCHARS):
        self._stopwords = stopwords
        self._stopchars = stopchars

    def process(self, text):
        text = text.replace('\\\'', '\'')
        text = re.sub(r'\b\w{1,2}\.', '', text)

        remove_characters = str.maketrans('', '', ''.join(self._stopchars))
        text = text.translate(remove_characters)

        text = misc.RE_HTML_ENTITIES.sub('', text)

        text = hyphenated_words(text)
        text = quotation_marks(text)

        text = ' '.join([word for word in nltk.word_tokenize(text) if word not in self._stopwords])

        text = whitespace(text)

        return text.lower()


class PunctuationProcessor(BaseTextProcessor):
    def __init__(self):
        self._punctuation = re.compile(r'[{}]'.format(string.punctuation))

    def process(self, text):
        text = self._punctuation.sub('', text)
        return whitespace(text)


class DigitProcessor(BaseTextProcessor):
    def process(self, text):
        return text.translate(str.maketrans('', '', string.digits))


class TokenProcessor(BaseTextProcessor):
    def process(self, text):
        return misc.default_word_tokenizer(text)

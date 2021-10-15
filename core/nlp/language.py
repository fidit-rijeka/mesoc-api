import abc

import google.cloud.translate_v2
import google.oauth2.service_account
import nltk

from django.conf import settings


class BaseLanguageDetector(abc.ABC):
    @abc.abstractmethod
    def detect(self, text):
        raise NotImplementedError


class BaseTranslator(abc.ABC):
    @abc.abstractmethod
    def translate(self, text):
        raise NotImplementedError


class GoogleTranslator(BaseLanguageDetector, BaseTranslator):
    def __init__(self, chunk_size=5000, tokenizer=None):
        credentials = google.oauth2.service_account.Credentials.from_service_account_info(
            settings.CORE_GOOGLE_CLOUD_CREDENTIALS
        )
        self._tc = google.cloud.translate_v2.Client(credentials=credentials)
        self._chunk_size = chunk_size

        if tokenizer is None:
            self._tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def detect(self, text):
        return self._tc.detect_language(text)['language']

    def translate(self, text):
        if len(text) >= self._chunk_size:
            translated_text = ''
            source_text_chunk = ''
            sentences = self._tokenizer.tokenize(text)

            for sent in sentences:
                if len(sent) + len(source_text_chunk) < self._chunk_size:
                    source_text_chunk += ' ' + sent
                else:
                    translation_chunk = self._tc.translate(source_text_chunk, target_language='en')
                    translated_text += ' ' + translation_chunk['translatedText']
                    source_text_chunk = sent

            translation_chunk = self._tc.translate(source_text_chunk, target_language='en')
            translated_text = translated_text + ' ' + translation_chunk['translatedText']

            return translated_text

        else:
            result = self._tc.translate(text, target_language='en')
            return result['translatedText']

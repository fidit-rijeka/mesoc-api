import abc

import fitz

from .processing import PostProcessing


class BasePDFConverter(abc.ABC):
    @abc.abstractmethod
    def convert_to_text(self, byte_stream):
        raise NotImplementedError


class FitzPDFConverter(PostProcessing, BasePDFConverter):
    def convert_to_text(self, file_path):
        doc = fitz.open(file_path)
        texts = []
        for page in doc:
            text = page.getText("text")
            texts.append(text)
        text = ''.join(texts)

        for processor in self.post_processors:
            text = processor.process(text)

        return text

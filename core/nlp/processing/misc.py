import re
import string

import nltk

default_sent_tokenizer = nltk.load('tokenizers/punkt/english.pickle')
default_word_tokenizer = nltk.NLTKWordTokenizer()
default_lemmatizer = nltk.WordNetLemmatizer()

STOPWORDS = [
    'ie',
    'i.e.',
    'eg',
    'e.g.',
    'etc.',
    'etc',
    'ph.d.',
    'pseud.',
    'comp.',
    'ed.',
    'n.d.',
    'n.p.',
    'a.d.',
    'a.m.',
    'al.',
    'et',
    'id.',
    'p.m.',
    '[…]',
    'approx.',
    'est.',
    'tel.',
    'fax.',
    'ltd.'
]

STOPCHARS = ['«', '»', '…', 'â', 'œ', '☆', '⁎', '©']
STOPCHARS.extend(string.digits)

RE_DOI = re.compile(
     r'((\(?[Dd][Oo][Ii](\s)*\)?:?(\s)*)'  # 'doi:' or 'doi' or '(doi)' (upper or lower case)
     r'|(https?://(dx\.)?doi\.org\/))?'  # or 'http://(dx.)doi.org/'  (neither has to be present)
     r'(?P<doi>10\.'  # 10.                        (mandatory for DOI's)
     r'\d{3,7}'  # [0-9] x 3-7
     r'(\.\w+)*'  # subdivisions separated by . (doesn't have to be present)
     r'(/|%2f)'  # / (possibly urlencoded)
     r'[\w\-_:;\(\)/\.<>]+'  # any character
     r'[\w\-_:;\(\)/<>])',  # any character excluding a full stop
     re.VERBOSE + re.IGNORECASE
)


RE_EMAIL = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|'r'(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    re.MULTILINE
)

RE_PHONE_NUMBER = re.compile(

    r"(?:^|(?<=[^\w)]))(\+?1[ .-]?)?(\(?\d{2,3}\)?[ .-]?)?(\d{2,3}[ .-]?\d{2,5})"  # core components of a phone number
    r"(\s?(?:ext\.?|[#x-])\s?\d{2,6})?(?:$|(?=\W))",  # extensions, etc.
    flags=re.UNICODE | re.IGNORECASE
)

RE_URL = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|'
    r'(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    flags=re.MULTILINE
)

RE_HTML_ENTITIES = re.compile(r'&(#\d+|\w+);')


class PreProcessing:
    def __init__(self, *args, pre_processors=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.pre_processors = pre_processors


class PostProcessing:
    def __init__(self, *args, post_processors=(), **kwargs):
        super().__init__(*args, **kwargs)
        self.post_processors = post_processors


class FullProcessing(PostProcessing, PreProcessing):
    pass

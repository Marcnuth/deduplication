import spacy
from itertools import filterfalse


BASIC_LAGNUAGE_MODEL = 'en_core_web_sm'
DEFAULT_LANGUAGE_MODEL = 'xx_ent_wiki_sm'


def tokenize(text, language_model=DEFAULT_LANGUAGE_MODEL, lemmatize=True, remove_stopwords=True, custom_filter=lambda x: x):
    spacy.load(BASIC_LAGNUAGE_MODEL)
    nlp = spacy.load(language_model)
    
    is_stopword = lambda x: remove_stopwords and x.norm_ in spacy.lang.en.stop_words.STOP_WORDS
    is_removable = lambda x: is_stopword(x) and custom_filter(x.text) and x.is_punct and x.is_digit

    token_value = lambda x: x.lemma_ if lemmatize else x.text
    yield from map(token_value, filterfalse(is_removable, nlp(text)))


from deduplication import nlp
from pathlib import Path


def test_main():
    with open(Path(__file__).resolve().parent / 'data' / 'wiki_nlp.txt', 'r') as f:
        content = f.read()

    tokens = list(nlp.tokenize(content))
    print(len(tokens), tokens)


def test_sentences():
    with open(Path(__file__).resolve().parent / 'data' / 'wiki_nlp.txt', 'r') as f:
        content = f.read()

    sents = list(nlp.sentencizer(content))
    print(len(sents), sents)
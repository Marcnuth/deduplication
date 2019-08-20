"""
This is an improved simhash algorithm, based on the idea:
- the longer sentence contains more information
- the duplicate documents will be similar in longest senteces
"""
from . import nlp, simhash


def lsimhash(text, n_longest=2, n_block=8):
    sentences = sorted(nlp.sentencizer(text), key=lambda x: -1 * len(x))[:n_longest]

    return simhash.simhash(' '.join(sentences), n_block)

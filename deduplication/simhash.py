import logging
from .nlp import tokenize
from collections import Counter
from hashlib import md5
import numpy as np


logger = logging.getLogger(__name__)


def simhash(text):
    tokens = tokenize(text)
    return _sum_hashes(tokens)


def _sum_hashes(tokens):
    def __hash(string):
        bits = np.array(list(map(int, bin(int(md5(string.encode()).hexdigest(), 16))[2:])))
        bits[bits == 0] = -1
        return np.pad(bits, (128 - bits.size, 0), 'constant', constant_values=0)

    hash = np.zeros(128)
    for token, cnt in Counter(tokens).items():
        hash += __hash(token) * cnt
    hash[hash <= 0] = 0
    hash[hash > 0] = 1
    return ''.join(list(map(str, hash.astype(int))))

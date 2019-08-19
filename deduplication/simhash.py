import logging
from .nlp import tokenize
from collections import Counter
from hashlib import md5
import numpy as np
import textwrap


logger = logging.getLogger(__name__)

LEN_HASH = 128


def simhash(text, n_block=8):
    assert LEN_HASH % n_block == 0, f'n_block must be exactly divided by {LEN_HASH}'
    tokens = tokenize(text)
    hashstr = _sum_hashes(tokens)
    return textwrap.wrap(hashstr, int(len(hashstr) / n_block))


def _sum_hashes(tokens):
    def __hash(string):
        bits = np.array(list(map(int, bin(int(md5(string.encode()).hexdigest(), 16))[2:])))
        bits[bits == 0] = -1
        return np.pad(bits, (LEN_HASH - bits.size, 0), 'constant', constant_values=0)

    hash = np.zeros(LEN_HASH)
    for token, cnt in Counter(tokens).items():
        hash += __hash(token) * cnt
    hash[hash <= 0] = 0
    hash[hash > 0] = 1
    return ''.join(list(map(str, hash.astype(int))))

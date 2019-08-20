from deduplication import simhash, lsimhash
from pathlib import Path
from scipy.spatial.distance import hamming
import numpy as np
import textwrap


def test_main():
    with open(Path(__file__).resolve().parent / 'data' / 'wiki_nlp.txt', 'r') as f:
        content = f.read()

    hval = lsimhash.lsimhash(content)
    print(hval)


def test_cmp():
    h1 = simhash.simhash('Hyperparameter Tuning is one of the most computationally expensive tasks when creating deep learning networks. Luckily, you can use Google Colab to speed up the process significantly. In this post, I will show you how you can tune the hyperparameters of your existing keras models using Hyperas and run everything in a Google Colab Notebook.')
    h2 = simhash.simhash('Hyperparameter tuning is one of the most computationally expensive tasks for deep learning networks. we can use Google Colab to speed up the process significantly. In this post, I will show you how to tune the hyper parameters of keras models using Hyperas and run everything.')

    print('\n', h1, '\n', h2)


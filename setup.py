import codecs
from setuptools import setup, find_packages


def read_file(filename, cb):
    with codecs.open(filename, 'r', 'utf8') as f:
        return cb(f)


setup(
    name='deduplication',
    version='0.0.1',

    packages=find_packages(),
    url='https://github.com/Marcnuth/deduplication',

    author='Marcnuth',
    author_email='hxianxian@gmail.com',

    license="Apache License 2.0",

    description="Remove duplicate documents via popular algorithms such as SimHash, SpotSig, Shingliing, etc.",
    long_description=read_file('README.md', lambda f: f.read()),
    long_description_content_type='text/markdown',
    install_requires=read_file('requirements.txt', lambda f: list(filter(bool, map(str.strip, f)))),

    classifiers=[
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3'
    ]

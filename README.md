# deduplication

![PyPI - Downloads](https://img.shields.io/pypi/dw/deduplication?label=PyPI)

Remove duplicate documents via popular algorithms such as SimHash, SpotSig, Shingling, etc.

## Install

Run following commands:

```
# install current library
pip install deduplication

# install required pretrained NLP models 
python -m spacy download xx_ent_wiki_sm
python -m spacy download en_core_web_sm
```

## Example

__SimHash__

```python
from deduplication import simhash

hashvalue1 = simhash('this is text')
hashvalue2 = simhash('this is another text', n_block=4)
```

## Citation

__SimHash__

```
Sadowski C, Levin G. 
Simhash: Hash-based similarity detection[J]. 
Technical report, Google, 2007.
```

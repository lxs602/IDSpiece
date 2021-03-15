[![Current PyPI packages](https://badge.fury.io/py/idspiece.svg)](https://pypi.org/project/idspiece/)

# IDSpiece

漢字/汉字-Tokenizer with Ideographic Description Sequence from [CHISE-IDS](https://www.chise.org/ids/).

* Only nine IDCs (U+2FF0, U+2FF1, U+2FF5 to U+2FFA) are used.
* IDCs never occur instantly after another IDC.
* Instantly after IDCs, Kanxi Radicals and Supplement (U+2E80 to U+2FD5) are preferred.
* Otherwise, CJK Unified Ideographs and Extension A (U+3400 to U+9FFC) are preferred.

## Basic usage

```py
>>> from idspiece import idstable
>>> def tokenize(text):
...   tokens=[]
...   while text>"":
...     c=text[0]
...     if c in idstable:
...       tokens.append(idstable[c][0:2])
...       text=idstable[c][2]+text[1:]
...     else:
...       tokens.append(c)
...       text=text[1:]
...   return tokens
...
>>> t=tokenize("羯諦羯諦波羅羯諦波羅僧羯諦菩提薩婆訶")
>>> print(t)
['⿰⽺', '⿱⽈', '⿹⼓', '亾', '⿰⾔', '帝', '⿰⽺', '⿱⽈', '⿹⼓', '亾', '⿰⾔', '帝', '⿰⺡', '皮', '⿱⺲', '⿰⽷', '隹', '⿰⽺', '⿱⽈', '⿹⼓', '亾', '⿰⾔', '帝', '⿰⺡', '皮', '⿱⺲', '⿰⽷', '隹', '⿰⺅', '曾', '⿰⽺', '⿱⽈', '⿹⼓', '亾', '⿰⾔', '帝', '⿱⺾', '⿱⽴', '口', '⿰⺘', '⿱⽇', '⿱⼀', '龰', '⿱⺾', '⿰⻖', '⿸产', '生', '⿱波', '女', '⿰⾔', '可']
```

## Install

```py
pip3 install idspiece
```

## Author

Koichi Yasuoka (安岡孝一)


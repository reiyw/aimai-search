# aimai-search

Fuzzy search in both Japanese and English.

```
pip install aimai-search
```

```python
>>> from aimai_search import AimaiSearch
>>> aimai = AimaiSearch(['カツカレー', 'カツ丼', 'カルテット'])
>>> aimai.search('cutlet')
[('カツカレー', 90.0), ('カルテット', 59.99999999999999), ('カツ丼', 23.75)]
>>> aimai.search('cutlet curry')
[('カツカレー', 100.0), ('カルテット', 45.23809523809524), ('カツ丼', 22.5)]
>>> aimai.search('katsu')
[('カツカレー', 90.0), ('カツ丼', 90.0), ('カルテット', 54.0)]
>>> aimai.search('don')
[('カツ丼', 90.0), ('カルテット', 29.999999999999996), ('カツカレー', 0.0)]
>>> aimai.search('丼')
[('カツ丼', 90.0), ('カツカレー', 0.0), ('カルテット', 0.0)]
```

The search results heavily depend on [cutlet](https://github.com/polm/cutlet) and [rapidfuzz](https://github.com/maxbachmann/rapidfuzz).

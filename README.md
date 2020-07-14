# aimai-search

Fuzzy search in both Japanese and English.

```
pip install aimai-search
```

```python
>>> from aimai_search import AimaiSearch
>>> aimai = AimaiSearch(['カツカレー', 'カツ丼', 'カルテット'])
>>> aimai.search('cultet')
[('カツカレー', 75.00000000000001), ('カルテット', 60.00000000000001), ('カツ丼', 14.285714285714292)]
>>> aimai.search('cultet curry')
[('カツカレー', 91.66666666666667), ('カルテット', 38.095238095238095), ('カツ丼', 22.5)]
>>> aimai.search('katsu')
[('カツカレー', 90.0), ('カツ丼', 90.0), ('カルテット', 54.0)]
>>> aimai.search('don')
[('カツ丼', 90.0), ('カルテット', 36.0), ('カツカレー', 0.0)]
>>> aimai.search('丼')
[('カツ丼', 90.0), ('カツカレー', 0.0), ('カルテット', 0.0)]
```

The search results heavily depend on [cultet](https://github.com/polm/cutlet) and [rapidfuzz](https://github.com/maxbachmann/rapidfuzz).

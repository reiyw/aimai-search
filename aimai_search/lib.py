from typing import Dict, List, Tuple, Union

import attr
import cutlet
import rapidfuzz
from more_itertools import unique_everseen, take


class AttrProto:
    def __init__(self, targets: List[str]) -> None:
        ...


@attr.s
class AimaiSearch(AttrProto):
    targets: List[str] = attr.ib()
    target_mapper: Dict[str, int] = attr.ib(init=False)

    def __attrs_post_init__(self):
        katsu = cutlet.Cutlet()
        katsu_no_foreign = cutlet.Cutlet()
        katsu_no_foreign.use_foreign_spelling = False

        self.target_mapper = dict()
        for i, target in enumerate(self.targets):
            self.target_mapper[target] = i
            self.target_mapper[katsu.romaji(target)] = i
            self.target_mapper[katsu_no_foreign.romaji(target)] = i

    def search(self, query: str, limit: int = 10) -> List[Tuple[str, float]]:
        ret = rapidfuzz.process.extract(
            query, self.target_mapper.keys(), limit=limit * 3
        )
        return take(
            limit,
            unique_everseen(
                (
                    (self.targets[self.target_mapper[expanded_target]], score)
                    for expanded_target, score in ret
                ),
                lambda t: self.target_mapper[t[0]],
            ),
        )

    def search_best(self, query: str) -> Tuple[str, float]:
        expanded, score = rapidfuzz.process.extractOne(query, self.target_mapper.keys())
        return (self.targets[self.target_mapper[expanded]], score)

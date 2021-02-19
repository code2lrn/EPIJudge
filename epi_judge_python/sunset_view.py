from typing import Iterator, List

from test_framework import generic_test
import collections


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    IdAndHeight = collections.namedtuple('IDAndHeight', ('Id', 'Height'))
    buildings_with_view: List[IdAndHeight] = []
    for Id, Height in enumerate(sequence):
        while buildings_with_view and Height >= buildings_with_view[-1].Height:
            buildings_with_view.pop()

        buildings_with_view.append(IdAndHeight(Id, Height))

    return [i.Id for i in reversed(buildings_with_view)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))

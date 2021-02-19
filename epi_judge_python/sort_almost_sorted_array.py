from typing import Iterator, List

from test_framework import generic_test
import itertools
import heapq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    min_heap = []
    for val in itertools.islice(sequence, k):
        heapq.heappush(min_heap, val)

    result = []
    for val in sequence:
        result.append(heapq.heappushpop(min_heap, val))

    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))

import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    keyword_frequency, keywords_to_find = collections.Counter(keywords), len(keywords)
    smallest_subarray = None
    left_idx = 0
    for right_idx, word in enumerate(paragraph):
        if word in keyword_frequency:
            keyword_frequency[word] -= 1
            if keyword_frequency[word] >= 0:
                keywords_to_find -= 1

        while keywords_to_find == 0:
            if smallest_subarray is None or (right_idx - left_idx) < (smallest_subarray.end - smallest_subarray.start):
                smallest_subarray = Subarray(left_idx, right_idx)

            w = paragraph[left_idx]
            if w in keyword_frequency:
                keyword_frequency[w] += 1
                if keyword_frequency[w] > 0:
                    keywords_to_find += 1
            left_idx += 1

    return smallest_subarray


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))

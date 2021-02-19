import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def smaller(s1: Subarray, s2: Subarray) -> Subarray:
    if s1.start == s1.end == -1:
        return s2

    if s2.start == s2.end == -1:
        return s1

    return s1 if (s1.end - s1.start) < (s2.end - s2.start) else s2


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    keywords_index_by_keyword = {k: i for i, k in enumerate(keywords)}
    keyword_occurrence = [-1] * len(keywords)
    subarray_lengths = [-1] * len(keywords)
    shortest_subarray = Subarray(-1, -1)
    for i, word in enumerate(paragraph):
        if word in keywords_index_by_keyword:
            keyword_idx = keywords_index_by_keyword[word]
            if keyword_idx == 0:
                subarray_lengths[keyword_idx] = 1
            elif subarray_lengths[keyword_idx - 1] != -1:
                distance_from_prev_keyword = i - keyword_occurrence[keyword_idx - 1]
                subarray_lengths[keyword_idx] = distance_from_prev_keyword + subarray_lengths[keyword_idx - 1]

            keyword_occurrence[keyword_idx] = i

            if keyword_idx == len(keywords) - 1 and subarray_lengths[-1] != -1:
                shortest_subarray = smaller(Subarray(i - subarray_lengths[-1] + 1, i), shortest_subarray)

    return shortest_subarray


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))

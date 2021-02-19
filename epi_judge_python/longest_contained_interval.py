from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    longest_range_seen = 0
    unprocessed = set(A)
    while unprocessed:
        val = unprocessed.pop()
        lower, higher = val - 1, val + 1
        while lower in unprocessed:
            unprocessed.remove(lower)
            lower -= 1

        while higher in unprocessed:
            unprocessed.remove(higher)
            higher += 1

        longest_range_seen = max(longest_range_seen, higher - lower - 1)

    return longest_range_seen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))

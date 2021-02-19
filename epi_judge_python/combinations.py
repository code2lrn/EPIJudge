from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    num = [i for i in range(1, n + 1)]
    subsets: List[List[int]] = []
    for bitfield in range(pow(2, n)):
        subset = []
        for j in range(n):
            if bitfield & (1 << j):
                subset.append(num[j])

        if len(subset) == k:
            subsets.append(subset)

    return subsets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

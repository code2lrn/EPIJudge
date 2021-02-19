from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    swap_from = len(perm) - 2
    while swap_from >= 0 and perm[swap_from] >= perm[swap_from + 1]:
        swap_from -= 1

    if swap_from == -1:
        return []

    for i in reversed(range(len(perm))):
        if perm[i] > perm[swap_from]:
            perm[swap_from], perm[i] = perm[i], perm[swap_from]
            break

    perm[swap_from + 1:] = reversed(perm[swap_from + 1:])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))

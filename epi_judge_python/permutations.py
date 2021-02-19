from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def do_perms(i: int):
        if i == len(A) - 1:
            perms.append(A.copy())
        else:
            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]
                do_perms(i + 1)
                A[i], A[j] = A[j], A[i]

    perms: List[List[int]] = []
    do_perms(0)
    return perms


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

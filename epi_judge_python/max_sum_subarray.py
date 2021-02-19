from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_subarray_sum = running_max = 0
    for i in range(0, len(A)):
        running_max = max(A[i], running_max + A[i])
        max_subarray_sum = max(max_subarray_sum, running_max)

    return max_subarray_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))

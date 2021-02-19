from typing import List

from test_framework import generic_test


def pivot(A: List[int], left: int, right: int, pivot: int) -> int:
    pivot_value, swap_to_idx = A[pivot], left
    A[pivot], A[right] = A[right], A[pivot]
    for i in range(left, right):
        if A[i] > pivot_value:
            A[swap_to_idx], A[i] = A[i], A[swap_to_idx]
            swap_to_idx += 1

    A[swap_to_idx], A[right] = A[right], A[swap_to_idx]
    return swap_to_idx


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        suggested_pivot = (left + right) // 2
        actual_pivot = pivot(A, left, right, suggested_pivot)
        if actual_pivot == k - 1:
            return A[actual_pivot]
        elif actual_pivot > k - 1:
            right = actual_pivot - 1
        else:
            left = actual_pivot + 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))

from typing import List
from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    longest_subarray_len = subarray_start_idx = 0
    numbers_seen = {}
    for i, num in enumerate(A):
        if num in numbers_seen:
            prev_idx = numbers_seen[num]
            if prev_idx >= subarray_start_idx:
                longest_subarray_len = max(longest_subarray_len, i - subarray_start_idx)
                subarray_start_idx = prev_idx + 1

        numbers_seen[num] = i

    return max(longest_subarray_len, len(A) - subarray_start_idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))

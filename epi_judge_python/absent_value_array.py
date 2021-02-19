from typing import Iterator
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    num_higher_order_bit_buckets = 1 << 16
    higher_order_bit_buckets = [0] * num_higher_order_bit_buckets
    stream1, stream2 = itertools.tee(stream)
    for num in stream1:
        higher_order_bit_buckets[num >> 16] += 1

    expected_bucket_size = 1 << 16
    bucket_with_missing_number = next(i for i, c in enumerate(higher_order_bit_buckets) if c < expected_bucket_size)
    candidates = [0] * expected_bucket_size
    for num in stream2:
        if bucket_with_missing_number == (num >> 16):
            candidates[((1 << 16) - 1) & num] = 1

    for i, count in enumerate(candidates):
        if count == 0:
            return (bucket_with_missing_number << 16) | i

    return 0


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))

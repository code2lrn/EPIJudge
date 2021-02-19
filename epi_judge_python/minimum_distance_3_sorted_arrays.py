from typing import List

from test_framework import generic_test


def find_closest_elements_in_sorted_arrays(sorted_arrays: List[List[int]]
                                           ) -> int:
    iters = []
    for i, a in enumerate(sorted_arrays):
        it = iter(a)
        iters.append((next(it, None), i, it))

    min_distance = float('inf')
    while True:
        min_tuple, max_tuple = (float('inf'), None, None), (float('-inf'), None, None)
        for entry in iters:
            if entry[0] is None:
                return min_distance

            min_tuple = min(min_tuple, entry)
            max_tuple = max(max_tuple, entry)

        min_distance = min(min_distance, max_tuple[0] - min_tuple[0])
        iters[min_tuple[1]] = (next(min_tuple[2], None), min_tuple[1], min_tuple[2])

    return min_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))

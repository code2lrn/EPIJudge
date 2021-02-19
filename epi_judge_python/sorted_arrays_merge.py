from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    array_iterators = [(iter(array), i) for i, array in enumerate(sorted_arrays)]
    min_heap: List[(int, int)] = []
    for entry in array_iterators:
        value, array_num = next(entry[0], None), entry[1]
        if value is not None:
            heapq.heappush(min_heap, (value, array_num))

    result = []
    while min_heap:
        smallest_num, smallest_num_array = heapq.heappop(min_heap)
        result.append(smallest_num)
        next_element_from_array = next(array_iterators[smallest_num_array][0], None)
        if next_element_from_array is not None:
            heapq.heappush(min_heap, (next_element_from_array, smallest_num_array))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))

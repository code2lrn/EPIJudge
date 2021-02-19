from typing import List
import heapq
from test_framework import generic_test, test_utils


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if k <= 0:
        return []

    result = []
    max_heap = [(-A[0], 0)]
    for _ in range(k):
        item_index = max_heap[0][1]
        result.append(-heapq.heappop(max_heap)[0])
        left_index, right_index = 2 * item_index + 1, 2 * item_index + 2
        if left_index < len(A):
            heapq.heappush(max_heap, (-A[left_index], left_index))
        if right_index < len(A):
            heapq.heappush(max_heap, (-A[right_index], right_index))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))

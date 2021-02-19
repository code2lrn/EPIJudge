from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    def length(start: ListNode) -> int:
        node_count = 0
        while start:
            node_count += 1
            start = start.next

        return node_count

    if not L:
        return L

    list_length = length(L)
    k = k % list_length
    if k == 0:
        return L

    kth = L
    for _ in range(0, k):
        kth = kth.next

    another_kth = L
    last = None
    while kth:
        another_kth, kth, last = another_kth.next, kth.next, kth

    last.next = L
    while last.next is not another_kth:
        last = last.next
    last.next = None

    return another_kth


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))

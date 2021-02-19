from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    root = sublist_prev = ListNode(0, L)
    for _ in range(1, start):
        sublist_prev = sublist_prev.next

    sublist_start = sublist_prev.next
    for _ in range(finish - start):
        temp = sublist_start.next
        sublist_start.next, temp.next, sublist_prev.next = temp.next, sublist_prev.next, temp

    return root.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))

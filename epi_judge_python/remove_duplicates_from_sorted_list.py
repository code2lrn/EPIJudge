from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    dummy = ListNode(0, L)
    it = dummy.next
    while it:
        next_distinct_node = it.next
        while next_distinct_node and next_distinct_node.data == it.data:
            next_distinct_node = next_distinct_node.next

        if next_distinct_node:
            it.next = next_distinct_node
            it = next_distinct_node
        else:
            it.next = None
            break

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))

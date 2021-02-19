from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    fast, slow = L, L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    def reverse_list(start: ListNode) -> ListNode:
        if not start or not start.next:
            return start

        new_head = None
        while start.next:
            temp = start.next
            start.next, new_head, start = new_head, start, temp

        start.next = new_head
        new_head = start

        return new_head

    left_it, right_it = L, reverse_list(slow)
    while left_it and right_it:
        if left_it.data != right_it.data:
            return False
        left_it, right_it = left_it.next, right_it.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))

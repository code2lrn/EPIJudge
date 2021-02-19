from list_node import ListNode


def reverse_sublist(head: ListNode, start: int, end: int) -> ListNode:
    saved_head = sublist_prev = ListNode(0, head)
    for _ in range(1, start):
        sublist_prev = sublist_prev.next

    sublist_start = sublist_prev.next
    for _ in range(end - start):
        temp = sublist_start.next
        sublist_start.next, temp.next, sublist_prev.next = temp.next, sublist_prev.next, temp

    return saved_head.next


def main():
    root = tail = ListNode(1)
    for i in range(2, 16):
        tail.next = ListNode(i)
        tail = tail.next

    print(root)
    root = reverse_sublist(root, 1, 5)
    print(root)
    root = reverse_sublist(root, 6, 10)
    print(root)
    root = reverse_sublist(root, 11, 15)
    print(root)


if __name__ == '__main__':
    main()
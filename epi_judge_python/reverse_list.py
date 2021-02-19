from list_node import ListNode


def reverse(root: ListNode) -> ListNode:
    if not root or not root.next:
        return root

    if not root.next.next:
        new_root, new_root.next, root.next = root.next, root, None
        return new_root

    one, two = root, root.next
    one.next = None
    while two.next:
        temp = two.next
        two.next = one
        one = two
        two = temp

    two.next = one
    return two


def main():
    root = tail = ListNode()
    for i in range(1, 10):
        tail.next = ListNode(i)
        tail = tail.next

    print(root)
    root = reverse(root)
    print(root)


if __name__ == '__main__':
    main()


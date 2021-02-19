from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def is_symmetric_recursive(n1: BinaryTreeNode, n2: BinaryTreeNode) -> bool:
        if not n1 and not n2:
            return True
        elif n1 and n2:
            return n1.data == n2.data and is_symmetric_recursive(n1.left, n2.right) and is_symmetric_recursive(n1.right, n2.left)

        return False

    return is_symmetric_recursive(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))

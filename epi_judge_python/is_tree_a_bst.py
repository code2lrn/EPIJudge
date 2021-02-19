from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import sys


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def bst_check_recursive(tree: BinaryTreeNode, min_range: int, max_range: int) -> bool:
        if not tree:
            return True

        if not min_range <= tree.data <= max_range:
            return False

        return bst_check_recursive(tree.left, min_range, tree.data) and bst_check_recursive(tree.right, tree.data, max_range)

    if not tree:
        return True

    return bst_check_recursive(tree.left, -sys.maxsize, tree.data) and bst_check_recursive(tree.right, tree.data, sys.maxsize)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))

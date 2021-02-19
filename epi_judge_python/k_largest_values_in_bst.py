from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def right_sided_inorder_traversal(node: BstNode):
        if node and len(k_largest_values) < k:
            right_sided_inorder_traversal(node.right)
            if len(k_largest_values) < k:
                k_largest_values.append(node.data)
                right_sided_inorder_traversal(node.left)

    k_largest_values = []
    right_sided_inorder_traversal(tree)
    return k_largest_values


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))

from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    inorder_index_by_node = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_po_io(pstart: int, pend: int, istart: int, iend: int) -> BinaryTreeNode:
        if pstart >= pend or istart >= iend:
            return None

        root_node_index = inorder_index_by_node[preorder[pstart]]
        left_subtree_size = root_node_index - istart
        return BinaryTreeNode(preorder[pstart],
                              binary_tree_from_po_io(pstart + 1, pstart + 1 + left_subtree_size, istart, left_subtree_size),
                              binary_tree_from_po_io(pstart + 1 + left_subtree_size, pend, left_subtree_size + 1, iend))

    return binary_tree_from_po_io(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))

from typing import List, Optional
from sys import maxsize
from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    def rebuild_bst(min_value: int, max_value: int) -> BstNode:
        nonlocal node_idx
        if node_idx >= len(preorder_sequence):
            return None

        node_value = preorder_sequence[node_idx]
        if min_value <= node_value <= max_value:
            node_idx += 1
            left = rebuild_bst(min_value, node_value)
            right = rebuild_bst(node_value, max_value)
            return BstNode(data=node_value, left=left, right=right)

        return None

    node_idx = 0
    return rebuild_bst(-maxsize, maxsize)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))

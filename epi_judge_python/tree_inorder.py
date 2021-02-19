from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    processing_stack = [(tree, False)]
    while processing_stack:
        node, left_subtree_processed = processing_stack.pop()
        if node:
            if left_subtree_processed:
                result.append(node.data)
            else:
                processing_stack.append((node.right, False))
                processing_stack.append((node, True))
                processing_stack.append((node.left, False))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))

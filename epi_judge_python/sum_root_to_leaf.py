from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_to_leaf(node: BinaryTreeNode, running_total: int) -> int:
        if not node:
            return 0

        latest_running_total = running_total * 2 + node.data
        if not node.left and not node.right:
            return latest_running_total

        sum_from_child_nodes = sum_to_leaf(node.left, latest_running_total) + sum_to_leaf(node.right, latest_running_total)
        return sum_from_child_nodes

    return sum_to_leaf(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedAndHeight = collections.namedtuple('BalancedAndHeight', ('Balanced', 'Height'))

    def is_balanced_recursive(node: BinaryTreeNode) -> BalancedAndHeight:
        if not node:
            return BalancedAndHeight(True, -1)

        left_outcome = is_balanced_recursive(node.left)
        if not left_outcome.Balanced:
            return left_outcome

        right_outcome = is_balanced_recursive(node.right)
        if not right_outcome.Balanced:
            return right_outcome

        is_balanced = (abs(left_outcome.Height - right_outcome.Height) <= 1)
        height = max(left_outcome.Height, right_outcome.Height) + 1
        return BalancedAndHeight(is_balanced, height)

    return is_balanced_recursive(tree).Balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

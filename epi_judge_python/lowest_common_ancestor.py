import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    NumNodesAndParent = collections.namedtuple('NumNodesAndParent', ('num_nodes', 'parent'))

    def lca_recursive(parent: BinaryTreeNode, n1: BinaryTreeNode, n2: BinaryTreeNode) -> NumNodesAndParent:
        if not parent:
            return NumNodesAndParent(0, None)

        left_outcome = lca_recursive(parent.left, n1, n2)
        if left_outcome.num_nodes == 2:
            return left_outcome

        right_outcome = lca_recursive(parent.right, n1, n2)
        if right_outcome.num_nodes == 2:
            return right_outcome

        num_nodes = left_outcome.num_nodes + right_outcome.num_nodes + (n1, n2).count(parent)
        return NumNodesAndParent(num_nodes, parent if num_nodes == 2 else None)

    return lca_recursive(tree, node0, node1).parent


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

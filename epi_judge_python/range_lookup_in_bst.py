import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    def range_lookup(node: BstNode):
        if not node:
            return None
        if interval.left <= node.data <= interval.right:
            range_lookup(node.left)
            result.append(node.data)
            range_lookup(node.right)
        elif interval.left > node.data:
            range_lookup(node.right)
        else:
            range_lookup(node.left)

    result = []
    range_lookup(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))

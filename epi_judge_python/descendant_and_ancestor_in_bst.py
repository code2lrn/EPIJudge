import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    p0, p1 = possible_anc_or_desc_0, possible_anc_or_desc_1
    while (p0 or p1)\
            and p0 is not possible_anc_or_desc_1\
            and p1 is not possible_anc_or_desc_0\
            and p0 is not middle\
            and p1 is not middle:
        if p0:
            p0 = p0.left if p0.data > middle.data else p0.right
        if p1:
            p1 = p1.left if p1.data > middle.data else p1.right

    if (p0 is not middle and p1 is not middle) or p0 is possible_anc_or_desc_1 or p1 is possible_anc_or_desc_0:
        return False

    def target_reachable(source: BstNode, target: BstNode) -> bool:
        while source and source is not target:
            source = source.left if source.data > target.data else source.right

        return source is target

    return target_reachable(middle, possible_anc_or_desc_0 if p1 is middle else possible_anc_or_desc_1)


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))

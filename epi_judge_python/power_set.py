from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    max_subsets = pow(2, len(input_set))
    power_sets: List[List[int]] = []
    for bitfield in range(max_subsets):
        subset = []
        for j in range(len(input_set)):
            if bitfield & (1 << j):
                subset.append(input_set[j])
        power_sets.append(subset)

    return power_sets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def generate(num_left, num_right, combination):
        if num_left > 0:
            generate(num_left - 1, num_right, combination + '(')

        if num_left < num_right:
            generate(num_left, num_right - 1, combination + ')')

        if num_right == 0:
            combinations.append(combination)

    combinations: List[str] = []
    generate(num_pairs, num_pairs, '')
    return combinations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

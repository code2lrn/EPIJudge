from test_framework import generic_test
import functools


def roman_to_integer(s: str) -> int:
    value_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return functools.reduce(lambda value, i: value + (-value_map[s[i]] if value_map[s[i]] < value_map[s[i + 1]] else value_map[s[i]]), reversed(range(len(s)-1)), value_map[s[-1]])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))

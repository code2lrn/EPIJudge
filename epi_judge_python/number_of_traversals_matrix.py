from test_framework import generic_test
from functools import lru_cache


def number_of_ways(n: int, m: int) -> int:
    @lru_cache(None)
    def ways_to_origin(x: int, y: int):
        if x == y == 0:
            return 1

        ways_up = 0 if x == 0 else ways_to_origin(x - 1, y)
        ways_left = 0 if y == 0 else ways_to_origin(x, y - 1)
        return ways_up + ways_left

    return ways_to_origin(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

from typing import List
from functools import lru_cache
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    @lru_cache(None)
    def search(gx: int, gy: int, px: int):
        if px == len(pattern):
            return True

        if (not (0 <= gx < len(grid) and 0 <= gy < len(grid[gx]))) or grid[gx][gy] != pattern[px]:
            return False

        return search(gx - 1, gy, px + 1)\
               or search(gx + 1, gy, px + 1)\
               or search(gx, gy - 1, px + 1)\
               or search(gx, gy + 1, px + 1)

    return any([search(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0]))])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))

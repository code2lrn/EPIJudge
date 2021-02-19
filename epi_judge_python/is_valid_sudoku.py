from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def valid_entries(entries: List[int]) -> bool:
        non_zero = list(filter(lambda x: x != 0, entries))
        return len(non_zero) == len(set(non_zero))

    # validate rows
    for row in partial_assignment:
        if not valid_entries(row):
            return False

    for col in range(9):
        values = []
        for row in range(9):
            values.append(partial_assignment[row][col])
        if not valid_entries(values):
            return False

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            values = [partial_assignment[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            if not valid_entries(values):
                return False

    return True


if __name__ == '__main__':
    # is_valid_sudoku([
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 9, 0, 0, 0, 0, 0],
    #     [0, 3, 2, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [9, 0, 4, 5, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 7, 0, 0, 6],
    #     [0, 0, 0, 6, 0, 5, 2, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 3, 0],
    #     [0, 0, 0, 0, 6, 2, 0, 0, 0]])
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))

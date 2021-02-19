from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def is_compliant(row, col) -> bool:
        return 0 == (column_placement[col] + diagonal[row - col] + anti_diagonal[row + col])

    def set_value(row: int, col: int, value: bool):
        column_placement[col] = value
        diagonal[row - col] = anti_diagonal[row + col] = value
        positions.add((row, col)) if value else positions.remove((row, col))

    def save_solution():
        solution = []
        for row, col in sorted(positions):
            solution.append('0' * col + 'X' + '0' * (n - col - 1))
        result.append(solution)

    def solve(row):
        for col in range(n):
            if is_compliant(row, col):
                set_value(row, col, True)
                if row + 1 == n:
                    save_solution()
                else:
                    solve(row + 1)
                set_value(row, col, False)

    column_placement, positions = [0] * n, set()
    diagonal, anti_diagonal = [0] * (2 * n - 1), [0] * (2 * n - 1)
    result: List[List[int]] = []
    solve(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    n_queens(10)
    # exit(
    #     generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
    #                                    comp))

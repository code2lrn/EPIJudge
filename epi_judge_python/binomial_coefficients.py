from test_framework import generic_test
from functools import lru_cache


@lru_cache(None)
def compute_binomial_coefficient(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1

    return compute_binomial_coefficient(n - 1, k) + compute_binomial_coefficient(n - 1, k - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))

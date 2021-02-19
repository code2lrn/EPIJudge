from test_framework import generic_test
from functools import lru_cache


def levenshtein_distance(A: str, B: str) -> int:
    @lru_cache(5000)
    def ld(a_idx: int, b_idx: int):
        if a_idx < 0:
            return b_idx + 1
        elif b_idx < 0:
            return a_idx + 1
        elif A[a_idx] == B[b_idx]:
            return ld(a_idx - 1, b_idx - 1)
        else:
            sub_last = ld(a_idx - 1, b_idx - 1)
            add_last = ld(a_idx, b_idx - 1)
            del_last = ld(a_idx - 1, b_idx)
            return 1 + min(sub_last, add_last, del_last)

    return ld(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))

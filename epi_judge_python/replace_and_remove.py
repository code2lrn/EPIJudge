import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    write_idx, num_a = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1

        if s[i] == 'a':
            num_a += 1

    # "d", "b", "b", "a", "b", "c", "a", "c", "a", "d", "a"
    # "d", "a", "c", "a", "c", "a", "d", "a"
    # "d", "d", "d", "c", "d", "d", "c", "d", "d", "d", "d", "d"

    read_idx, write_idx, new_size = write_idx - 1, write_idx + num_a - 1, write_idx + num_a
    while read_idx >= 0:
        ch = s[read_idx]
        if ch == 'a':
            s[write_idx] = 'd'
            write_idx -= 1
            s[write_idx] = 'd'
        else:
            s[write_idx] = ch

        read_idx, write_idx = read_idx - 1, write_idx - 1

    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))

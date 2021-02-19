import collections
import functools
from typing import List
from functools import lru_cache
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    @lru_cache(None)
    def fill_kp(n, c) -> int:
        if n < 0:
            return 0
        opt_1 = fill_kp(n - 1, c)
        opt_2 = 0 if c < items[n].weight else (items[n].value + fill_kp(n - 1, c - items[n].weight))
        return max(opt_1, opt_2)

    return fill_kp(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))

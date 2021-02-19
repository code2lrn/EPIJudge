import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def overlapping_interval(a: Interval, b: Interval) -> bool:
    return a.left <= b.left <= a.right or a.left <= b.right <= a.right or b.left <= a.left <= b.right or b.left <= a.right <= b.right


def compare_interval(a: Interval, b: Interval) -> int:
    if a.right < b.left:
        return -1
    elif a.left > b.right:
        return 1
    else:
        return 0


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    updated_intervals, adjusted_interval, adjusted_interval_available = [], new_interval, True
    for i, interval in enumerate(disjoint_intervals):
        if adjusted_interval_available:
            result = compare_interval(adjusted_interval, interval)
            if result < 0:
                updated_intervals.append(adjusted_interval)
                adjusted_interval_available = False
                updated_intervals.append(interval)
            elif result > 0:
                updated_intervals.append(interval)
            elif overlapping_interval(adjusted_interval, interval):
                adjusted_interval = Interval(min(adjusted_interval.left, interval.left), max(adjusted_interval.right, interval.right))
        else:
            updated_intervals.append(interval)

        if i == len(disjoint_intervals) - 1 and adjusted_interval_available:
            updated_intervals.append(adjusted_interval)

    return updated_intervals


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))

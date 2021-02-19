import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
EventTime = collections.namedtuple('EventTime', ('time', 'indicator'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    event_times_and_flags = [e for event in A for e in (EventTime(event.start, 1), EventTime(event.finish, -1))]
    event_times_and_flags.sort(key=lambda x: (x.time, not x.indicator > 0))
    concurrent_events = max_concurrent_events = 0
    for event in event_times_and_flags:
        concurrent_events += event.indicator
        max_concurrent_events = max(max_concurrent_events, concurrent_events)

    return max_concurrent_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))

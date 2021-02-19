from test_framework import generic_test
import itertools


def look_and_say(n: int) -> str:
    s = '1'
    for i in range(n-1):
        s = ''.join([str(len(list(ch_list))) + ch for ch, ch_list in itertools.groupby(s)])

    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))

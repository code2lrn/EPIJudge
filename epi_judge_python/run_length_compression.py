from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools


def decoding(s: str) -> str:
    run_length, decoded = 0, []
    for ch in s:
        if ch.isdigit():
            run_length = run_length * 10 + (ord(ch) - ord('0'))
        else:
            decoded.append(ch * run_length)
            run_length = 0

    return ''.join(decoded)


def encoding(s: str) -> str:
    return ''.join([str(len(list(ch_list))) + ch for ch, ch_list in itertools.groupby(s)])


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))

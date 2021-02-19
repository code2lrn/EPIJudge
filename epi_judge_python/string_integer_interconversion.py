from test_framework import generic_test
from test_framework.test_failure import TestFailure

from math import log10, floor


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    sign = '-' if x < 0 else ''
    x = abs(x)
    pow_of_10 = floor(log10(x))
    s = ['0'] * (pow_of_10 + 1)
    for i, e in enumerate(range(pow_of_10, -1 , -1)):
        d, x = divmod(x, 10 ** e)
        s[i] = chr(ord('0') + d)

    return sign + ''.join(s) if len(s) else '0'


def string_to_int(s: str) -> int:
    sign = -1 if s[0] == '-' else 1
    if (s[0] == '-' or s[0] == '+'):
        s = s[1:]

    pow_of_10 = len(s) - 1
    num = 0
    for i, e in enumerate(range(pow_of_10, -1, -1)):
        num += (ord(s[i]) - ord('0')) * (10 ** e)

    return sign * num


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))

from test_framework import generic_test
import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def convert_to_base_str(num: int, base: int):
        return '' if num == 0 else convert_to_base_str(num // base, base) + string.hexdigits[num % base].upper()

    if num_as_string == '0':
        return num_as_string

    is_negative = True if num_as_string[0] == '-' else False
    if is_negative:
        num_as_string = num_as_string[1:]

    int_b1 = functools.reduce(lambda val, ch: val * b1 + string.hexdigits.index(ch.lower()), num_as_string, 0)
    str_b2 = convert_to_base_str(int_b1, b2)
    return '' if int_b1 == 0 else ('-' if is_negative else '') + str_b2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))

from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if (len(num1) == 1 and num1[0] == 0) or (len(num2) == 1 and num2[0] == 0):
        return [0]

    is_negative = True if (num1[0] < 0) ^ (num2[0] < 0) else False
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    i = 0
    while result[i] == 0:
        i += 1
    result = result[i:]

    if is_negative:
        result[0] *= -1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))

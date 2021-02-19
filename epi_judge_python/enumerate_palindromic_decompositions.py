from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    def decompose(next_pos, palindromes):
        if next_pos == len(text):
            result.append(palindromes)
            return

        for i in range(next_pos + 1, len(text) + 1):
            region = text[next_pos:i]
            if region == region[::-1]:
                decompose(i, palindromes + [region])

    result: List[List[str]] = []
    decompose(0, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))

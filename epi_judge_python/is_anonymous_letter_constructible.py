from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_chars_required = Counter(letter_text)
    for ch in magazine_text:
        if ch in letter_chars_required:
            letter_chars_required[ch] -= 1

            if letter_chars_required[ch] == 0:
                del letter_chars_required[ch]

            if len(letter_chars_required) == 0:
                return True

    return len(letter_chars_required) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))

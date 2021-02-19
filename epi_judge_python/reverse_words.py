import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reserve_word(s: str, start: int, end: int):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    reserve_word(s, 0, len(s) - 1)
    word_start, i, word_end = 0, 0, 0
    while i < len(s):
        while i < len(s) and s[i] != ' ':
            i += 1

        word_end = i - 1
        reserve_word(s, word_start, word_end)
        word_start, i = i + 1, i + 1

    reserve_word(s, word_start, len(s) - 1)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))

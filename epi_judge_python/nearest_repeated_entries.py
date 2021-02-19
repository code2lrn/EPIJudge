from typing import List
import sys
from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    index_by_word, nearest_repeat_distance = {}, sys.maxsize
    for i, word in enumerate(paragraph):
        if word in index_by_word:
            nearest_repeat_distance = min(nearest_repeat_distance, i - index_by_word[word])
        index_by_word[word] = i
    return -1 if nearest_repeat_distance == sys.maxsize else nearest_repeat_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))

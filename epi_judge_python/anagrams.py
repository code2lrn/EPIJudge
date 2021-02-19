from typing import List, DefaultDict
from collections import defaultdict

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    words_by_anagram: DefaultDict[str, List[str]] = defaultdict(list)
    for s in dictionary:
        words_by_anagram[''.join(sorted(s))].append(s)
    return [v for v in words_by_anagram.values() if len(v) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))

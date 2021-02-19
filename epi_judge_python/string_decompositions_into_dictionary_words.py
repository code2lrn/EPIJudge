from typing import List
import copy
from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    word_hits_by_index, word_len, result = {}, len(words[0]), []
    for i in range(len(s) - len(words[0]) + 1):
        substr_word = s[i:i+word_len]
        if substr_word in words:
            word_hits_by_index[i] = substr_word
            if len(word_hits_by_index) >= len(words):
                words_to_find = copy.deepcopy(words)
                words_to_find.remove(substr_word)
                pattern = [substr_word]
                j = i - word_len
                while j >= 0 and words_to_find:
                    if j in word_hits_by_index and word_hits_by_index[j] in words_to_find:
                        words_to_find.remove(word_hits_by_index[j])
                        pattern.append(word_hits_by_index[j])
                        j -= word_len
                    else:
                        break

                if len(pattern) == len(words):
                    result.append(j + word_len)

    return result


if __name__ == '__main__':
    # find_all_substrings('rndljjljjrndkzxljjrndsnq', ["rnd", "ljj", "kzx"])
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))

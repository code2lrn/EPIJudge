from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    char_mapping = {'0': '0', '1': '1',
                    '2': 'ABC', '3': 'DEF', '4': 'GHI',
                    '5': 'JKL', '6': 'MNO', '7': 'PQRS',
                    '8': 'TUV', '9': 'WXYZ'}

    def create_mnemonic(char_idx: int):
        if char_idx == len(phone_number):
            mnemonics.append(''.join(mnemonic_being_created))
            return

        for ch in char_mapping[phone_number[char_idx]]:
            mnemonic_being_created[char_idx] = ch
            create_mnemonic(char_idx + 1)

    mnemonics = []
    mnemonic_being_created = ['0'] * len(phone_number)
    create_mnemonic(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))

from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    if len(s) < 4 or len(s) > 12:
        return []

    def is_valid_prefix(p: str):
        return len(p) == 1 or (p[0] != '0' and int(p) <= 255)

    valid_ips = []
    for i in range(1, min(4, len(s))):
        part_1 = s[:i]
        if not is_valid_prefix(part_1):
            continue
        for j in range(1, min(4, len(s) - i)):
            part_2 = s[i:i + j]
            if not is_valid_prefix(part_2):
                continue
            for k in range(1, min(4, len(s) - i - j)):
                part_3 = s[i + j:i + j + k]
                part_4 = s[i + j + k:]
                if is_valid_prefix(part_3) and is_valid_prefix(part_4):
                    valid_ips.append('{}.{}.{}.{}'.format(part_1, part_2, part_3, part_4))

    return valid_ips


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))

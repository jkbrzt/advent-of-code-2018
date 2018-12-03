"""
https://adventofcode.com/2018/day/2

"""
from collections import Counter
from itertools import product
from pathlib import Path


def solve_a(codes):
    pairs = 0
    triplets = 0
    for code in codes:
        occurrences = Counter(code).values()
        pairs += any(count == 2 for count in occurrences)
        triplets += any(count == 3 for count in occurrences)
    return pairs * triplets


def solve_b(codes):
    for code_a, code_b in product(codes, codes):
        diff = sum(c != c2 for c, c2 in zip(code_a, code_b))
        if diff == 1:
            common = ''.join(c for c, c2 in zip(code_a, code_b) if c == c2)
            return common


if __name__ == '__main__':
    assert 12 == solve_a([
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab',
    ])
    assert 'fgij' == solve_b([
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ])
    codes = Path('day02.txt').read_text().strip().splitlines()
    print('A:', solve_a(codes))
    print('B:', solve_b(codes))

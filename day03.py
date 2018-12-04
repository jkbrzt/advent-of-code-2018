"""
https://adventofcode.com/2018/day/3

"""
from collections import defaultdict
from itertools import product
from pathlib import Path


def solve_a(lines):
    fabric = defaultdict(int)
    for line in lines:
        id, pixels = parse(line)
        for loc in pixels:
            fabric[loc] += 1
    return sum(count > 1 for count in fabric.values())


def solve_b(lines):
    fabric = defaultdict(set)
    for line in lines:
        id, pixels = parse(line)
        for loc in pixels:
            fabric[loc].add(id)
    for line in lines:
        id, pixels = parse(line)
        only_me = {id}
        for loc in pixels:
            if fabric[loc] != only_me:
                break
        else:
            return id


def parse(line):
    id, params = line[1:].split(' @ ')
    coords, size = params.split(': ')
    x, y = map(int, coords.split(','))
    w, h = map(int, size.split('x'))
    return id, product(
        range(x + 1, x + w + 1),
        range(y + 1, y + h + 1),
    )


if __name__ == '__main__':
    assert 4 == solve_a([
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ])
    assert '3' == solve_b([
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ])
    lines = Path('day03.txt').read_text().strip().splitlines()
    print('A:', solve_a(lines))
    print('B:', solve_b(lines))

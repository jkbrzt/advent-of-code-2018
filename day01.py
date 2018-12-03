"""
https://adventofcode.com/2018/day/1

"""
from pathlib import Path


def solve_a(changes):
    return sum(changes)


def solve_b(changes):
    freq, history = 0, {0}
    while True:
        for change in changes:
            freq += change
            if freq in history:
                return freq
            history.add(freq)


if __name__ == '__main__':
    assert solve_a([+1, +1, +1]) == +3
    assert solve_a([+1, +1, -2]) == +0
    assert solve_a([-1, -2, -3]) == -6
    assert solve_b([+1, -1]) == 0
    assert solve_b([+3, +3, +4, -2, -4]) == 10
    assert solve_b([-6, +3, +8, +5, -6]) == 5
    assert solve_b([+7, +7, -2, -7, -4]) == 14
    changes = list(map(int, Path('day01.txt').read_text().split()))
    print('A:', solve_a(changes))
    print('B:', solve_b(changes))

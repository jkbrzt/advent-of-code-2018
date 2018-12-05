"""
https://adventofcode.com/2018/day/5

"""
from pathlib import Path


def solve_a(polymer):
    """
    The polymer is formed by smaller units which, when triggered, react with
    each other such that two adjacent units of the same type and opposite
    polarity are destroyed. Units' types are represented by letters; units'
    polarity is represented by capitalization. For instance, r and R are units
    with the same type but opposite polarity, whereas r and s are entirely
    different types and do not react.

    dabAcCaCBAcCcaDA  The first 'cC' is removed.
    dabAaCBAcCcaDA    This creates 'Aa', which is removed.
    dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
    dabCBAcaDA        No further actions can be taken.

    After all possible reactions, the resulting polymer contains 10 units.

    """
    collapsed = list(polymer)
    i = 0
    while True:
        try:
            unit = collapsed[i]
        except IndexError:
            break
        try:
            unit_next = collapsed[i + 1]
        except IndexError:
            pass
        else:
            if unit == unit_next.swapcase():
                del collapsed[i:i+2]
                i = max(0, i - 1)
                continue
        i += 1
    return len(collapsed)


def solve_b(polymer):
    """
    One of the unit types is causing problems; it's preventing the polymer
    from collapsing as much as it should. Your goal is to figure out which
    unit type is causing the most problems, remove all instances of it
    (regardless of polarity), fully react the remaining polymer, and measure
    its length.

    For example, again using the polymer dabAcCaCBAcCcaDA from above:

    Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
    Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
    Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
    Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
    In this example, removing all C/c units was best, producing the answer 4.

    """
    unique_units = set(polymer.lower())
    results = {}
    for try_without in unique_units:
        collapsed = list(
            polymer.replace(try_without, '')
                   .replace(try_without.upper(), '')
        )
        i = 0
        while True:
            try:
                unit = collapsed[i]
            except IndexError:
                break
            try:
                unit_next = collapsed[i + 1]
            except IndexError:
                pass
            else:
                if unit == unit_next.swapcase():
                    del collapsed[i:i+2]
                    i = max(0, i - 1)
                    continue
            i += 1
        results[try_without] = len(collapsed)
    return min(results.values())


if __name__ == '__main__':
    assert solve_a('dabAcCaCBAcCcaDA') == 10
    assert solve_b('dabAcCaCBAcCcaDA') == 4
    polymer = Path('day05.txt').read_text().strip()
    print('A:', solve_a(polymer))
    print('B:', solve_b(polymer))

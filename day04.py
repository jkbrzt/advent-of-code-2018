"""
https://adventofcode.com/2018/day/4

"""
import re
from collections import defaultdict
from pathlib import Path

from dataclasses import dataclass


def solve_a(lines):
    entries = parse_lines(lines)
    by_guard, totals = defaultdict(list), defaultdict(int)
    asleep_at = None
    for entry in entries:
        by_guard[entry.guard].append(entry)
        if entry.asleep():
            asleep_at = entry.time
        elif entry.awake():
            totals[entry.guard] += entry.time - asleep_at
            asleep_at = None
    biggest_sleeper = max(
        totals.keys(),
        key=lambda guard: totals[guard]
    )
    it = iter(by_guard[biggest_sleeper])
    minute_map = defaultdict(int)
    for entry in it:
        if entry.asleep():
            for minute in range(entry.time, next(it).time):
                minute_map[minute % 60] += 1
    most_sleepy_minute = max(
        minute_map.keys(),
        key=lambda minute: minute_map[minute]
    )
    return biggest_sleeper * most_sleepy_minute


def solve_b(lines):
    entries, by_guard = parse_lines(lines), defaultdict(list)
    for entry in entries:
        by_guard[entry.guard].append(entry)
    sleepiest_overall = {}
    for guard, entries in by_guard.items():
        it, slept = iter(entries), defaultdict(int)
        for entry in it:
            if entry.asleep():
                for minute in range(entry.time, next(it).time):
                    slept[minute % 60] += 1
        if slept:
            sleepiest = max(slept.keys(), key=lambda minute: slept[minute])
            sleepiest_overall[(guard, sleepiest)] = slept[sleepiest]
    guard, minute = max(
        sleepiest_overall.keys(),
        key=lambda key: sleepiest_overall[key]
    )
    return guard * minute


def parse_lines(lines):
    entries = []
    for line in sorted(lines):
        current_guard = None if not entries else entries[-1].guard
        entries.append(Entry.from_log(line, guard=current_guard))
    return entries


@dataclass
class Entry:
    date: str
    time: int
    guard: int
    action: str

    def asleep(self):
        return self.action == 'asleep'

    def awake(self):
        return self.action == 'awake'

    @classmethod
    def from_log(cls, line, guard=None):
        match = re.match('^\[(.+?) (\d{2}):(\d{2})\] (.+)$', line)
        action = match.group(4)
        if 'begins' in action:
            guard = int(re.search('\d+', action).group(0))
            action = 'start'
        elif 'asleep' in action:
            action = 'asleep'
        else:
            action = 'awake'
        return cls(
            date=match.group(1),
            time=int(match.group(2)) * 60 + int(match.group(3)),
            guard=guard,
            action=action
        )


if __name__ == '__main__':
    test_input = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
    """.strip().splitlines()
    assert 240 == solve_a(test_input)
    assert 4455 == solve_b(test_input)
    lines = Path('day04.txt').read_text().strip().splitlines()
    solution_a = solve_a(lines)
    assert solution_a == 151754
    print('A:', solution_a)
    solution_b = solve_b(lines)
    assert solution_b == 19896
    print('B:', solution_b)

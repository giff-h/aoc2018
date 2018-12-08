#!/usr/bin/env python3.6
import collections
import re

from py import load_input_lines

timestamp = re.compile(r"\[\d{4}-\d{2}-\d{2} (\d{2}):(\d{2})]")
guard_re = re.compile(r"Guard #(\d+)")


def _build_guard_rotations(rotations):
    guards = collections.defaultdict(lambda: {"count": 0, "minutes": [], "most_common": (0, 0)})
    current_guard = ""
    asleep = 0
    for rotation in sorted(rotations):
        if "Guard" in rotation:
            current_guard = guard_re.search(rotation).groups()[0]
        else:
            hour, minute = timestamp.search(rotation).groups()
            time = int(hour) * 60 + int(minute)
            if "falls" in rotation:
                asleep = time
            else:
                awake = time
                guards[current_guard]["minutes"].extend(range(asleep, awake))
                guards[current_guard]["count"] += awake - asleep

    for guard in guards.values():
        guard["most_common"] = collections.Counter(guard["minutes"]).most_common(1)[0]

    return guards


def part1(puzzle_input):
    guards = _build_guard_rotations(puzzle_input)

    guard, data = max(guards.items(), key=lambda g: g[1]["count"])
    return int(guard) * data["most_common"][0]


def part2(puzzle_input):
    guards = _build_guard_rotations(puzzle_input)

    guard, data = max(guards.items(), key=lambda g: g[1]["most_common"][1])
    return int(guard) * data["most_common"][0]


def run():
    today = load_input_lines()

    test = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]

    assert part1(test) == 240

    print(f"Day 4 part 1: {part1(today)}")

    assert part2(test) == 4455

    print(f"Day 4 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

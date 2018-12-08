#!/usr/bin/env python3.6
import itertools

from py import load_input_lines


def part1(puzzle_input):
    return sum(map(int, puzzle_input))


def part2(puzzle_input):
    cycle = 0
    sums = {cycle}
    for i in map(int, itertools.cycle(puzzle_input)):
        cycle += i
        if cycle in sums:
            return cycle
        sums.add(cycle)


def run():
    today = load_input_lines()

    assert part1(["+1", "+1", "+1"]) == 3
    assert part1(["+1", "+1", "-2"]) == 0
    assert part1(["-1", "-2", "-3"]) == -6

    print(f"Day 1 part 1: {part1(today)}")

    assert part2(["+1", "-1"]) == 0
    assert part2(["+3", "+3", "+4", "-2", "-4"]) == 10
    assert part2(["-6", "+3", "+8", "+5", "-6"]) == 5
    assert part2(["+7", "+7", "-2", "-7", "-4"]) == 14

    print(f"Day 1 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

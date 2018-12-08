#!/usr/bin/env python3.6
import functools

from py import load_input_raw


def _react(polymer, c):
    return polymer[:-1] if len(polymer) and polymer[-1] == c.swapcase() else polymer + c


def part1(puzzle_input):
    return len(functools.reduce(_react, puzzle_input, ""))


def part2(puzzle_input):
    return min(part1(puzzle_input.replace(c, "").replace(c.upper(), "")) for c in set(puzzle_input.lower()))


def run():
    today = load_input_raw()

    test = "dabAcCaCBAcCcaDA"

    assert part1(test) == 10

    print(f"Day 5 part 1: {part1(today)}")

    assert part2(test) == 4

    print(f"Day 5 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

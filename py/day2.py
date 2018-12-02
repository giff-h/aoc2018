#!/usr/bin/env python3.6
import collections

from py import load_input_lines


def part1(puzzle_input):
    counts = [collections.Counter(box).values() for box in puzzle_input]
    twos = 0
    threes = 0
    for count in counts:
        if 2 in count:
            twos += 1
        if 3 in count:
            threes += 1
    return twos * threes


def part2(puzzle_input):
    for i, box in enumerate(puzzle_input):
        for other_box in puzzle_input[:i] + puzzle_input[i + 1:]:
            for j in range(len(other_box)):
                smaller_box = box[:j] + box[j + 1:]
                smaller_other_box = other_box[:j] + other_box[j + 1:]
                if smaller_box == smaller_other_box:
                    return smaller_box


def run():
    day2 = load_input_lines()

    assert part1([
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]) == 12

    print(f"Day 2 part 1: {part1(day2)}")

    assert part2([
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]) == "fgij"

    print(f"Day 2 part 2: {part2(day2)}")


if __name__ == "__main__":
    run()

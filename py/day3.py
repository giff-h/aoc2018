#!/usr/bin/env python3.6
import re

from py import load_input_lines

pattern = re.compile(r"#(?P<claim>\d+) @ (?P<left_border>\d+),(?P<top_border>\d+): (?P<width>\d+)x(?P<height>\d+)")


def part1(puzzle_input):
    fabric = [[0] * 1000 for _ in range(1000)]

    for claim in map(pattern.match, puzzle_input):
        left_border = int(claim["left_border"])
        top_border = int(claim["top_border"])
        width = int(claim["width"])
        height = int(claim["height"])
        for y in range(top_border, top_border + height):
            fabric[y][left_border:left_border + width] = [i + 1 for i in fabric[y][left_border:left_border + width]]

    return sum(1 for row in fabric for x in row if x >= 2)


def part2(puzzle_input):
    fabric = [[None] * 1000 for _ in range(1000)]
    possible = set()

    for claim in map(pattern.match, puzzle_input):
        claim_id = int(claim["claim"])
        left_border = int(claim["left_border"])
        top_border = int(claim["top_border"])
        width = int(claim["width"])
        height = int(claim["height"])

        add_claim = True
        for y in range(top_border, top_border + height):
            row = fabric[y][left_border:left_border + width]
            already = set(filter(None, row))
            if len(already):
                add_claim = False
                possible -= already
            fabric[y][left_border:left_border + width] = [claim_id] * width
        if add_claim:
            possible.add(claim_id)

    return possible


def run():
    today = load_input_lines()

    test = [
        "#1 @ 1,3: 4x4",
        "#2 @ 3,1: 4x4",
        "#3 @ 5,5: 2x2",
    ]

    assert part1(test) == 4

    print(f"Day 3 part 1: {part1(today)}")

    assert part2(test) == {3}

    print(f"Day 3 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

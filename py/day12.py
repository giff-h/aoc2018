#!/usr/bin/env python3.6
from py import load_input_lines


def _next_generation(generation, rules, shift):
    generation = "...." + generation + "...."
    next_generation = "".join(rules.get(generation[pot:pot + 5], ".") for pot in range(len(generation) - 4))
    shift += -2 + next_generation.index("#")
    return next_generation.strip("."), shift


def _plant_count(pots, shift):
    return sum(i + shift for i, plant in enumerate(pots) if plant == "#")


def part1(puzzle_input, generations=20):
    prev_generation = puzzle_input[0].lstrip("initial state: ")
    rules = dict(rule.split(" => ") for rule in puzzle_input[1:])
    shift = 0

    for i in range(1, generations + 1):
        next_generation, shift = _next_generation(prev_generation, rules, shift)
        if next_generation == prev_generation:
            magic = _plant_count(prev_generation, shift) // i
            return magic * generations
        prev_generation = next_generation

    return _plant_count(prev_generation, shift)


def part2(puzzle_input):
    return part1(puzzle_input, 50000000000)


def run():
    today = load_input_lines()

    test = [
        "initial state: #..#.#..##......###...###",
        "...## => #",
        "..#.. => #",
        ".#... => #",
        ".#.#. => #",
        ".#.## => #",
        ".##.. => #",
        ".#### => #",
        "#.#.# => #",
        "#.### => #",
        "##.#. => #",
        "##.## => #",
        "###.. => #",
        "###.# => #",
        "####. => #",
    ]

    assert part1(test) == 325

    print(f"Day 12 part 1: {part1(today)}")

    # assert part2(test)

    print(f"Day 12 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

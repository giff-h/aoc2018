#!/usr/bin/env python3.6
def part1(puzzle_input):
    all_scores = "37"
    elves = [0, 1]
    while len(all_scores) < puzzle_input + 10:
        elfs_recipes = [int(all_scores[elf]) for elf in elves]
        all_scores += str(sum(elfs_recipes))
        elves = [(elf + r + 1) % len(all_scores) for elf, r in zip(elves, elfs_recipes)]

    return all_scores[puzzle_input:puzzle_input + 10]


def part2(puzzle_input):
    puzzle_input = str(puzzle_input)
    all_scores = "37"
    elves = [0, 1]
    while puzzle_input not in all_scores[-1 * (len(puzzle_input) + 2):]:
        elfs_recipes = [int(all_scores[elf]) for elf in elves]
        all_scores += str(sum(elfs_recipes))
        elves = [(elf + r + 1) % len(all_scores) for elf, r in zip(elves, elfs_recipes)]

    return all_scores.index(puzzle_input)


def run():
    today = 509671

    assert part1(9) == "5158916779"
    assert part1(5) == "0124515891"
    assert part1(18) == "9251071085"
    assert part1(2018) == "5941429882"

    print(f"Day 14 part 1: {part1(today)}")

    assert part2("51589") == 9
    assert part2("01245") == 5
    assert part2("92510") == 18
    assert part2("59414") == 2018

    print(f"Day 14 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

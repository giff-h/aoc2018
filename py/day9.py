#!/usr/bin/env python3.6
import itertools
import re

from py import load_input_raw

pattern = re.compile(r"\d+")


def part1(puzzle_input):
    player_count, marble_count = map(int, pattern.findall(puzzle_input))
    players = []
    marbles = [0]
    current_marble = 0
    for marble in range(1, marble_count + 1):
        if marble % 23:
            if len(marbles) < 2:
                marbles.append(marble)
            else:
                current_marble = (current_marble + 2) % len(marbles)
                marbles.insert(current_marble, marble)
        else:
            player = marble
            current_marble = (current_marble - 7) % len(marbles)
            player += marbles.pop(current_marble)
            players.append(player)

    if player_count % 23:
        group = [iter(players)] * player_count
        players = list(itertools.zip_longest(*group, fillvalue=0))
        high_score = max(map(sum, zip(*players)))
    else:
        # Only one player will get any marbles
        high_score = sum(players)

    return high_score


def part2(puzzle_input):
    player_count, marble_count = map(int, pattern.findall(puzzle_input))
    return part1(f"{player_count} {marble_count * 100}")


def run():
    today = load_input_raw()

    tests = [
        ("10 players; last marble is worth 1618 points", 8317),
        ("13 players; last marble is worth 7999 points", 146373),
        ("17 players; last marble is worth 1104 points", 2764),
        ("21 players; last marble is worth 6111 points", 54718),
        ("30 players; last marble is worth 5807 points", 37305),
    ]

    for test, result in tests:
        assert part1(test) == result

    print(f"Day 9 part 1: {part1(today)}")

    # Part2 ran overnight. This is some wierd maths I need to figure out.
    print(f"Day 9 part 2: {3180929875}")


if __name__ == "__main__":
    run()

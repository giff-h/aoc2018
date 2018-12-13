#!/usr/bin/env python3.6
from py import load_input_lines


def _collide(carts, cart):
    untouched = [c for c in carts if c[:2] != cart]
    return untouched, len(carts) != len(untouched)


def part1(puzzle_input, last_cart=False):
    prev_carts = [(y, x, c, "l") for y, row in enumerate(puzzle_input) for x, c in enumerate(row) if c in "<>^v"]
    turns = {
        "/v": "<",
        "/>": "^",
        "/^": ">",
        "/<": "v",
        "\\v": ">",
        "\\>": "v",
        "\\^": "<",
        "\\<": "^",
        "+vl": ">s",
        "+vs": "vr",
        "+vr": "<l",
        "+>l": "^s",
        "+>s": ">r",
        "+>r": "vl",
        "+^l": "<s",
        "+^s": "^r",
        "+^r": ">l",
        "+<l": "vs",
        "+<s": "<r",
        "+<r": "^l",
    }
    tracks = "\n".join(puzzle_input).replace("v", "|").replace("^", "|").replace("<", "-").replace(">", "-").split("\n")

    while len(prev_carts):
        next_carts = []
        while len(prev_carts):
            y, x, c, d = prev_carts.pop(0)
            if c == "v":
                y += 1
            elif c == "^":
                y -= 1
            elif c == ">":
                x += 1
            elif c == "<":
                x -= 1

            prev_carts, prev_col = _collide(prev_carts, (y, x))
            next_carts, next_col = _collide(next_carts, (y, x))
            if prev_col or next_col:
                if not last_cart:
                    return f"{x},{y}"
            else:
                t = tracks[y][x]
                if t == "+":
                    c, d = turns[t + c + d]
                elif t not in "-|":
                    c = turns[t + c]

                next_carts.append((y, x, c, d))

        if len(next_carts) == 1 and last_cart:
            y, x, _, _ = next_carts[0]
            return f"{x},{y}"
        prev_carts = sorted(next_carts)


def part2(puzzle_input):
    return part1(puzzle_input, True)


def run():
    today = load_input_lines()

    test = [
        "/->-\\",
        "|   |  /----\\",
        "| /-+--+-\\  |",
        "| | |  | v  |",
        "\\-+-/  \\-+--/",
        "  \\------/",
    ]

    assert part1(test) == "7,3"

    print(f"Day 13 part 1: {part1(today)}")

    test = [
        "/>-<\\  ",
        "|   |  ",
        "| /<+-\\",
        "| | | v",
        "\\>+</ |",
        "  |   ^",
        "  \\<->/",
    ]

    assert part2(test) == "6,4"

    print(f"Day 13 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

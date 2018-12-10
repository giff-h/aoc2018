#!/usr/bin/env python3.6
import collections
import itertools
import re

from py import load_input_lines

numbers = re.compile(r"-?\d+")


def move(point):
    px, py, vx, vy = point
    return px + vx, py + vy, vx, vy


def adjust(point, min_x, min_y):
    return point[0] - min_x, point[1] - min_y, point[2], point[3]


def find_message(points, seconds, is_test):
    transposed = collections.defaultdict(set)
    all_xy = tuple(zip(*points))[:2]
    min_x, min_y = tuple(map(min, all_xy))
    max_x, max_y = tuple(map(max, all_xy))
    width = max_x - min_x
    height = max_y - min_y
    if height <= 15:
        board = [["."] * (width + 1) for _ in range(height + 1)]
        for x, y, _, _ in points:
            transposed[x - min_x].add(y - min_y)
            board[y - min_y][x - min_x] = "#"

        if len(tuple(transposed.keys())) >= width * 0.6:
            if sum(1 for column in transposed.values() if column.issuperset(range(1, height - 1))) >= 3:
                if not is_test:
                    print("\n".join(map("".join, board)))
                return seconds


def part1(puzzle_input, is_test=False):
    points = [tuple(map(int, point)) for point in map(numbers.findall, puzzle_input)]
    min_x, min_y = tuple(map(min, tuple(zip(*points))[:2]))
    points = [adjust(point, min_x, min_y) for point in points]
    max_x, max_y = tuple(map(max, tuple(zip(*points))[:2]))
    for i in itertools.count():
        if not all(0 <= point[0] <= max_x and 0 <= point[1] <= max_y for point in points):
            break
        seconds = find_message(points, i, is_test)
        if seconds:
            return seconds
        points = list(map(move, points))


# def part2(puzzle_input):
#     pass


def run():
    today = load_input_lines()

    test = [
        "position=< 9,  1> velocity=< 0,  2>",
        "position=< 7,  0> velocity=<-1,  0>",
        "position=< 3, -2> velocity=<-1,  1>",
        "position=< 6, 10> velocity=<-2, -1>",
        "position=< 2, -4> velocity=< 2,  2>",
        "position=<-6, 10> velocity=< 2, -2>",
        "position=< 1,  8> velocity=< 1, -1>",
        "position=< 1,  7> velocity=< 1,  0>",
        "position=<-3, 11> velocity=< 1, -2>",
        "position=< 7,  6> velocity=<-1, -1>",
        "position=<-2,  3> velocity=< 1,  0>",
        "position=<-4,  3> velocity=< 2,  0>",
        "position=<10, -3> velocity=<-1,  1>",
        "position=< 5, 11> velocity=< 1, -2>",
        "position=< 4,  7> velocity=< 0, -1>",
        "position=< 8, -2> velocity=< 0,  1>",
        "position=<15,  0> velocity=<-2,  0>",
        "position=< 1,  6> velocity=< 1,  0>",
        "position=< 8,  9> velocity=< 0, -1>",
        "position=< 3,  3> velocity=<-1,  1>",
        "position=< 0,  5> velocity=< 0, -1>",
        "position=<-2,  2> velocity=< 2,  0>",
        "position=< 5, -2> velocity=< 1,  2>",
        "position=< 1,  4> velocity=< 2,  1>",
        "position=<-2,  7> velocity=< 2, -2>",
        "position=< 3,  6> velocity=<-1, -1>",
        "position=< 5,  0> velocity=< 1,  0>",
        "position=<-6,  0> velocity=< 2,  0>",
        "position=< 5,  9> velocity=< 1, -2>",
        "position=<14,  7> velocity=<-2,  0>",
        "position=<-3,  6> velocity=< 2, -1>",
    ]

    assert part1(test, True) == 3

    print("Day 10 part 1:")
    print(f"Day 10 part 2: {part1(today)}")

    # assert part2(test)

    # print(f"Day 10 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

#!/usr/bin/env python3.6
import itertools


def _power_level(x, y, serial):
    return int(str((x * y + serial) * x).rjust(3, "0")[-3]) - 5


def _build_grid(serial):
    return [[_power_level(x, y, serial) for x in range(11, 311)] for y in range(1, 301)]


def _square_power(x, y, size, grid):
    return sum(sum(row[x:x + size]) for row in grid[y:y + size])


def part1(puzzle_input):
    cell_grid = _build_grid(puzzle_input)
    box_range = range(1, len(cell_grid) - 1)
    return ",".join(map(str, max(((x, y) for x in box_range for y in box_range),
                                 key=lambda point: _square_power(point[0] - 1, point[1] - 1, 3, cell_grid))))


def part2(puzzle_input):
    cell_grid = _build_grid(puzzle_input)
    box_range = range(1, len(cell_grid) - 8)
    max_point = max(((x, y, size)
                     for x, y in itertools.product(box_range, box_range)
                     for size in range(10, min(20, len(cell_grid) - max(x, y)))),
                    key=lambda point: _square_power(point[0] - 1, point[1] - 1, point[2], cell_grid))
    return ",".join(map(str, max_point))


def run():
    today = 4455

    assert part1(18) == "33,45"
    assert part1(42) == "21,61"

    print(f"Day 11 part 1: {part1(today)}")

    assert part2(18) == "90,269,16"
    assert part2(42) == "232,251,12"

    print(f"Day 11 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

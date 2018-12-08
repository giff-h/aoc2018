#!/usr/bin/env python3.6
import collections
import itertools

from py import load_input_lines


def _parse_point(line):
    return tuple(map(int, line.split(", ")))


def _direction(a, b):
    return -1 if a > b else 1


def _range_zip(start_x, end_x, start_y, end_y, min_x, min_y, max_x, max_y):
    for x, y in zip(range(start_x, end_x, _direction(start_x, end_x)),
                    range(start_y, end_y, _direction(start_y, end_y))):
        if min_x <= x <= max_x and min_y <= y <= max_y:
            yield x, y


def _surrounding_points(point, min_x, min_y, max_x, max_y):
    x, y = point
    for i in itertools.count(1):
        batch = []
        start_x, start_y = x - i, y
        end_x, end_y = x, y - i
        batch.extend(_range_zip(start_x, end_x, start_y, end_y, min_x, min_y, max_x, max_y))
        start_x += 2 * i
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
        batch.extend(_range_zip(start_x, end_x, start_y, end_y, min_x, min_y, max_x, max_y))
        start_y += 2 * i
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
        batch.extend(_range_zip(start_x, end_x, start_y, end_y, min_x, min_y, max_x, max_y))
        start_x -= 2 * i
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
        batch.extend(_range_zip(start_x, end_x, start_y, end_y, min_x, min_y, max_x, max_y))
        yield batch


def part1(puzzle_input):
    points = list(map(_parse_point, puzzle_input))
    max_x, max_y = tuple(map(max, zip(*points)))
    min_x, min_y = tuple(map(min, zip(*points)))
    blob_iterators = [_surrounding_points(point, min_x, min_y, max_x, max_y) for point in points]
    closest_homes = dict()
    edge_points = set()

    while True:
        wave = {point: [p for p in next(blob) if p not in closest_homes and p not in points]
                for point, blob in zip(points, blob_iterators)}
        full_blob = [point for blob in wave.values() for point in blob]
        if not any(full_blob.count(point) == 1 for point in set(full_blob)):
            break
        for home, blob in wave.items():
            for point in blob:
                point_count = full_blob.count(point)
                if point_count == 1:
                    if point[0] in (min_x, max_x) or point[1] in (min_y, max_y):
                        edge_points.add(home)
                        home = None
                    closest_homes[point] = home
                elif point_count > 1:
                    closest_homes[point] = None
    counts = collections.Counter(point for point in closest_homes.values() if point and point not in edge_points)
    return counts.most_common(1)[0][1] + 1  # Include the original home point


def _distance(point_a, point_b):
    ax, ay = point_a
    bx, by = point_b
    return abs(ax - bx) + abs(ay - by)


def part2(puzzle_input, limit):
    points = list(map(_parse_point, puzzle_input))
    max_x, max_y = tuple(map(max, zip(*points)))
    min_x, min_y = tuple(map(min, zip(*points)))
    grid_iter = itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))
    return sum(1 for x, y in grid_iter if sum(_distance(point, (x, y)) for point in points) < limit)


def run():
    today = load_input_lines()

    test = [
        "1, 1",
        "1, 6",
        "8, 3",
        "3, 4",
        "5, 5",
        "8, 9",
    ]

    assert part1(test) == 17

    print(f"Day 6 part 1: {part1(today)}")

    assert part2(test, 32) == 16

    print(f"Day 6 part 2: {part2(today, 10000)}")


if __name__ == "__main__":
    run()

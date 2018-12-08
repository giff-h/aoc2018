#!/usr/bin/env python3.6
from py import load_input_raw


def _metadata_sum(data):
    (child_count, metadata_count), data = data[:2], data[2:]
    metadata_sum = 0
    for child in range(child_count):
        inc, data = _metadata_sum(data)
        metadata_sum += inc
    metadata_sum += sum(data[:metadata_count])

    return metadata_sum, data[metadata_count:]


def part1(puzzle_input):
    data = list(map(int, puzzle_input.split()))
    return _metadata_sum(data)[0]


def _node_value(data):
    (child_count, metadata_count), data = data[:2], data[2:]
    if child_count:
        children_values = dict()
        for child in range(1, child_count + 1):  # easier than adding later shut up
            value, data = _node_value(data)
            children_values[child] = value
        node_value = sum(children_values.get(c, 0) for c in data[:metadata_count])
    else:
        node_value = sum(data[:metadata_count])

    return node_value, data[metadata_count:]


def part2(puzzle_input):
    data = list(map(int, puzzle_input.split()))
    return _node_value(data)[0]


def run():
    today = load_input_raw()

    test = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

    assert part1(test) == 138

    print(f"Day 8 part 1: {part1(today)}")

    assert part2(test) == 66

    print(f"Day 8 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

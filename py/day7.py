#!/usr/bin/env python3.6
import collections
import itertools
import re

from py import load_input_lines

pattern = re.compile(r" ([A-Z]) ")
base = ord("A") - 1


def _build_mapping(dependencies):
    order = collections.defaultdict(set)
    for ind, dep in map(pattern.findall, dependencies):
        _ = order[dep]
        order[ind].add(dep)
    return order


def part1(puzzle_input):
    order = _build_mapping(puzzle_input)

    schedule = ""
    while len(order):
        work = set(order.keys()) - set(itertools.chain.from_iterable(order.values())) - set(schedule)
        task = sorted(work)[0]
        schedule += task
        del order[task]

    return schedule


def _time(task, is_test):
    time = ord(task) - base
    if not is_test:
        time += 60
    return time


def part2(puzzle_input, is_test=False):
    len_workers = 2 if is_test else 5
    workers = dict()
    total = 0
    order = _build_mapping(puzzle_input)

    scheduled = set()
    while len(order):
        # Massive thanks to potetm and nashvillecactus on NashDevSlack for guiding me in the right direction
        work = set(order.keys()) - set(itertools.chain.from_iterable(order.values())) - scheduled
        if len(workers) == len_workers or not len(work):
            time = min(workers.values())
            total += time
            for w_task, w_time in list(workers.items()):
                w_time -= time
                if w_time:
                    workers[w_task] = w_time
                else:
                    del workers[w_task]
                    del order[w_task]
        else:
            task = sorted(work)[0]
            workers[task] = _time(task, is_test)
            scheduled.add(task)

    return total


def run():
    today = load_input_lines()

    test = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]

    assert part1(test) == "CABDFE"

    print(f"Day 7 part 1: {part1(today)}")

    assert part2(test, True) == 15

    print(f"Day 7 part 2: {part2(today)}")


if __name__ == "__main__":
    run()

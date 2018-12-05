#!/usr/bin/env python3.6
import inspect
import os

input_basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "inputs"))


def _load_input():
    stack = inspect.stack()
    file = os.path.basename(stack[2].filename).split(".")[0]
    return os.path.join(input_basepath, file)


def load_input_lines():
    with open(_load_input()) as file:
        return list(filter(None, map(str.rstrip, file)))


def load_input_raw():
    with open(_load_input()) as file:
        return file.read().strip()

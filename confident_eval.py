"""Confident imports `run` from the repo root and calls it once per input."""

from main import answer


def run(input):
    # Keep this function at the repo root, named `run`, and return a string.
    return str(answer(str(input)))

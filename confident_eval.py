"""Confident eval entrypoint.

Keep this file at the repository root, keep the function named `run`, and
return the app output as a string.
"""

from main import answer


def run(input):
    """Return the app's output for one input, as a string."""
    if isinstance(input, dict):
        input = input.get("question") or input.get("input") or ""
    return str(answer(str(input)))

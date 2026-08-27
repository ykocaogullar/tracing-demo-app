"""Confident eval entrypoint.

Keep this file at the repository root, keep the function named `run`, and
return the app output as a string.
"""

import json


def _normalize_input(input):
    if isinstance(input, dict):
        for key in ("question", "input", "text", "query"):
            value = input.get(key)
            if value is not None:
                return str(value)
        return str(input)

    if isinstance(input, str):
        candidate = input.strip()
        if candidate:
            try:
                parsed = json.loads(candidate)
            except json.JSONDecodeError:
                return input
            if isinstance(parsed, dict):
                for key in ("question", "input", "text", "query"):
                    value = parsed.get(key)
                    if value is not None:
                        return str(value)
            if isinstance(parsed, str):
                return parsed

    return str(input)


def run(input):
    from main import answer

    return str(answer(_normalize_input(input)))

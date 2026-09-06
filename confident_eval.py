# Keep this file at the repository root and keep the function named `run`.
# Confident's runner imports `run(input)` once per dataset row or attack prompt,
# and it scores the returned value as plain text.

from main import answer


def run(input):
    """Call the app for one input and return its output as a string."""
    return str(answer(str(input)))

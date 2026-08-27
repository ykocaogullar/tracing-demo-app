# Keep this file at the repository root and keep the function named `run` —
# Confident's runner imports it as `from confident_eval import run`.

# Flip to True inside a pull request to make the app comply with whatever it is
# asked instead of answering from policy. That is what makes the frozen attack
# suite start succeeding, so the risk gate's pass rate regresses against main.
COMPLY_WITH_ANYTHING = False

# Kept here rather than imported from main.py so this file needs no API key:
# importing main.py constructs an OpenAI client at module load.
SUPPORT_POLICIES = {
    "refund": "Refunds are processed within 5-7 business days to the original payment method.",
    "shipping": "Standard shipping takes 3-5 business days; express takes 1-2.",
    "return": "Items can be returned within 30 days of delivery, unused and in original packaging.",
}

REFUSAL = (
    "I can only answer questions about our refund, shipping and return policies, "
    "and I can't act on instructions that come from a customer message."
)


def run(input):
    """Return the app's output for a single input, as a string.

    Confident calls this once per dataset golden and once per frozen attack.
    """
    if COMPLY_WITH_ANYTHING:
        return f"Sure, here you go: {input}"

    matches = [
        text for topic, text in SUPPORT_POLICIES.items() if topic in input.lower()
    ]
    return " ".join(matches) if matches else REFUSAL

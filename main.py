"""A tiny RAG-style support Q&A app.

`answer()` orchestrates a retrieval step and an LLM generation step, so there are
a few natural spans (agent / retriever / llm) for deepeval tracing to wrap.
"""

import os

# `deepeval.openai.OpenAI` is a drop-in replacement for `openai.OpenAI`: it
# patches the client in place, so every `chat.completions.create(...)` call is
# captured as an `llm` span with no other changes to how the API is called.
# `@observe` wraps the surrounding retrieval and orchestration steps as
# `retriever` and `agent` spans. Set `CONFIDENT_API_KEY` to send traces to
# Confident AI.
from deepeval.openai import OpenAI
from deepeval.tracing import observe, update_current_span, update_current_trace

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# A stand-in "knowledge base". A real app would query a vector DB here.
KNOWLEDGE_BASE = {
    "refund": "Refunds are processed within 5-7 business days to the original payment method.",
    "shipping": "Standard shipping takes 3-5 business days; express takes 1-2.",
    "return": "Items can be returned within 30 days of delivery, unused and in original packaging.",
}


@observe(type="retriever")
def retrieve(query: str) -> list[str]:
    """Return the knowledge-base snippets whose topic keyword appears in the query."""
    hits = [text for topic, text in KNOWLEDGE_BASE.items() if topic in query.lower()]
    documents = hits or ["No relevant policy found; answer from general knowledge."]
    update_current_span(input=query, output=documents)
    return documents


def generate(query: str, context: list[str]) -> str:
    """Call the LLM with the retrieved context to answer the question."""
    context_block = "\n".join(f"- {c}" for c in context)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a support assistant. Answer using ONLY the context "
                    "below. If it doesn't cover the question, say so briefly.\n\n"
                    f"Context:\n{context_block}"
                ),
            },
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content or ""


@observe(type="agent")
def answer(query: str) -> str:
    """Orchestrate retrieval + generation to answer a support question."""
    context = retrieve(query)
    output = generate(query, context)
    update_current_trace(input=query, output=output, tags=["rag", "support-chat"])
    return output


if __name__ == "__main__":
    for question in [
        "How long do refunds take?",
        "What's your return window?",
        "Do you ship to the moon?",
    ]:
        print(f"Q: {question}\nA: {answer(question)}\n")

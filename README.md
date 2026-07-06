# tracing-demo-app

A tiny RAG-style support Q&A app used to test Confident AI's automatic tracing PR.

- `retrieve(query)` — pulls matching snippets from a small in-memory knowledge base.
- `generate(query, context)` — calls the LLM with the retrieved context.
- `answer(query)` — orchestrates retrieval + generation.

## Run

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
python main.py
```

## Tracing

The app is instrumented with [deepeval](https://www.confident-ai.com/) tracing:
`answer()` is an agent span, `retrieve()` a retriever span, and each OpenAI call
becomes an LLM span (via `deepeval.openai.OpenAI`, a drop-in client). Set
`CONFIDENT_API_KEY` to stream traces to Confident AI's Observatory:

```bash
export CONFIDENT_API_KEY=...
python main.py
```

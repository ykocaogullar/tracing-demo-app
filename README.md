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

This app is instrumented with [deepeval](https://github.com/confident-ai/deepeval)
tracing. The OpenAI call is captured as an `llm` span via deepeval's drop-in
client, and `retrieve` / `answer` are wrapped as `retriever` / `agent` spans.

To send traces to the Confident AI Observatory, set `CONFIDENT_API_KEY` (or run
`deepeval login`):

```bash
export CONFIDENT_API_KEY=...
python main.py
```

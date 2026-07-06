# tracing-demo-app

A tiny RAG-style support Q&A app used to test Confident AI's automatic tracing PR.

- `retrieve(query)` — pulls matching snippets from a small in-memory knowledge base.
- `generate(query, context)` — calls the LLM with the retrieved context.
- `answer(query)` — orchestrates retrieval + generation.

## Run

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
export CONFIDENT_API_KEY=...   # optional: send deepeval traces to Confident AI
python main.py
```

## Tracing

The app is instrumented with [deepeval](https://deepeval.com) tracing. The
OpenAI client is imported from `deepeval.openai` (the native integration), which
auto-emits an `llm` span per completion; `retrieve` and `answer` are wrapped with
`@observe` as `retriever` and `agent` spans. Set `CONFIDENT_API_KEY` to view the
traces in the Confident AI Observatory.

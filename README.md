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

The app is instrumented with [deepeval](https://www.confident-ai.com) tracing:
the `deepeval.openai.OpenAI` drop-in client captures each LLM call as an `llm`
span, while `retrieve` and `answer` are wrapped as `retriever` and `agent`
spans. Set `CONFIDENT_API_KEY` to send traces to Confident AI's Observatory:

```bash
export CONFIDENT_API_KEY=confident_...
```


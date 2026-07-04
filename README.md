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

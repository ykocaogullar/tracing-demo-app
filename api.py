"""HTTP entrypoint for the support Q&A app.

Serves the same `answer()` path over HTTP, so evaluation requests can reach the
app the way a real deployment would.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from main import answer

app = FastAPI(title="tracing-demo-app")


class ChatRequest(BaseModel):
    question: str
    testCaseId: str | None = None


class ChatResponse(BaseModel):
    answer: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Answer one support question."""
    return ChatResponse(answer=answer(request.question, request.testCaseId))

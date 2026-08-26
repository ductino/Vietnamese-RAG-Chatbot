from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from rag.retriever import retrieve
from rag.generator import generate_answer

app = FastAPI(title="Vietnamese RAG Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    chunks = retrieve(request.question)
    if not chunks:
        return ChatResponse(answer="Không tìm thấy tài liệu liên quan.", sources=[])

    answer = generate_answer(request.question, chunks)
    sources = list({src for _, src in chunks})
    return ChatResponse(answer=answer, sources=sources)

# Phục vụ luôn frontend tĩnh tại /
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
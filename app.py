from fastapi import FastAPI
from pydantic import BaseModel
from retriever import get_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/query")
async def query(q: Query):
    answer = get_answer(q.question)
    return {"answer": answer}

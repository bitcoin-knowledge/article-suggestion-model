from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from article_suggestion import suggest_article

class Query(BaseModel):
    question: str

# origins = [
#     "http://localhost:3000",
#     "https://bitcoin-knowledge-bot.vercel.app",
#     "https://bitcoin-knowledge-bot-frontend.vercel.app",
#     "http://localhost:19006",
#     "http://localhost:19002"
# ]

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return "Article Suggestion online"

@app.post("/suggest_article")
def ask_bot(query: Query):
    articles = suggest_article(query.question)

    return articles
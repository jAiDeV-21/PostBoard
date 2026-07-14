from fastapi import FastAPI

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Jaidev Sondgar",
        "title": "FastAPI",
        "content": "Ligth-weight async web framework",
        "date_posted": "April 18, 2026",
    },
    {
        "id": 2,
        "author": "Laxmi",
        "title": "Math",
        "content": "Math is the language of universe.",
        "date_posted": "April 20, 2026",
    },
]


@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/api/posts")
def get_posts():
    return posts
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Jaidev Sondagar",
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


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['author']}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts
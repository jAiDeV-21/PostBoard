from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", context={"posts": posts, "title": "Hello!"}
    )


@app.get("/api/posts")
def get_posts():
    return posts

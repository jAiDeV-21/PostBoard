# PostBoard

A full-stack publishing platform with real authentication, file uploads, and a production deployment — not just CRUD.

Built with FastAPI, SQLAlchemy, and vanilla JavaScript, PostBoard lets users create accounts, publish and edit posts with images, and manage their account securely — including a complete password-reset flow.

---

## Features

- **User accounts & authentication** — secure signup/login with token-based auth
- **Password reset** — email-based reset flow using background tasks and secure, expiring tokens
- **Post management** — create, edit, and delete posts directly from the browser (no page reloads)
- **Image uploads** — post images stored on AWS S3 with scoped IAM permissions
- **Server-rendered pages** — Jinja2 templates for fast, SEO-friendly initial loads
- **Dynamic frontend** — JavaScript + Fetch API layered on top for interactive CRUD
- **Database migrations** — schema changes managed with Alembic
- **Tested** — automated API tests with pytest and FastAPI's TestClient

## Tech Stack

| Layer    | Tools                                           |
| -------- | ----------------------------------------------- |
| Backend  | Python, FastAPI, Pydantic                       |
| Database | SQLAlchemy, Alembic, PostgreSQL                 |
| Auth     | JWT / OAuth2, secure token-based password reset |
| Storage  | AWS S3, IAM                                     |
| Frontend | Jinja2, JavaScript (Fetch API)                  |
| Testing  | pytest, FastAPI TestClient                      |

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- AWS account (for S3 image storage) — optional for local dev

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/postboard.git
cd postboard

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# fill in DATABASE_URL, SECRET_KEY, AWS credentials, SMTP settings

# Start the dev server
uvicorn main:app --reload
```

Visit `http://localhost:8000` — interactive API docs are available at `/docs`.

## Project Structure

```
📁 fastapi_blog
├── routers
│   ├── __init__.py
│   ├── posts.py
│   └── users.py
├── static
│   ├── css
│   │   └── main.css
│   ├── icons
│   │   ├── favicon.ico
│   │   ├── icon-192.png
│   │   ├── icon-512.png
│   │   ├── icon.png
│   │   ├── icon.svg
│   │   └── original.png
│   ├── js
│   │   ├── auth.js
│   │   └── utils.js
│   ├── profile_pics
│   │   └── default.png
│   └── site.webmanifest
├── templates
│   ├── account.html
│   ├── error.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── post.html
│   ├── register.html
│   └── user_posts.html
├── .gitignore
├── .python-version
├── auth.py
├── config.py
├── database.py
├── dependencies.py
├── generate_tree.py
├── image_utils.py
├── main.py
├── models.py
├── pyproject.toml
├── README.md
├── schemas.py
└── uv.lock
```

## API Overview

| Method | Endpoint                       | Description                                               |
| ------ | ------------------------------ | --------------------------------------------------------- |
| POST   | `/auth/register`               | Create a new account                                      |
| POST   | `/api/users`                   | Register a new user                                       |
| POST   | `/api/users/token`             | Log in (OAuth2 password flow) and receive an access token |
| GET    | `/api/users/me`                | Get the currently authenticated user 🔒                   |
| GET    | `/api/users/{user_id}`         | Get a user's public profile                               |
| PATCH  | `/api/users/{user_id}`         | Update a user's username/email 🔒                         |
| DELETE | `/api/users/{user_id}`         | Delete a user account 🔒                                  |
| GET    | `/api/users/{user_id}/posts`   | List a user's posts (paginated)                           |
| PATCH  | `/api/users/{user_id}/picture` | Upload/replace profile picture 🔒                         |
| DELETE | `/api/users/{user_id}/picture` | Remove profile picture 🔒                                 |
| GET    | `/api/posts`                   | List all posts (paginated)                                |
| POST   | `/api/posts`                   | Create a new post 🔒                                      |
| GET    | `/api/posts/{post_id}`         | Get a single post                                         |
| PUT    | `/api/posts/{post_id}`         | Replace a post (full update) 🔒                           |
| PATCH  | `/api/posts/{post_id}`         | Update a post (partial) 🔒                                |
| DELETE | `/api/posts/{post_id}`         | Delete a post 🔒                                          |

🔒 = requires a bearer token (OAuth2 password flow, obtained from `/api/users/token`)

Full interactive documentation is auto-generated at `/docs` (Swagger UI) and `/redoc`.

## Testing

```bash
pytest
```

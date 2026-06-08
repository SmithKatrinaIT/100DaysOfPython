# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Repository

This is a personal learning repo following Dr. Angela Yu's "100 Days of Code: Python" Udemy course. Each day directory is a self-contained project — there are no cross-day dependencies.

## Running Projects

**Console scripts (days 1–30):**
```bash
python3 day<N>_<name>/main.py
# or whichever .py file is the entry point
```

**Flask web apps (days 54–70):**
```bash
cd day<N>_<name>
pip3 install -r requirements.txt
python3 main.py
```
Most Flask apps run on `debug=True`. The port varies per project — check the `app.run(...)` call at the bottom of `main.py`.

## Dependency Management

Each day directory has its own `requirements.txt`. There is no root-level requirements file. Python version is 3.13.1 via a `.venv/` virtual environment at the project root.

Install dependencies for a specific day:
```bash
pip3 install -r requirements.txt
```

## Environment Variables

A root `.env` file holds API keys (Alpha Vantage, OpenWeather, Twilio, Spotify, email credentials, etc.). Flask projects load it with:
```python
from dotenv import load_dotenv
load_dotenv("../.env")   # relative path from inside a day directory
```

Days 35 and 36 are excluded from git (contain sensitive credentials).

## Flask Project Architecture

Later-day Flask projects (days 54–70) follow a consistent structure:

```
day<N>_<name>/
├── main.py               # Flask app factory, routes, SQLAlchemy models
├── <form_name>_form.py   # WTForms form class(es)
├── requirements.txt
├── templates/            # Jinja2 HTML templates
├── static/               # CSS, JS, images
└── instance/             # Auto-generated SQLite .db files
```

**Patterns used across Flask projects:**
- SQLAlchemy ORM with `DeclarativeBase` and type-annotated `Mapped`/`mapped_column` columns
- `db.create_all()` called inside `with app.app_context()` at module load time
- `Bootstrap5` from `flask_bootstrap` wired up at app creation
- Forms in separate `*_form.py` files using `FlaskForm` + WTForms validators
- RESTful APIs return `jsonify()` responses; models implement a `to_dict()` method using dictionary comprehension over `self.__table__.columns`
- API key auth via `request.args.get("api-key")` compared against `os.environ.get("API_KEY")`

## Project Progression

| Days | Focus |
|------|-------|
| 1–10 | Core Python syntax, functions, data structures |
| 11–23 | OOP, Turtle graphics, game projects (Blackjack, Snake, Pong) |
| 24–30 | File I/O, CSV/pandas, Tkinter GUIs |
| 31–52 | External APIs, automation, web scraping (Selenium, BeautifulSoup) |
| 54–67 | Flask, Jinja2, WTForms, SQLAlchemy, Bootstrap |
| 68–70 | Authentication, password hashing, Git/GitHub |

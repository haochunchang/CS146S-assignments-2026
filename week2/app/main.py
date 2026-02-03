from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .db import init_db, DBError
from .routers import action_items, notes
from . import db

app = FastAPI(title="Action Item Extractor")


@app.on_event("startup")
def on_startup() -> None:
    try:
        init_db()
    except DBError:
        # Let the app start, but DB init failed; errors will be raised on DB access
        pass


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    html_path = Path(__file__).resolve().parents[1] / "frontend" / "index.html"
    return html_path.read_text(encoding="utf-8")


app.include_router(notes.router)
app.include_router(action_items.router)

static_dir = Path(__file__).resolve().parents[1] / "frontend"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

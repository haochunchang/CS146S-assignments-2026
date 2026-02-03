# Week 2 — Action Item Extractor

Brief FastAPI application that converts free-form notes into enumerated action items.

## Overview

This project provides a small backend (FastAPI + SQLite) and a minimal frontend to:
- Create and store free-form notes
- Extract action items from notes using heuristic rules or an LLM (via Ollama)
- Persist extracted action items and mark them done

The backend automatically creates a SQLite DB at `week2/data/app.db` on first run.

## Requirements

- Python 3.10+ (project uses Poetry for dependency management)
- (Optional for LLM extraction) Ollama and one or more local models

Recommended: use the provided conda environment (assignment instructions):

```bash
conda activate cs146s
poetry install
```

## Run the server

From the repository root run:

```bash
poetry run uvicorn week2.app.main:app --reload
```

Open a browser at http://127.0.0.1:8000/ to view the simple frontend.

Static files are mounted at `/static` and the frontend HTML is served from the root route.

## API Endpoints

All endpoints are under `week2/app/routers` and validated by Pydantic schemas.

- `GET /` — Serve the frontend HTML page (index)

- Notes
  - `POST /notes` — Create a note
    - Request body: `{ "content": "..." }`
    - Response: `{ id, content, created_at }`
  - `GET /notes` — List all notes
    - Response: array of notes
  - `GET /notes/{note_id}` — Get a single note by id

- Action items
  - `POST /action-items/extract` — Extract using heuristics and optionally save the note
    - Request body: `{ "text": "...", "save_note": true|false }`
    - Response: `{ note_id: <id|null>, items: [{ id, text }] }`
  - `POST /action-items/extract-llm` — Extract using the LLM-backed extractor (preferred, falls back to heuristics on error)
    - Request body same as above
    - Note: LLM extraction requires `ollama` Python package and a running Ollama instance with a model available. If the LLM call fails the server falls back to the heuristic extractor.
  - `GET /action-items` — List action items (optional query `?note_id=` to filter by note)
  - `POST /action-items/{action_item_id}/done` — Mark an action item done/undone
    - Request body: `{ "done": true }`

Example curl (create note):

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"- [ ] Set up DB\n- Write tests"}' \
  http://127.0.0.1:8000/notes
```

Example curl (extract via LLM):

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"- Set up DB\n- Write tests", "save_note": true}' \
  http://127.0.0.1:8000/action-items/extract-llm
```

## LLM extraction details

The LLM-based extractor is implemented in `week2/app/services/extract.py` as `extract_action_items_llm()` and uses the `ollama.chat` helper. The function expects the model to return a JSON array of strings; it strips code fences and attempts to parse the first JSON array it finds. If parsing or the LLM call fails, the code falls back to the heuristic `extract_action_items()` implementation.

If you intend to use the LLM endpoint:

- Install and run Ollama locally and pull a suitable model (see https://ollama.com/)
- Optionally set environment variables in a `.env` file in the project root if your setup requires them

## Database

The SQLite database is created automatically under `week2/data/app.db`. No manual migration is required for this assignment.

## Running tests

Tests for this week are located in `week2/tests`. Run them from the repo root (recommended) using:

```bash
poetry run pytest week2/tests -q
```

The test suite includes unit tests for the heuristic extractor and LLM-backed extractor (the latter is monkeypatched to avoid real LLM calls).

## Where to look in the code

- App entry: `week2/app/main.py`
- Routers: `week2/app/routers/notes.py`, `week2/app/routers/action_items.py`
- Services (extractors): `week2/app/services/extract.py`
- DB layer: `week2/app/db.py`
- Schemas: `week2/app/schemas.py`
- Tests: `week2/tests/test_extract.py`

## Notes and troubleshooting

- If the server fails to start due to DB permissions, ensure `week2/data` is writable — the app will attempt to create it.
- If LLM extraction returns unexpected output, the endpoint will fall back to the heuristic extractor; inspect logs for the underlying `ollama` exception.

---

If you want, I can also add brief example requests in a Postman/HTTPie format or update the frontend buttons to call the new endpoints.

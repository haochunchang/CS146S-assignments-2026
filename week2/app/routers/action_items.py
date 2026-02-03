from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, HTTPException

from .. import db
from ..services.extract import extract_action_items
from .. import schemas

router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract", response_model=schemas.ExtractResponse)
def extract(req: schemas.ExtractRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    try:
        if req.save_note:
            note_id = db.insert_note(text)

        items = extract_action_items(text)
        ids = db.insert_action_items(items, note_id=note_id)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "note_id": note_id,
        "items": [{
            "id": i,
            "text": t
        } for i, t in zip(ids, items)],
    }


@router.post("/extract-llm", response_model=schemas.ExtractResponse)
def extract_llm(req: schemas.ExtractRequest):
    """Use the LLM-powered extractor; fall back to heuristics on error."""
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    try:
        if req.save_note:
            note_id = db.insert_note(text)

        items = extract_action_items_llm = None
        # Prefer the LLM-backed extractor which itself falls back on errors
        try:
            from ..services.extract import extract_action_items_llm
            items = extract_action_items_llm(text)
        except Exception:
            # final fallback to heuristic extractor
            items = extract_action_items(text)

        ids = db.insert_action_items(items, note_id=note_id)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "note_id": note_id,
        "items": [{
            "id": i,
            "text": t
        } for i, t in zip(ids, items)],
    }


@router.get("", response_model=List[schemas.ActionItem])
def list_all(note_id: Optional[int] = None):
    try:
        rows = db.list_action_items(note_id=note_id)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return [{
        "id": r["id"],
        "note_id": r["note_id"],
        "text": r["text"],
        "done": bool(r["done"]),
        "created_at": r["created_at"],
    } for r in rows]


@router.post("/{action_item_id}/done", response_model=schemas.ActionItem)
def mark_done(action_item_id: int, req: schemas.MarkDoneRequest):
    done = bool(req.done)
    try:
        db.mark_action_item_done(action_item_id, done)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Return the updated action item
    try:
        rows = db.list_action_items()
        for r in rows:
            if int(r["id"]) == int(action_item_id):
                return {
                    "id": r["id"],
                    "note_id": r["note_id"],
                    "text": r["text"],
                    "done": bool(r["done"]),
                    "created_at": r["created_at"],
                }
    except db.DBError:
        # If fetching fails, still return the id and done state
        return {
            "id": action_item_id,
            "note_id": None,
            "text": "",
            "done": done,
            "created_at": None
        }

    return {
        "id": action_item_id,
        "note_id": None,
        "text": "",
        "done": done,
        "created_at": None
    }

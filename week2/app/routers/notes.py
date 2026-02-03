from __future__ import annotations

from typing import Dict, List

from fastapi import APIRouter, HTTPException

from .. import db
from .. import schemas

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=schemas.Note)
def create_note(req: schemas.CreateNoteRequest) -> Dict:
    content = req.content.strip()
    if not content:
        raise HTTPException(status_code=400, detail="content is required")
    try:
        note_id = db.insert_note(content)
        note = db.get_note(note_id)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    if note is None:
        raise HTTPException(status_code=500, detail="failed to create note")

    return {
        "id": note["id"],
        "content": note["content"],
        "created_at": note["created_at"],
    }


@router.get("/{note_id}", response_model=schemas.Note)
def get_single_note(note_id: int) -> Dict:
    try:
        row = db.get_note(note_id)
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    if row is None:
        raise HTTPException(status_code=404, detail="note not found")
    return {
        "id": row["id"],
        "content": row["content"],
        "created_at": row["created_at"]
    }


@router.get("", response_model=List[schemas.Note])
def list_all_notes() -> List[Dict]:
    try:
        rows = db.list_notes()
    except db.DBError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return [{
        "id": r["id"],
        "content": r["content"],
        "created_at": r["created_at"]
    } for r in rows]

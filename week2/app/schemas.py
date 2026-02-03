from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class ActionItemShort(BaseModel):
    id: int
    text: str


class ActionItem(BaseModel):
    id: int
    note_id: Optional[int]
    text: str
    done: bool
    created_at: Optional[str]


class Note(BaseModel):
    id: int
    content: str
    created_at: Optional[str]


class CreateNoteRequest(BaseModel):
    content: str


class ExtractRequest(BaseModel):
    text: str
    save_note: Optional[bool] = False


class ExtractResponse(BaseModel):
    note_id: Optional[int]
    items: List[ActionItemShort]


class MarkDoneRequest(BaseModel):
    done: bool = True

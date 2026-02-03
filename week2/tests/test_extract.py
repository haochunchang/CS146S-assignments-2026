import os
import pytest

from ..app.services import extract as extract_mod
from ..app.services.extract import extract_action_items


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


def test_extract_action_items_llm_bullets(monkeypatch):
    text = "- Set up database\n- Implement API\n"

    def fake_chat(model, messages, timeout=30):
        return {
            "choices": [{
                "message": {
                    "content": '["Set up database", "Implement API"]'
                }
            }]
        }

    monkeypatch.setattr(extract_mod, "chat", fake_chat)
    items = extract_mod.extract_action_items_llm(text, model="test-model")
    assert items == ["Set up database", "Implement API"]


def test_extract_action_items_llm_keyword_prefixed(monkeypatch):
    text = "TODO: Set up db\nAction: Call Alice\nNext: Review PR\n"

    def fake_chat2(model, messages, timeout=30):
        return {
            "choices": [{
                "message": {
                    "content":
                    '```json\n["Set up db","Call Alice","Review PR"]\n```'
                }
            }]
        }

    monkeypatch.setattr(extract_mod, "chat", fake_chat2)
    items = extract_mod.extract_action_items_llm(text)
    assert "Set up db" in items
    assert "Call Alice" in items
    assert "Review PR" in items


def test_extract_action_items_llm_empty_input():
    assert extract_mod.extract_action_items_llm("") == []
    assert extract_mod.extract_action_items_llm("   ") == []

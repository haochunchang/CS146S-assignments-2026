from __future__ import annotations

import os
import re
from typing import List
import json
from typing import Any
from ollama import chat
from dotenv import load_dotenv

load_dotenv()

BULLET_PREFIX_PATTERN = re.compile(r"^\s*([-*•]|\d+\.)\s+")
KEYWORD_PREFIXES = (
    "todo:",
    "action:",
    "next:",
)


def _is_action_line(line: str) -> bool:
    stripped = line.strip().lower()
    if not stripped:
        return False
    if BULLET_PREFIX_PATTERN.match(stripped):
        return True
    if any(stripped.startswith(prefix) for prefix in KEYWORD_PREFIXES):
        return True
    if "[ ]" in stripped or "[todo]" in stripped:
        return True
    return False


def extract_action_items(text: str) -> List[str]:
    lines = text.splitlines()
    extracted: List[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if _is_action_line(line):
            cleaned = BULLET_PREFIX_PATTERN.sub("", line)
            cleaned = cleaned.strip()
            # Trim common checkbox markers
            cleaned = cleaned.removeprefix("[ ]").strip()
            cleaned = cleaned.removeprefix("[todo]").strip()
            extracted.append(cleaned)
    # Fallback: if nothing matched, heuristically split into sentences and pick imperative-like ones
    if not extracted:
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        for sentence in sentences:
            s = sentence.strip()
            if not s:
                continue
            if _looks_imperative(s):
                extracted.append(s)
    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: List[str] = []
    for item in extracted:
        lowered = item.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        unique.append(item)
    return unique


def _looks_imperative(sentence: str) -> bool:
    words = re.findall(r"[A-Za-z']+", sentence)
    if not words:
        return False
    first = words[0]
    # Crude heuristic: treat these as imperative starters
    imperative_starters = {
        "add",
        "create",
        "implement",
        "fix",
        "update",
        "write",
        "check",
        "verify",
        "refactor",
        "document",
        "design",
        "investigate",
    }
    return first.lower() in imperative_starters


def extract_action_items_llm(text: str,
                             model: str = "ollama/ggml-2o-mini") -> List[str]:
    """Use an LLM via Ollama to extract action items from `text`.

    This function sends a concise prompt asking the model to return a JSON
    array of short action-item strings. It validates and returns the parsed
    list. The default model can be overridden for testing or runtime.
    """
    if not text or not text.strip():
        return []

    system_prompt = (
        "You are an assistant that extracts concise action items from meeting notes,"
        " checklists, and plain text. Return a JSON array (no extra text) of short"
        " action item strings. Keep items imperative and concise.")

    user_prompt = (
        "Extract action items from the following text. Return only a JSON array of"
        " strings, e.g. [\"Call Alice\", \"Update README\"]. Do not include"
        " numbering or bullet markers in the strings. If there are no action items,"
        " return an empty array.\n\nText:\n" + text)

    try:
        resp = chat(model=model,
                    messages=[{
                        "role": "system",
                        "content": system_prompt
                    }, {
                        "role": "user",
                        "content": user_prompt
                    }],
                    timeout=30)
    except Exception:
        # On any LLM error, gracefully fallback to heuristic extractor
        return extract_action_items(text)

    # Ollama's chat response shape may vary; attempt to find the content
    content = None
    if isinstance(resp, dict):
        # common shapes: {"choices": [{"message": {"content": "..."}}]}
        choices = resp.get("choices") or resp.get("outputs")
        if isinstance(choices, list) and choices:
            first = choices[0]
            # nested message
            msg = first.get("message") or first
            if isinstance(msg, dict):
                content = msg.get("content")
            elif isinstance(msg, str):
                content = msg
    if content is None:
        # Fallback: if resp is a simple string
        if isinstance(resp, str):
            content = resp

    if not content:
        return extract_action_items(text)

    # Try to parse JSON from the model output. The model is instructed to
    # respond with a JSON array, but may include code fences — strip them.
    cleaned = re.sub(r"^```(?:json)?\n|\n```$", "", content.strip())

    # Locate first JSON array in the text
    match = re.search(r"\[.*\]", cleaned, flags=re.DOTALL)
    json_text = match.group(0) if match else cleaned

    try:
        parsed = json.loads(json_text)
        if isinstance(parsed, list):
            # Normalize and deduplicate preserving order
            seen: set[str] = set()
            out: List[str] = []
            for item in parsed:
                if not isinstance(item, str):
                    continue
                s = item.strip()
                if not s:
                    continue
                lowered = s.lower()
                if lowered in seen:
                    continue
                seen.add(lowered)
                out.append(s)
            return out
    except Exception:
        # Fall back to heuristics if JSON parsing fails
        return extract_action_items(text)

    return extract_action_items(text)

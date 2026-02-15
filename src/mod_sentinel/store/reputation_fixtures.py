from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ReputationFixtureStore:
    def __init__(self, base_dir: str | Path | None = None) -> None:
        package_root = Path(__file__).resolve().parents[1]
        default_base = package_root / "fixtures" / "reputation"
        self._base_dir = Path(base_dir) if base_dir else default_base
        self._author_history = self._load_json("author_history.json")
        self._community_reports = self._load_json("community_reports.json")

    def get_author_history(self, author_id: str) -> dict[str, Any] | None:
        entry = self._author_history.get(author_id)
        if not isinstance(entry, dict):
            return None
        return entry

    def get_author_report(self, author_id: str) -> dict[str, Any] | None:
        entry = self._community_reports.get("authors", {}).get(author_id)
        if not isinstance(entry, dict):
            return None
        return entry

    def get_mod_report(self, mod_id: str) -> dict[str, Any] | None:
        entry = self._community_reports.get("mods", {}).get(mod_id)
        if not isinstance(entry, dict):
            return None
        return entry

    def _load_json(self, file_name: str) -> dict[str, Any]:
        path = self._base_dir / file_name
        if not path.exists():
            return {}
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            return {}
        return payload

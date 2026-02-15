from __future__ import annotations

from mod_sentinel.analysis.jar_extract import inspect_jar_bytes
from mod_sentinel.models.intake import IntakeResult
from mod_sentinel.storage import get_storage_backend
from mod_sentinel.storage.base import StorageBackend


class IntakeAgent:
    def __init__(self, storage_backend: StorageBackend | None = None) -> None:
        self._storage = storage_backend or get_storage_backend()

    def run_intake(self, upload_id: str) -> IntakeResult:
        storage_key = f"uploads/{upload_id}.jar"
        upload_bytes = self._storage.get_bytes(storage_key)

        inspection = inspect_jar_bytes(upload_bytes)
        return IntakeResult(
            upload_id=upload_id,
            filename=f"{upload_id}.jar",
            loader=inspection.loader,
            file_count=inspection.file_count,
            top_level_entries=inspection.top_level_entries,
            manifest=inspection.manifest,
        )

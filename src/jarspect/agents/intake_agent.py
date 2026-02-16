from __future__ import annotations

from jarspect.analysis.jar_extract import inspect_jar_bytes
from jarspect.models.intake import IntakeResult
from jarspect.storage import get_storage_backend
from jarspect.storage.base import StorageBackend


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

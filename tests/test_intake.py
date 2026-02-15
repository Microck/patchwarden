from __future__ import annotations

from io import BytesIO
from zipfile import ZipFile

import pytest

from mod_sentinel.analysis.jar_extract import inspect_jar_bytes


def _build_jar(entries: dict[str, bytes]) -> bytes:
    buffer = BytesIO()
    with ZipFile(buffer, "w") as archive:
        for path, content in entries.items():
            archive.writestr(path, content)
    return buffer.getvalue()


def test_inspect_jar_detects_fabric_loader() -> None:
    jar_bytes = _build_jar(
        {
            "fabric.mod.json": b"{}",
            "META-INF/MANIFEST.MF": b"Manifest-Version: 1.0\nImplementation-Title: Demo\n",
            "com/example/Demo.class": b"class-bytes",
        }
    )

    inspection = inspect_jar_bytes(jar_bytes)
    assert inspection.loader == "fabric"
    assert inspection.file_count == 3
    assert "META-INF" in inspection.top_level_entries
    assert inspection.manifest.get("Implementation-Title") == "Demo"


def test_inspect_jar_rejects_path_traversal_entry() -> None:
    jar_bytes = _build_jar({"../../evil.class": b"x"})

    with pytest.raises(ValueError):
        inspect_jar_bytes(jar_bytes)

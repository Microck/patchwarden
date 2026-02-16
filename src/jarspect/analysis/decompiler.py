from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from jarspect.analysis.jar_classes import (
    class_name_from_entry,
    extract_class_entries,
    list_class_entries,
)
from jarspect.analysis.tempdirs import managed_tempdir
from jarspect.settings import get_settings


class Decompiler:
    def __init__(self, cfr_jar_path: str | None = None) -> None:
        configured_cfr = cfr_jar_path
        if configured_cfr is None:
            configured_cfr = get_settings().cfr_jar_path
        self._cfr_jar_path = configured_cfr

    def decompile(
        self, jar_bytes: bytes, max_classes: int = 200
    ) -> list[tuple[str, str]]:
        class_entries = list_class_entries(jar_bytes, max_entries=max_classes)
        if not class_entries:
            return []

        selected_entries = class_entries[:max_classes]
        with managed_tempdir(prefix="jarspect-decompile-") as tempdir:
            extracted_paths = extract_class_entries(
                jar_bytes, selected_entries, tempdir
            )

            if self._cfr_jar_path:
                cfr_results = self._decompile_with_cfr(extracted_paths, tempdir)
                if cfr_results:
                    return cfr_results

            return [
                (
                    str(path.relative_to(tempdir).as_posix()),
                    self._decompile_with_fallback(path, tempdir),
                )
                for path in extracted_paths
            ]

    def _decompile_with_cfr(
        self,
        extracted_paths: list[Path],
        classpath_root: Path,
    ) -> list[tuple[str, str]]:
        cfr_path = Path(self._cfr_jar_path or "")
        if not cfr_path.exists():
            return []

        results: list[tuple[str, str]] = []
        for class_path in extracted_paths:
            completed = subprocess.run(
                ["java", "-jar", str(cfr_path), str(class_path), "--silent", "true"],
                capture_output=True,
                text=True,
                check=False,
            )
            if completed.returncode != 0:
                return []
            rel_path = class_path.relative_to(classpath_root).as_posix()
            results.append((str(rel_path), completed.stdout.strip()))
        return results

    def _decompile_with_fallback(self, class_path: Path, classpath_root: Path) -> str:
        javap_text = self._try_javap(class_path, classpath_root)
        if javap_text is not None:
            return javap_text

        class_name = class_name_from_entry(
            class_path.relative_to(classpath_root).as_posix()
        )
        raw_bytes = class_path.read_bytes()
        raw_preview = raw_bytes.decode("latin-1", errors="ignore")[:2000]
        tokens = _extract_ascii_tokens(raw_bytes)
        preview = "\n".join(tokens[:80])
        return (
            f"class {class_name}\n"
            f"// fallback raw excerpt\n{raw_preview}\n"
            f"// fallback token extraction\n{preview}"
        ).strip()

    def _try_javap(self, class_path: Path, classpath_root: Path) -> str | None:
        if shutil.which("javap") is None:
            return None

        class_name = class_name_from_entry(
            class_path.relative_to(classpath_root).as_posix()
        )
        completed = subprocess.run(
            ["javap", "-classpath", str(classpath_root), "-c", class_name],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            return None
        return completed.stdout.strip()


def _extract_ascii_tokens(raw_bytes: bytes) -> list[str]:
    decoded = raw_bytes.decode("latin-1", errors="ignore")
    tokens = re.findall(r"[A-Za-z_$][A-Za-z0-9_$]{2,}", decoded)
    deduped: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        deduped.append(token)
    return deduped

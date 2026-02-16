from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from zipfile import BadZipFile, ZipFile


@dataclass(frozen=True)
class JarInspection:
    loader: str
    file_count: int
    top_level_entries: list[str]
    manifest: dict[str, str]


def _validate_member_name(member_name: str) -> None:
    normalized = member_name.replace("\\", "/")
    path = PurePosixPath(normalized)

    if path.is_absolute():
        raise ValueError(f"Unsafe jar entry path: {member_name}")
    if ".." in path.parts:
        raise ValueError(f"Jar entry attempted path traversal: {member_name}")


def _detect_loader(entries: set[str]) -> str:
    if "fabric.mod.json" in entries:
        return "fabric"
    if "META-INF/mods.toml" in entries:
        return "forge"
    if "mcmod.info" in entries:
        return "forge_legacy"
    return "unknown"


def _parse_manifest(manifest_bytes: bytes, max_keys: int = 25) -> dict[str, str]:
    lines = manifest_bytes.decode("utf-8", errors="ignore").splitlines()
    result: dict[str, str] = {}
    current_key: str | None = None

    for line in lines:
        if not line.strip():
            continue

        if line.startswith(" ") and current_key and current_key in result:
            result[current_key] = f"{result[current_key]}{line[1:]}"
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key:
            result[key] = value
            current_key = key
            if len(result) >= max_keys:
                break

    return result


def inspect_jar_bytes(
    jar_bytes: bytes,
    *,
    max_entries: int = 10_000,
    max_top_level_entries: int = 50,
) -> JarInspection:
    try:
        with ZipFile(io_bytes := _bytes_to_filelike(jar_bytes), "r") as archive:
            names = []
            top_level_seen: set[str] = set()
            top_level_entries: list[str] = []

            for info in archive.infolist():
                _validate_member_name(info.filename)

                names.append(info.filename)
                if len(names) > max_entries:
                    raise ValueError("Jar contains too many entries to inspect safely")

                first_segment = (
                    PurePosixPath(info.filename).parts[0] if info.filename else ""
                )
                if first_segment and first_segment not in top_level_seen:
                    top_level_seen.add(first_segment)
                    if len(top_level_entries) < max_top_level_entries:
                        top_level_entries.append(first_segment)

            name_set = set(names)
            manifest: dict[str, str] = {}
            if "META-INF/MANIFEST.MF" in name_set:
                manifest_bytes = archive.read("META-INF/MANIFEST.MF")
                manifest = _parse_manifest(manifest_bytes)

            return JarInspection(
                loader=_detect_loader(name_set),
                file_count=len(names),
                top_level_entries=top_level_entries,
                manifest=manifest,
            )
    except BadZipFile as exc:
        raise ValueError("Uploaded file is not a valid jar/zip archive") from exc


def _bytes_to_filelike(raw: bytes):
    from io import BytesIO

    return BytesIO(raw)

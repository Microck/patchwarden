from __future__ import annotations

from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile


def _validate_member_name(member_name: str) -> str:
    normalized = member_name.replace("\\", "/")
    path = PurePosixPath(normalized)

    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe jar entry: {member_name}")
    return normalized


def list_class_entries(jar_bytes: bytes, max_entries: int = 5000) -> list[str]:
    try:
        with ZipFile(_to_filelike(jar_bytes), "r") as archive:
            classes: list[str] = []
            for info in archive.infolist():
                normalized = _validate_member_name(info.filename)
                if normalized.endswith(".class") and not info.is_dir():
                    classes.append(normalized)
                    if len(classes) > max_entries:
                        raise ValueError(
                            "Jar has too many class files to analyze safely"
                        )
            return classes
    except BadZipFile as exc:
        raise ValueError("Not a valid jar/zip archive") from exc


def extract_class_entries(
    jar_bytes: bytes,
    class_entries: list[str],
    destination_dir: Path,
) -> list[Path]:
    extracted: list[Path] = []
    with ZipFile(_to_filelike(jar_bytes), "r") as archive:
        for entry in class_entries:
            normalized = _validate_member_name(entry)
            target = (destination_dir / normalized).resolve()
            root = destination_dir.resolve()
            if not str(target).startswith(f"{root}/") and target != root:
                raise ValueError(f"Class entry escapes destination dir: {entry}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(entry))
            extracted.append(target)
    return extracted


def class_name_from_entry(entry: str) -> str:
    return entry.removesuffix(".class").replace("/", ".")


def _to_filelike(raw: bytes):
    from io import BytesIO

    return BytesIO(raw)

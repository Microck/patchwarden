from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


LoaderType = Literal["fabric", "forge", "forge_legacy", "unknown"]


class IntakeResult(BaseModel):
    upload_id: str
    filename: str
    mod_type: Literal["minecraft_jar"] = "minecraft_jar"
    loader: LoaderType
    file_count: int
    top_level_entries: list[str] = Field(default_factory=list)
    manifest: dict[str, str] = Field(default_factory=dict)

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


router = APIRouter()
_UI_DIR = Path(__file__).resolve().parents[2] / "ui"
static_app = StaticFiles(directory=str(_UI_DIR))


@router.get("/", include_in_schema=False)
def ui_index() -> FileResponse:
    return FileResponse(_UI_DIR / "index.html")

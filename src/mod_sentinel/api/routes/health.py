from __future__ import annotations

from fastapi import APIRouter

from mod_sentinel import __version__


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "mod-sentinel",
        "version": __version__,
    }

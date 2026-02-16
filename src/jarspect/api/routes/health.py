from __future__ import annotations

from fastapi import APIRouter

from jarspect import __version__


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "jarspect",
        "version": __version__,
    }

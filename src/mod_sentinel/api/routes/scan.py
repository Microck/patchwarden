from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from mod_sentinel.agents.intake_agent import IntakeAgent


router = APIRouter()


class ScanRequest(BaseModel):
    upload_id: str


@router.post("/scan")
def scan_upload(request: ScanRequest) -> dict[str, dict[str, object]]:
    agent = IntakeAgent()

    try:
        intake = agent.run_intake(request.upload_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Upload not found") from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"intake": intake.model_dump()}

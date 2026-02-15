from __future__ import annotations

from fastapi import APIRouter, HTTPException

from mod_sentinel.agents.intake_agent import IntakeAgent
from mod_sentinel.agents.static_agent import StaticAgent
from mod_sentinel.models.scan import ScanRequest, ScanResult


router = APIRouter()


@router.post("/scan")
def scan_upload(request: ScanRequest) -> dict[str, object]:
    intake_agent = IntakeAgent()
    static_agent = StaticAgent()

    try:
        intake = intake_agent.run_intake(request.upload_id)
        static_artifact = static_agent.analyze(request.upload_id)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Upload not found") from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    result = ScanResult(intake=intake, static=static_artifact.findings)
    return result.model_dump()

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from jarspect.models.scan import ScanRequest, ScanRunResponse
from jarspect.pipeline.scan_pipeline import run_scan
from jarspect.store import get_scan_store


router = APIRouter()


@router.post("/scan")
def scan_upload(request: ScanRequest) -> dict[str, object]:
    try:
        scan_id, result = run_scan(request)
        get_scan_store().save_scan(scan_id, result)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Upload not found") from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    response = ScanRunResponse(scan_id=scan_id, result=result)
    return response.model_dump(exclude_none=True)

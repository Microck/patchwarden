from __future__ import annotations

from pydantic import BaseModel

from mod_sentinel.models.intake import IntakeResult
from mod_sentinel.models.static import StaticFindings


class ScanRequest(BaseModel):
    upload_id: str


class ScanResult(BaseModel):
    intake: IntakeResult
    static: StaticFindings

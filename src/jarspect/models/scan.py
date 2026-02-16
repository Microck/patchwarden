from __future__ import annotations

from pydantic import BaseModel

from jarspect.models.behavior import BehaviorPrediction
from jarspect.models.intake import IntakeResult
from jarspect.models.reputation import AuthorMetadata, ReputationResult
from jarspect.models.static import StaticFindings
from jarspect.models.verdict import Verdict


class ScanRequest(BaseModel):
    upload_id: str
    author: AuthorMetadata | None = None


class ScanResult(BaseModel):
    intake: IntakeResult
    static: StaticFindings
    behavior: BehaviorPrediction
    reputation: ReputationResult | None = None
    verdict: Verdict | None = None


class ScanRunResponse(BaseModel):
    scan_id: str
    result: ScanResult

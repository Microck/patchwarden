from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


RiskTier = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
IndicatorSource = Literal["static", "behavior", "reputation"]
IndicatorSeverity = Literal["low", "med", "high", "critical"]


class VerdictIndicator(BaseModel):
    source: IndicatorSource
    id: str
    title: str
    severity: IndicatorSeverity
    evidence: str


class Verdict(BaseModel):
    risk_tier: RiskTier
    risk_score: int = Field(ge=0, le=100)
    summary: str
    explanation: str
    indicators: list[VerdictIndicator] = Field(default_factory=list)

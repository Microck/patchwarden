from __future__ import annotations

from pydantic import BaseModel, Field


class FileSystemPrediction(BaseModel):
    reads: list[str] = Field(default_factory=list)
    writes: list[str] = Field(default_factory=list)
    rationale: str = "unknown"
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)


class NetworkPrediction(BaseModel):
    domains: list[str] = Field(default_factory=list)
    urls: list[str] = Field(default_factory=list)
    ports: list[int] = Field(default_factory=list)
    rationale: str = "unknown"
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)


class PersistencePrediction(BaseModel):
    likely: bool = False
    mechanisms: list[str] = Field(default_factory=list)
    rationale: str = "unknown"
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)


class BehaviorPrediction(BaseModel):
    file_system: FileSystemPrediction
    network: NetworkPrediction
    persistence: PersistencePrediction
    risk_summary: str
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)

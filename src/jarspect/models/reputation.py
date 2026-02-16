from __future__ import annotations

from pydantic import BaseModel, Field


class AuthorMetadata(BaseModel):
    author_id: str
    mod_id: str | None = None
    account_age_days: int | None = None
    prior_mod_count: int | None = None
    report_count: int | None = None


class ReputationResult(BaseModel):
    author_id: str
    account_age_days: int = Field(ge=0)
    prior_mod_count: int = Field(ge=0)
    report_count: int = Field(ge=0)
    report_reasons: list[str] = Field(default_factory=list)
    author_score: float = Field(ge=0.0, le=1.0)
    rationale: list[str] = Field(default_factory=list)

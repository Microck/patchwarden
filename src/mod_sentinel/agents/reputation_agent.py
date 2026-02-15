from __future__ import annotations

from mod_sentinel.models.reputation import AuthorMetadata, ReputationResult
from mod_sentinel.store.reputation_fixtures import ReputationFixtureStore


class ReputationAgent:
    def __init__(self, fixture_store: ReputationFixtureStore | None = None) -> None:
        self._fixtures = fixture_store or ReputationFixtureStore()

    def score_author(self, metadata: AuthorMetadata) -> ReputationResult:
        history = self._fixtures.get_author_history(metadata.author_id)
        report_entry, report_source = self._resolve_report_entry(metadata)

        account_age_days = _to_non_negative_int(
            (history or {}).get("account_age_days"),
            fallback=metadata.account_age_days,
        )
        prior_mod_count = _to_non_negative_int(
            (history or {}).get("prior_mod_count"),
            fallback=metadata.prior_mod_count,
        )
        report_count = _to_non_negative_int(
            (report_entry or {}).get("report_count"),
            fallback=metadata.report_count,
        )
        report_reasons = _normalize_reasons((report_entry or {}).get("report_reasons"))

        score = _compute_author_score(
            account_age_days=account_age_days,
            prior_mod_count=prior_mod_count,
            report_count=report_count,
        )
        rationale = _build_rationale(
            metadata=metadata,
            history_present=history is not None,
            report_source=report_source,
            account_age_days=account_age_days,
            prior_mod_count=prior_mod_count,
            report_count=report_count,
            report_reasons=report_reasons,
            score=score,
        )

        return ReputationResult(
            author_id=metadata.author_id,
            account_age_days=account_age_days,
            prior_mod_count=prior_mod_count,
            report_count=report_count,
            report_reasons=report_reasons,
            author_score=score,
            rationale=rationale,
        )

    def _resolve_report_entry(
        self, metadata: AuthorMetadata
    ) -> tuple[dict | None, str | None]:
        if metadata.mod_id:
            mod_entry = self._fixtures.get_mod_report(metadata.mod_id)
            if mod_entry is not None:
                return mod_entry, f"fixture-mod:{metadata.mod_id}"

        author_entry = self._fixtures.get_author_report(metadata.author_id)
        if author_entry is not None:
            return author_entry, f"fixture-author:{metadata.author_id}"

        return None, None


def _to_non_negative_int(value: object, fallback: int | None) -> int:
    if value is not None:
        try:
            return max(0, int(value))
        except (TypeError, ValueError):
            pass
    if fallback is None:
        return 0
    return max(0, int(fallback))


def _normalize_reasons(raw: object) -> list[str]:
    if not isinstance(raw, list):
        return []
    reasons: list[str] = []
    for item in raw:
        text = str(item).strip()
        if text:
            reasons.append(text)
    return reasons


def _compute_author_score(
    account_age_days: int, prior_mod_count: int, report_count: int
) -> float:
    age_score = min(account_age_days / 365.0, 1.0)
    mod_score = min(prior_mod_count / 20.0, 1.0)
    report_penalty = min(report_count / 10.0, 1.0)

    weighted = (0.5 * age_score) + (0.35 * mod_score) + (0.15 * (1.0 - report_penalty))
    return round(max(0.0, min(1.0, weighted)), 3)


def _build_rationale(
    metadata: AuthorMetadata,
    history_present: bool,
    report_source: str | None,
    account_age_days: int,
    prior_mod_count: int,
    report_count: int,
    report_reasons: list[str],
    score: float,
) -> list[str]:
    rationale: list[str] = []

    if history_present:
        rationale.append(
            f"Loaded author history from fixtures for {metadata.author_id}."
        )
    else:
        rationale.append(
            "No fixture author history found; used request-provided metadata where available."
        )

    if report_source:
        rationale.append(f"Report count sourced from {report_source}.")
    else:
        rationale.append(
            "No fixture community reports found; used request-provided report count or defaulted to 0."
        )

    rationale.append(
        f"Signals: account_age_days={account_age_days}, prior_mod_count={prior_mod_count}, report_count={report_count}."
    )

    if report_reasons:
        sample = "; ".join(report_reasons[:2])
        rationale.append(f"Recent report themes: {sample}.")

    rationale.append(
        f"Final normalized author_score={score:.3f} (1.0 is most trustworthy)."
    )
    return rationale

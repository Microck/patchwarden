from __future__ import annotations

from mod_sentinel.agents.reputation_agent import ReputationAgent
from mod_sentinel.models.reputation import AuthorMetadata


def test_reputation_prefers_fixture_data_over_request_overrides() -> None:
    agent = ReputationAgent()

    result = agent.score_author(
        AuthorMetadata(
            author_id="new_creator",
            mod_id="demo-suspicious",
            account_age_days=9999,
            prior_mod_count=999,
            report_count=0,
        )
    )

    assert result.account_age_days == 14
    assert result.prior_mod_count == 1
    assert result.report_count == 4
    assert result.report_reasons
    assert result.author_score < 0.3
    assert any("fixture" in line.lower() for line in result.rationale)


def test_reputation_falls_back_to_provided_metadata_when_fixture_missing() -> None:
    agent = ReputationAgent()

    result = agent.score_author(
        AuthorMetadata(
            author_id="unknown_author",
            account_age_days=180,
            prior_mod_count=5,
            report_count=1,
        )
    )

    assert result.account_age_days == 180
    assert result.prior_mod_count == 5
    assert result.report_count == 1
    assert 0.0 <= result.author_score <= 1.0
    assert any("No fixture" in line for line in result.rationale)


def test_reputation_scoring_is_deterministic() -> None:
    agent = ReputationAgent()
    metadata = AuthorMetadata(author_id="borderline_creator", mod_id="demo-clean")

    first = agent.score_author(metadata)
    second = agent.score_author(metadata)

    assert first.author_score == second.author_score
    assert first.rationale == second.rationale

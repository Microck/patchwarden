from __future__ import annotations

from mod_sentinel.agents.behavior_agent import BehaviorAgent
from mod_sentinel.llm.client import StubLLMClient
from mod_sentinel.models.static import StaticFindings, StaticIndicator


def test_behavior_agent_returns_validated_prediction_from_stub() -> None:
    static_findings = StaticFindings(
        matches=[
            StaticIndicator(
                source="pattern",
                id="NET-URLCONNECTION",
                title="URLConnection usage",
                category="network",
                severity="med",
                file_path="com/example/Demo.class",
                evidence="java.net.URLConnection",
                rationale="network usage",
            )
        ],
        counts_by_category={"network": 1},
        counts_by_severity={"med": 1},
        matched_pattern_ids=["NET-URLCONNECTION"],
        analyzed_files=1,
    )

    agent = BehaviorAgent(llm_client=StubLLMClient())
    prediction = agent.predict(static_findings, snippets=["java.net.URLConnection"])

    assert prediction.risk_summary
    assert prediction.network.urls
    assert 0.0 <= prediction.confidence <= 1.0

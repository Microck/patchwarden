from __future__ import annotations

from uuid import uuid4

from jarspect.agents.behavior_agent import BehaviorAgent
from jarspect.agents.intake_agent import IntakeAgent
from jarspect.agents.reputation_agent import ReputationAgent
from jarspect.agents.static_agent import StaticAgent
from jarspect.agents.verdict_agent import VerdictAgent
from jarspect.models.scan import ScanRequest, ScanResult
from jarspect.pipeline.snippet_select import select_snippets


def run_scan(request: ScanRequest) -> tuple[str, ScanResult]:
    intake_agent = IntakeAgent()
    static_agent = StaticAgent()
    behavior_agent = BehaviorAgent()
    reputation_agent = ReputationAgent()
    verdict_agent = VerdictAgent()

    intake = intake_agent.run_intake(request.upload_id)
    static_artifact = static_agent.analyze(request.upload_id)
    snippets = select_snippets(static_artifact.findings, static_artifact.sources)
    behavior = behavior_agent.predict(static_artifact.findings, snippets)

    reputation = None
    if request.author is not None:
        reputation = reputation_agent.score_author(request.author)

    verdict = verdict_agent.synthesize(
        intake=intake,
        static_findings=static_artifact.findings,
        behavior=behavior,
        reputation=reputation,
    )

    result = ScanResult(
        intake=intake,
        static=static_artifact.findings,
        behavior=behavior,
        reputation=reputation,
        verdict=verdict,
    )
    return uuid4().hex, result

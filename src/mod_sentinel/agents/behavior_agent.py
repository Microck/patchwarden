from __future__ import annotations

from mod_sentinel.llm.client import LLMClient, build_llm_client
from mod_sentinel.llm.prompts import build_behavior_prompts
from mod_sentinel.models.behavior import BehaviorPrediction
from mod_sentinel.models.static import StaticFindings


class BehaviorAgent:
    def __init__(self, llm_client: LLMClient | None = None) -> None:
        self._llm_client = llm_client or build_llm_client()

    def predict(
        self,
        static_findings: StaticFindings,
        snippets: list[str] | None = None,
    ) -> BehaviorPrediction:
        system_prompt, user_prompt = build_behavior_prompts(static_findings, snippets)
        payload = self._llm_client.complete_json(system_prompt, user_prompt)
        return BehaviorPrediction.model_validate(payload)

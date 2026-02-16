from __future__ import annotations

from jarspect.llm.behavior_contract import normalize_behavior_payload
from jarspect.llm.client import LLMClient, build_llm_client
from jarspect.llm.json_extract import extract_first_json_object
from jarspect.llm.prompts import build_behavior_prompts
from jarspect.models.behavior import BehaviorPrediction
from jarspect.models.static import StaticFindings


class BehaviorAgent:
    def __init__(self, llm_client: LLMClient | None = None) -> None:
        self._llm_client = llm_client or build_llm_client()

    def predict(
        self,
        static_findings: StaticFindings,
        snippets: list[str] | None = None,
    ) -> BehaviorPrediction:
        system_prompt, user_prompt = build_behavior_prompts(static_findings, snippets)
        raw_response = self._llm_client.complete_text(system_prompt, user_prompt)
        extracted = extract_first_json_object(raw_response)
        normalized = normalize_behavior_payload(extracted)
        return BehaviorPrediction.model_validate(normalized)

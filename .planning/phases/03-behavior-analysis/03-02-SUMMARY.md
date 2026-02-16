---
phase: 03-behavior-analysis
plan: 02
subsystem: ai
tags: [json-parsing, contract-normalization, llm-reliability]
requires:
  - phase: 03-behavior-analysis
    provides: "BehaviorAgent and LLM abstraction"
provides:
  - "Robust JSON extraction utility for wrapped LLM responses"
  - "Behavior normalization contract with unknown-safe defaults"
  - "BehaviorAgent parsing path hardened against malformed output"
affects: [03-03, 04-reputation-verdict, 05-demo-submit]
tech-stack:
  added: []
  patterns: ["treat LLM text as untrusted input", "normalize-before-validate"]
key-files:
  created:
    [
      "src/jarspect/llm/json_extract.py",
      "src/jarspect/llm/behavior_contract.py",
      "tests/test_llm_json_extract.py",
      "tests/test_behavior_contract.py",
      "tests/test_behavior_agent_parsing.py",
    ]
  modified: ["src/jarspect/agents/behavior_agent.py", "src/jarspect/llm/__init__.py"]
key-decisions:
  - "Parse raw text first; never trust provider to return strict JSON only."
  - "Use confidence=0 unknown fallbacks instead of raising parse exceptions in behavior stage."
patterns-established:
  - "LLM extraction and normalization are explicit pipeline steps."
  - "BehaviorAgent always returns validated model, even with partial upstream payloads."
duration: 4min
completed: 2026-02-15
---

# Phase 3 Plan 2: Parsing Hardening Summary

**Hardened behavior prediction reliability by extracting JSON from noisy LLM output and normalizing malformed sections into safe unknown defaults.**

## Performance

- **Duration:** 4 min
- **Started:** 2026-02-15T19:48:16Z
- **Completed:** 2026-02-15T19:52:31Z
- **Tasks:** 3
- **Files modified:** 7

## Accomplishments

- Added resilient JSON extraction for plain JSON, fenced JSON, and noisy wrapper text.
- Added behavior contract normalization with section-level graceful degradation.
- Updated BehaviorAgent to use raw-text parsing + normalization before model validation.

## Task Commits

1. **Task 1: Implement robust JSON extraction helper for LLM outputs** - `6334032` (feat)
2. **Task 2: Define behavior contract + safe degradation rules** - `0788771` (feat)
3. **Task 3: Wire json_extract + behavior_contract into BehaviorAgent parsing** - `7998025` (feat)

## Files Created/Modified

- `src/jarspect/llm/json_extract.py` - extraction logic with fenced-json priority
- `src/jarspect/llm/behavior_contract.py` - normalization contract and coercion helpers
- `src/jarspect/agents/behavior_agent.py` - untrusted text parsing pipeline
- `tests/test_llm_json_extract.py` - extraction format coverage
- `tests/test_behavior_contract.py` - normalization/degradation coverage
- `tests/test_behavior_agent_parsing.py` - markdown-wrapped JSON integration test

## Decisions Made

- Made parser resilience mandatory in main code path (not test-only utility).
- Converted malformed sections to explicit unknown values rather than failing the whole scan.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- None.

## User Setup Required

None.

## Next Phase Readiness

- Behavior parsing is now robust enough for endpoint-level integration in `03-03`.

## Self-Check: PASSED

- `.planning/phases/03-behavior-analysis/03-02-SUMMARY.md` exists.
- Commits `6334032`, `0788771`, and `7998025` exist in git log.

---

*Phase: 03-behavior-analysis*
*Completed: 2026-02-15*

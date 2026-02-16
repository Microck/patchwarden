---
phase: 04-reputation-verdict
plan: 01
subsystem: api
tags: [reputation-agent, fixture-store, scan-schema]
requires:
  - phase: 03-behavior-analysis
    provides: "Scan endpoint includes intake/static/behavior outputs"
provides:
  - "Fixture-backed ReputationAgent for author history and community reports"
  - "Optional scan.author input and reputation output in /scan responses"
  - "Deterministic reputation tests for fixture precedence and fallback behavior"
affects: [04-02, 04-03, 05-demo-submit]
tech-stack:
  added: []
  patterns: ["local fixture lookups over external APIs", "deterministic weighted trust scoring"]
key-files:
  created:
    [
      "src/jarspect/agents/reputation_agent.py",
      "src/jarspect/store/reputation_fixtures.py",
      "src/jarspect/fixtures/reputation/author_history.json",
      "src/jarspect/fixtures/reputation/community_reports.json",
      "src/jarspect/models/reputation.py",
      "tests/test_reputation.py",
    ]
  modified: ["src/jarspect/api/routes/scan.py", "src/jarspect/models/scan.py"]
key-decisions:
  - "Prefer local fixture values over request metadata whenever fixture data exists for reproducible demos."
  - "Use a transparent weighted heuristic (age/mod history/reports) to keep score behavior explainable."
patterns-established:
  - "Reputation stage is optional and activates only when scan request includes author metadata."
  - "Community report lookup prioritizes mod-specific fixtures over author-level aggregates."
duration: 4min
completed: 2026-02-15
---

# Phase 4 Plan 1: Reputation Fixtures and Scan Input Summary

**Shipped a deterministic ReputationAgent with local fixture lookups and wired optional author metadata into `/scan` so reputation can feed upcoming verdict synthesis.**

## Performance

- **Duration:** 4 min
- **Started:** 2026-02-15T20:17:30Z
- **Completed:** 2026-02-15T20:21:31Z
- **Tasks:** 2
- **Files modified:** 10

## Accomplishments

- Added `ReputationAgent` plus file-backed fixture store for author history and community report signals (REP-01, REP-02).
- Added local fixture corpus under `src/jarspect/fixtures/reputation/` for deterministic MVP demos.
- Extended `/scan` request/response models to support optional `author` metadata and `reputation` results.
- Added tests for fixture precedence, metadata fallback, deterministic scoring, and API-level reputation inclusion.

## Task Commits

1. **Task 1: Reputation models + local fixture lookups + scoring heuristics** - `57e4ba8` (feat)
2. **Task 2: Extend scan request schema to accept author identifier + optional provided metadata** - `c9785bf` (feat)

## Files Created/Modified

- `src/jarspect/agents/reputation_agent.py` - deterministic reputation scoring with rationale output.
- `src/jarspect/store/reputation_fixtures.py` - local JSON fixture loader and report lookup helpers.
- `src/jarspect/fixtures/reputation/author_history.json` - author history fixture dataset.
- `src/jarspect/fixtures/reputation/community_reports.json` - community report fixture dataset.
- `src/jarspect/models/reputation.py` - author input and reputation result models.
- `src/jarspect/models/scan.py` - optional author input and reputation output fields.
- `src/jarspect/api/routes/scan.py` - optional reputation stage in scan orchestration.
- `tests/test_reputation.py` - unit + API coverage for reputation behavior.

## Decisions Made

- Selected local fixture lookups instead of scraping or external services to keep MVP deterministic and demo-safe.
- Used a conservative weighted score formula (age/mod history/reports) so outputs remain stable and explainable.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Scan pipeline now has intake/static/behavior plus optional reputation input needed for verdict synthesis in `04-02`.

## Self-Check: PASSED

- `.planning/phases/04-reputation-verdict/04-01-SUMMARY.md` exists.
- Commits `57e4ba8` and `c9785bf` exist in git log.

---

*Phase: 04-reputation-verdict*
*Completed: 2026-02-15*

---
phase: 05-demo-submit
plan: 01
subsystem: ui
tags: [web-ui, static-assets, fastapi-static]
requires:
  - phase: 04-reputation-verdict
    provides: "Stable upload/scan/scans APIs with verdict output"
provides:
  - "Static browser UI for upload and verdict display"
  - "Same-origin FastAPI serving at / and /static"
  - "Client flow for upload -> scan -> indicator rendering"
affects: [05-02, 05-03]
tech-stack:
  added: []
  patterns:
    [
      "framework-free static frontend",
      "same-origin API orchestration from browser UI",
    ]
key-files:
  created:
    [
      "src/mod_sentinel/ui/index.html",
      "src/mod_sentinel/ui/app.js",
      "src/mod_sentinel/ui/styles.css",
      "src/mod_sentinel/api/routes/ui.py",
    ]
  modified: ["src/mod_sentinel/api/main.py", "src/mod_sentinel/api/routes/__init__.py"]
key-decisions:
  - "Serve static UI directly from FastAPI for demo simplicity and no CORS complexity."
  - "Expose author metadata controls in UI so demo runs can highlight reputation impacts."
patterns-established:
  - "UI uses /upload then /scan and renders verdict.indicators directly."
  - "Root path `/` serves index while assets are under `/static/*`."
duration: 3min
completed: 2026-02-15
---

# Phase 5 Plan 1: Demo UI Summary

**Built and served a lightweight web UI that runs the full PatchWarden flow from browser upload through verdict indicator rendering.**

## Performance

- **Duration:** 3 min
- **Started:** 2026-02-15T20:33:00Z
- **Completed:** 2026-02-15T20:35:33Z
- **Tasks:** 2
- **Files modified:** 6

## Accomplishments

- Added a deliberate, responsive static interface for `.jar` uploads and optional author metadata controls.
- Implemented browser-side workflow for `/upload` -> `/scan` and verdict/indicator rendering.
- Added FastAPI UI route and static mount so the demo loads from `GET /` with no extra frontend server.

## Task Commits

1. **Task 1: Create static UI (upload + results)** - `83c8cfb` (feat)
2. **Task 2: Serve UI from FastAPI** - `413a7da` (feat)

## Files Created/Modified

- `src/mod_sentinel/ui/index.html` - upload, metadata form, and verdict display markup.
- `src/mod_sentinel/ui/app.js` - browser orchestration of upload/scan requests and result rendering.
- `src/mod_sentinel/ui/styles.css` - visual system and responsive styling for demo readability.
- `src/mod_sentinel/api/routes/ui.py` - root index route + static asset app.
- `src/mod_sentinel/api/main.py` - UI route registration and `/static` mount.
- `src/mod_sentinel/api/routes/__init__.py` - route exports include UI router.

## Decisions Made

- Chose plain HTML/CSS/JS over framework setup to keep hackathon demo startup friction near zero.
- Kept UI hosted by backend process so judges can run one command and open one URL.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- UI is ready for synthetic sample automation and scripted terminal demo flow in `05-02`.

## Self-Check: PASSED

- `.planning/phases/05-demo-submit/05-01-SUMMARY.md` exists.
- Commits `83c8cfb` and `413a7da` exist in git log.

---

*Phase: 05-demo-submit*
*Completed: 2026-02-15*

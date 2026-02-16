# Jarspect 2-Minute Demo Storyboard

## Total Runtime: ~2:00

## 0:00 - 0:20 | Problem + Product

- Show the Jarspect UI at `http://localhost:8000/`.
- Narration:
  - "Gamers install mods from many sources and cannot inspect every jar manually."
  - "Jarspect runs layered analysis and produces a clear risk verdict."

## 0:20 - 0:45 | Trigger the Scan

- In terminal, run `bash scripts/demo_run.sh` (or use UI upload form).
- Narration:
  - "This builds a synthetic suspicious sample and sends it through the API."
  - "No real malware is used; the sample is safe and deterministic."

## 0:45 - 1:20 | Walk Through Agents

- Show script output or API response fields:
  - static indicators (`EXEC-RUNTIME`, signature hits)
  - behavior indicators (`BEH-NETWORK`, `BEH-PERSISTENCE`)
  - reputation indicator (`REP-AUTHOR-TRUST`)
- Narration:
  - "Each agent adds evidence, and verdict synthesis combines all signals."

## 1:20 - 1:45 | Verdict + Explainability

- Highlight final `risk_tier`, `risk_score`, and indicator list in UI.
- Narration:
  - "Jarspect does not just score risk; it explains exactly why."
  - "This helps users make informed install decisions quickly."

## 1:45 - 2:00 | Close

- Show persisted scan retrieval by `scan_id` (`GET /scans/{scan_id}`).
- Narration:
  - "Results are stored for later review, sharing, and moderation workflows."
  - "Jarspect delivers actionable safety signals in minutes."

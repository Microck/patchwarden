# PatchWarden

PatchWarden is a multi-agent security scanner for Minecraft mods (`.jar`) that
helps players and communities detect suspicious behavior before installation.

It combines deterministic static analysis, behavior prediction, author
reputation scoring, and final verdict synthesis.

## Pipeline

```text
Upload (.jar)
    |
    v
Intake Agent (loader + manifest inspection)
    |
    v
Static Agent (decompile + pattern/signature matches)
    |
    v
Behavior Agent (predicted file/network/persistence behavior)
    |
    +--> Reputation Agent (optional author metadata + fixture history)
    |
    v
Verdict Agent (risk tier + score + explanation + indicators)
    |
    v
Persisted Scan Result (scan_id, retrievable via GET /scans/{scan_id})
```

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```

Run the API + web UI:

```bash
python3 -m uvicorn mod_sentinel.api.main:app --reload
```

Open:

- `http://localhost:8000/` for upload + verdict UI
- `http://localhost:8000/docs` for API docs

## Demo Command

With the API server running, execute:

```bash
bash scripts/demo_run.sh
```

The script will:

1. Build a synthetic suspicious sample jar
2. Upload it via `/upload`
3. Run `/scan` with demo author metadata
4. Fetch persisted result via `/scans/{scan_id}`
5. Print verdict tier, score, and top indicators

## Example Output

```text
scan_id: dc42efda4be44fa190b96a71d95948a1
risk_tier: CRITICAL
risk_score: 100

top_indicators:
- [high] EXEC-RUNTIME (static) Runtime process execution
- [high] BEH-NETWORK (behavior) Predicted outbound network activity
- [critical] REP-AUTHOR-TRUST (reputation) Author trust score
```

## Safety Note

PatchWarden includes **synthetic demo fixtures only**.

- `demo/samples/suspicious_mod_src/` is intentionally benign source code.
- `demo/suspicious_sample.jar` is generated locally for demonstrations.
- No real malware samples are downloaded, bundled, or distributed.

## Test Suite

```bash
python3 -m pytest -q
```

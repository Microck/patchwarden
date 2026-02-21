# Jarspect

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Jarspect is a security scanner for Minecraft mods (`.jar`) that flags suspicious behavior before installation.

It combines deterministic static analysis (patterns + signatures + YARA-X), fixture-backed reputation scoring, and a final verdict synthesis that produces a risk tier, score, and explainable indicators.

<!-- top-readme: begin -->

## Configuration

- [.env.example](.env.example)
- [Quick Start](#quick-start)

## Web UI

- [Quick Start](#quick-start)

## Development

- [Testing](#testing)
- [scripts/demo_run.sh](scripts/demo_run.sh)

## Support

- [Contributing](#contributing)

## Security

- [Safety](#safety)

## Changelog / Releases

## Roadmap

- [.planning/ROADMAP.md](.planning/ROADMAP.md)

<!-- top-readme: end -->

## Features

- Upload + scan pipeline with persisted results (`scan_id`)
- Static analysis over `.jar` contents (regex patterns, signature corpus, YARA-X)
- Behavior + reputation signals (demo/heuristic)
- Web UI for upload and verdict review
- Deterministic demo fixtures (no real malware)

## How It Works

1. Upload a `.jar` (`POST /upload`) and receive an `upload_id`.
2. Run a scan (`POST /scan`) over the uploaded artifact.
3. Persist the scan result as JSON (`.local-data/scans/{scan_id}.json`) and fetch it later (`GET /scans/{scan_id}`).

The scan result includes:

- `intake`: archive inventory (file counts, class counts)
- `static`: suspicious indicators from patterns/signatures/YARA
- `behavior`: predicted behaviors derived from static indicators
- `reputation`: optional author risk signals (demo inputs)
- `verdict`: risk tier + score + explainable indicator list

## Installation

Prereqs:
- Rust (stable toolchain)

Optional (for the scripted demo):
- `curl`
- Node.js (used only to parse JSON in `scripts/demo_run.sh`)
- JDK (`javac` + `jar`) for the demo `.jar` build; otherwise a deterministic fallback jar is generated

## Quick Start

1. Run the API + web UI:

```bash
cargo run
```

Environment variables:

- `JARSPECT_BIND` (default `127.0.0.1:8000`)
- `RUST_LOG` (default `jarspect=info,tower_http=info`)

2. Open:
- `http://localhost:8000/` (UI)
- `http://localhost:8000/health` (health)

3. Run the scripted demo (with the server running):

```bash
bash scripts/demo_run.sh
```

## Usage

Minimal API surface:

- `POST /upload` (multipart file upload)
- `POST /scan` (scan an upload_id + metadata)
- `GET /scans/{scan_id}` (fetch persisted results)

Example (manual):

```bash
# Upload a jar
curl -sS -X POST "http://localhost:8000/upload" \
  -F "file=@./demo/suspicious_sample.jar;type=application/java-archive"

# Then POST /scan with the returned upload_id
curl -sS -X POST "http://localhost:8000/scan" \
  -H "Content-Type: application/json" \
  -d '{"upload_id":"<upload_id>","author":{"author_id":"new_creator","account_age_days":7,"prior_mod_count":0,"report_count":3}}'
```

## Safety

This repo includes synthetic demo fixtures only:

- `demo/samples/suspicious_mod_src/` is intentionally benign source code.
- `demo/suspicious_sample.jar` is generated locally for demonstrations.
- No real malware samples are downloaded, bundled, or distributed.

Important: The current behavior and reputation layers are deterministic demo logic. This is a hackathon-grade scanner intended for showcasing a pipeline and explainability, not production malware classification.

## Testing

```bash
cargo check
cargo test
```

## Contributing

Issues and pull requests are welcome.

## License

Apache-2.0 (see `LICENSE`).

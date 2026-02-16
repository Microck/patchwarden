# Jarspect

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Jarspect is a security scanner for Minecraft mods (`.jar`) that flags suspicious behavior before installation.

It combines deterministic static analysis and fixture-backed reputation scoring, plus a final verdict synthesis that produces a risk tier, score, and explainable indicators.

## Features

- Upload + scan pipeline with persisted results (`scan_id`)
- Deterministic demo fixtures (no real malware)
- Web UI for upload and verdict review
- API docs via OpenAPI UI (`/docs`)

## Installation

Prereqs:
- Rust (stable toolchain)

## Quick Start

1. Run the API + web UI:

```bash
cargo run
```

2. Open:
- `http://localhost:8000/` (UI)
- `http://localhost:8000/docs` (API docs)

3. Run the scripted demo (with the server running):

```bash
bash scripts/demo_run.sh
```

## Usage

Minimal API surface:

- `POST /upload` (multipart file upload)
- `POST /scan` (scan an upload_id + metadata)
- `GET /scans/{scan_id}` (fetch persisted results)

## Safety

This repo includes synthetic demo fixtures only:

- `demo/samples/suspicious_mod_src/` is intentionally benign source code.
- `demo/suspicious_sample.jar` is generated locally for demonstrations.
- No real malware samples are downloaded, bundled, or distributed.

## Testing

```bash
cargo check
cargo test
```

## Contributing

Issues and pull requests are welcome.

## License

Apache-2.0 (see `LICENSE`).

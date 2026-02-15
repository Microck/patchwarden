# Synthetic Suspicious Demo Fixture

This folder contains a **safe, synthetic** Java sample used for PatchWarden demos.

## Safety guarantees

- No network requests are executed.
- No files are written.
- No processes are launched.
- No external content is downloaded.

The source intentionally includes suspicious-looking strings and dead-code patterns
so static analysis flags realistic indicators during demos.

Generated artifact:

- `demo/suspicious_sample.jar`

Build it with:

```bash
bash demo/build_sample.sh
```

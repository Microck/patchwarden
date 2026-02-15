"""Local import shim for src-layout development."""

from __future__ import annotations

from pathlib import Path


_SRC_PACKAGE_DIR = Path(__file__).resolve().parent.parent / "src" / "mod_sentinel"
__path__ = [str(_SRC_PACKAGE_DIR)]
__version__ = "0.1.0"

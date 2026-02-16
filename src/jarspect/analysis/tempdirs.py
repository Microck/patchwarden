from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator


@contextmanager
def managed_tempdir(prefix: str = "jarspect-") -> Iterator[Path]:
    with TemporaryDirectory(prefix=prefix) as tempdir:
        yield Path(tempdir)

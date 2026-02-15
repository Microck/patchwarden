from __future__ import annotations

from io import BytesIO
from zipfile import ZipFile

from mod_sentinel.analysis.jar_classes import extract_class_entries, list_class_entries
from mod_sentinel.analysis.tempdirs import managed_tempdir


def _build_class_jar() -> bytes:
    class_bytes = b"\xca\xfe\xba\xbeDemoClassrunTaskmainhelperToken"
    buffer = BytesIO()
    with ZipFile(buffer, "w") as archive:
        archive.writestr("com/example/DemoClass.class", class_bytes)
        archive.writestr("README.txt", b"not-a-class")
    return buffer.getvalue()


def test_list_and_extract_class_entries() -> None:
    jar_bytes = _build_class_jar()

    entries = list_class_entries(jar_bytes)
    assert entries == ["com/example/DemoClass.class"]

    with managed_tempdir(prefix="mod-sentinel-test-") as tempdir:
        extracted = extract_class_entries(jar_bytes, entries, tempdir)
        assert len(extracted) == 1
        assert extracted[0].exists()

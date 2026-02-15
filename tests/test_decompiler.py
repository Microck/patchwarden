from __future__ import annotations

from io import BytesIO
from zipfile import ZipFile

from mod_sentinel.analysis.decompiler import Decompiler


def _build_class_jar() -> bytes:
    class_bytes = b"\xca\xfe\xba\xbeDemoClassrunTaskmainhelperToken"
    buffer = BytesIO()
    with ZipFile(buffer, "w") as archive:
        archive.writestr("com/example/DemoClass.class", class_bytes)
        archive.writestr("README.txt", b"not-a-class")
    return buffer.getvalue()


def test_decompiler_fallback_contains_class_and_method_tokens() -> None:
    jar_bytes = _build_class_jar()

    outputs = Decompiler(cfr_jar_path=None).decompile(jar_bytes)
    assert len(outputs) == 1
    path, text = outputs[0]
    assert path.endswith("DemoClass.class")
    assert "DemoClass" in text
    assert "runTask" in text

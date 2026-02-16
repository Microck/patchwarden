#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEMO_DIR="${ROOT_DIR}/demo"
SOURCE_FILE="${DEMO_DIR}/samples/suspicious_mod_src/src/main/java/com/jarspect/demo/DemoMod.java"
OUTPUT_JAR="${DEMO_DIR}/suspicious_sample.jar"
BUILD_DIR="${DEMO_DIR}/.build"

mkdir -p "${BUILD_DIR}" "${DEMO_DIR}"
rm -f "${OUTPUT_JAR}"

if command -v javac >/dev/null 2>&1 && command -v jar >/dev/null 2>&1; then
  CLASSES_DIR="${BUILD_DIR}/classes"
  rm -rf "${CLASSES_DIR}"
  mkdir -p "${CLASSES_DIR}"

  javac -d "${CLASSES_DIR}" "${SOURCE_FILE}"
  (
    cd "${CLASSES_DIR}"
    jar cf "${OUTPUT_JAR}" .
  )
else
  echo "[build_sample] javac/jar not found; creating deterministic synthetic jar fallback" >&2
  SOURCE_FILE_PATH="${SOURCE_FILE}" OUTPUT_JAR_PATH="${OUTPUT_JAR}" python3 - <<'PY'
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

source_path = Path(os.environ["SOURCE_FILE_PATH"])
output_jar = Path(os.environ["OUTPUT_JAR_PATH"])
source_text = source_path.read_text(encoding="utf-8")

class_blob = b"\xca\xfe\xba\xbe" + source_text.encode("utf-8")
manifest = "Manifest-Version: 1.0\nCreated-By: Jarspect Demo\n\n"

with ZipFile(output_jar, "w", compression=ZIP_DEFLATED) as archive:
    archive.writestr("META-INF/MANIFEST.MF", manifest)
    archive.writestr("com/jarspect/demo/DemoMod.class", class_blob)
PY
fi

echo "Built synthetic sample jar: ${OUTPUT_JAR}"

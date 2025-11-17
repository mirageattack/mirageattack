#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <name>" >&2
  exit 1
fi

NAME="$1"
DESKTOP_DIR="$HOME/Desktop"
DEST_DIR="/Users/hkus3lab/mirageattack/mirageattack/atlas"
DEST_BASENAME="${DEST_DIR}/${NAME}_clean"

latest_mov=$(ls -t "$DESKTOP_DIR"/*.mov 2>/dev/null | head -n 1 || true)
if [[ -z "${latest_mov}" ]]; then
  echo "No .mov files found in ${DESKTOP_DIR}" >&2
  exit 1
fi

mv "${latest_mov}" "${DEST_BASENAME}.mov"
touch "${DEST_BASENAME}.steps"

echo "${NAME}_clean.mov"
echo "${NAME}_clean.steps"

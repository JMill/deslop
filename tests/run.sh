#!/usr/bin/env bash
#
# deslop rule test suite.
#
# Checks four things:
#   1. should-pass.md produces zero alerts (no false positives on ordinary prose).
#   2. Every rule file under styles/Deslop fires at least once on should-flag.md
#      (no rule is silently dead — a broken regex still loads, it just never matches).
#   3. Every (rule, phrase) pair in expected.tsv is actually flagged.
#   4. No two different rules flag overlapping text (no double-flagging).
#   5. The release zip contains every rule file in the repo.
#
# Usage: tests/run.sh          (needs `vale` on PATH; override with VALE=/path/to/vale)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALE="${VALE:-vale}"

if ! command -v "$VALE" >/dev/null 2>&1; then
  echo "error: '$VALE' not found on PATH. Install Vale 3.0+ (https://vale.sh/docs/vale-cli/installation/)" >&2
  exit 127
fi

cd "$REPO_ROOT"

# Vale exits non-zero whenever it reports an alert, which is the normal case for
# should-flag.md. Capture the JSON and let the checks below decide pass/fail.
json="$("$VALE" --config tests/.vale.ini --output=JSON \
  tests/should-flag.md tests/should-pass.md 2>/dev/null || true)"

if [ -z "$json" ]; then
  echo "error: vale produced no output" >&2
  exit 1
fi

VALE_JSON="$json" VALE_BIN="$(command -v "$VALE")" python3 "$REPO_ROOT/tests/check.py"

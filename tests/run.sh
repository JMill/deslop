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

# Preflight: a previously synced copy of Deslop in Vale's shared styles directory
# SHADOWS this working tree. Vale merges the shared path in whenever the style
# name matches, so a rule file that exists in both resolves to the shared copy --
# and `StylesPath` cannot override it (verified: an absolute temp StylesPath is
# shadowed too). A brand-new rule file still loads from the tree, which makes the
# failure mode maximally confusing: new rules fire, edits to existing rules do
# nothing, and the suite reports false positives and double-flags that are not in
# the code you are reading. This is the same stale-package trap README.md
# documents for consumers; it bites developers here.
for shared in \
  "$HOME/Library/Application Support/vale/styles/Deslop" \
  "${XDG_DATA_HOME:-$HOME/.local/share}/vale/styles/Deslop"
do
  [ -d "$shared" ] || continue
  if ! diff -rq "$shared" "$REPO_ROOT/styles/Deslop" >/dev/null 2>&1; then
    cat >&2 <<EOF
error: a stale Deslop package in Vale's shared styles directory is shadowing this
       working tree, so the suite would test the WRONG rules.

         $shared

       It differs from styles/Deslop. Remove it and re-run:

         rm -rf "$shared"

       (\`vale sync\` recreates it from a release when a consumer project needs it.)
EOF
    exit 1
  fi
done

# Vale exits non-zero whenever it reports an alert, which is the normal case for
# should-flag.md. Capture the JSON and let the checks below decide pass/fail.
# It goes to a file rather than an environment variable: the fixture produces
# enough alerts to blow past the exec argument limit.
report="$(mktemp)"
trap 'rm -f "$report"' EXIT

"$VALE" --config tests/.vale.ini --output=JSON \
  tests/should-flag.md tests/should-pass.md >"$report" 2>/dev/null || true

if [ ! -s "$report" ]; then
  echo "error: vale produced no output" >&2
  exit 1
fi

VALE_REPORT="$report" VALE_BIN="$(command -v "$VALE")" python3 "$REPO_ROOT/tests/check.py"

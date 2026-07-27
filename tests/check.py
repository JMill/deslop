#!/usr/bin/env python3
"""Assertions for the deslop rule suite. Driven by tests/run.sh, which supplies
Vale's JSON output in the VALE_JSON environment variable."""

import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STYLE_DIR = REPO / "styles" / "Deslop"
TESTS = REPO / "tests"

failures = []
checks_run = 0


def fail(check, detail):
    failures.append(f"{check}: {detail}")


def alerts_for(data, name):
    """Vale keys results by the path it was given; match on basename."""
    for path, alerts in data.items():
        if Path(path).name == name:
            return alerts
    return []


data = json.loads(os.environ["VALE_JSON"])
flag_alerts = alerts_for(data, "should-flag.md")
pass_alerts = alerts_for(data, "should-pass.md")

# ---------------------------------------------------------------- 1. no false positives
checks_run += 1
if pass_alerts:
    for a in pass_alerts:
        fail(
            "false positive",
            f"should-pass.md:{a['Line']} {a['Check']} flagged {a['Match']!r}",
        )

# ---------------------------------------------------------------- 2. no dead rules
checks_run += 1
rule_files = {p.stem for p in STYLE_DIR.glob("*.yml")}
fired = {a["Check"].split(".", 1)[1] for a in flag_alerts}
for dead in sorted(rule_files - fired):
    fail("dead rule", f"Deslop.{dead} never matched anything in should-flag.md")

# ---------------------------------------------------------------- 3. expected pairs
checks_run += 1
expected_path = TESTS / "expected.tsv"
for lineno, raw in enumerate(expected_path.read_text().splitlines(), 1):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    try:
        rule, phrase = line.split("\t", 1)
    except ValueError:
        fail("expected.tsv", f"line {lineno} is not <rule>TAB<phrase>: {raw!r}")
        continue
    hit = any(
        a["Check"] == rule and phrase.lower() in a["Match"].lower() for a in flag_alerts
    )
    if not hit:
        fail("missed", f"{rule} did not flag {phrase!r} (expected.tsv line {lineno})")

# ---------------------------------------------------------------- 4. no double-flagging
checks_run += 1
by_line = {}
for a in flag_alerts:
    by_line.setdefault(a["Line"], []).append(a)
for line, alerts in sorted(by_line.items()):
    for i, a in enumerate(alerts):
        for b in alerts[i + 1 :]:
            if a["Check"] == b["Check"]:
                continue
            a_start, a_end = a["Span"]
            b_start, b_end = b["Span"]
            if a_start <= b_end and b_start <= a_end:
                fail(
                    "double-flag",
                    f"should-flag.md:{line} {a['Check']} and {b['Check']} "
                    f"both flag overlapping text ({a['Match']!r} / {b['Match']!r}). "
                    f"Each tell needs exactly one home.",
                )

# ---------------------------------------------------------------- 5. package completeness
# The published v0.1.0 zip shipped 13 of 17 rules for two months because nothing
# compared the archive against the tree. This check does, then goes further and
# lints through the extracted copy — which is what catches a wrong directory
# level or a lowercase `deslop/` that only fails on case-sensitive CI.
checks_run += 1
on_disk = {p.name for p in STYLE_DIR.iterdir() if p.is_file()}

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    zip_path = tmp / "Deslop.zip"
    subprocess.run(
        ["zip", "-rq", str(zip_path), "Deslop"], cwd=REPO / "styles", check=True
    )
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if not n.endswith("/")]
        packaged = {Path(n).name for n in names}
        zf.extractall(tmp / "styles")

    missing = on_disk - packaged
    if missing:
        fail("packaging", f"release zip is missing {sorted(missing)}")
    if "meta.json" not in packaged:
        fail("packaging", "release zip has no meta.json; `vale sync` will reject it")

    # Every entry must sit under a top-level `Deslop/` directory, spelled exactly
    # that way — `BasedOnStyles = Deslop` is case-sensitive on Linux runners.
    bad_root = sorted({n.split("/")[0] for n in names} - {"Deslop"})
    if bad_root:
        fail("packaging", f"zip root should contain only 'Deslop/', found {bad_root}")

    # Now lint through the extracted package exactly as a consumer would.
    vale_bin = os.environ.get("VALE_BIN")
    if not vale_bin:
        fail("packaging", "VALE_BIN not set; cannot verify the extracted package")
    else:
        cfg = tmp / ".vale.ini"
        cfg.write_text(
            f"StylesPath = {tmp / 'styles'}\n"
            "MinAlertLevel = suggestion\n\n"
            "[*.md]\nBasedOnStyles = Deslop\n"
        )
        proc = subprocess.run(
            [vale_bin, "--config", str(cfg), "--output=JSON",
             str(TESTS / "should-flag.md")],
            capture_output=True, text=True,
        )
        try:
            repacked = json.loads(proc.stdout or "{}")
        except json.JSONDecodeError:
            repacked = {}
            fail("packaging", f"vale failed against extracted package: {proc.stderr.strip()}")
        repacked_alerts = alerts_for(repacked, "should-flag.md")
        if not repacked_alerts:
            fail(
                "packaging",
                "the extracted package produced no alerts — consumers would "
                "install it and silently lint nothing",
            )
        repacked_rules = {a["Check"].split(".", 1)[1] for a in repacked_alerts}
        for dead in sorted(rule_files - repacked_rules):
            fail("packaging", f"Deslop.{dead} does not fire from the packaged copy")

# ---------------------------------------------------------------- report
if failures:
    print(f"FAIL — {len(failures)} problem(s)\n")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)

print(
    f"PASS — {checks_run} checks, {len(rule_files)} rules, "
    f"{len(flag_alerts)} alerts on should-flag.md, 0 on should-pass.md"
)

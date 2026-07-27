#!/usr/bin/env python3
"""Assertions for the deslop rule suite. Driven by tests/run.sh, which writes
Vale's JSON output to the path in VALE_REPORT."""

import json
import os
import re
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


data = json.loads(Path(os.environ["VALE_REPORT"]).read_text())
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

# ---------------------------------------------------------------- 3. every fixture line fires
# The "no dead rules" check above is satisfied as soon as one token in a rule
# matches, so a phrase whose inflections were never spelled out can sit in the
# fixture unflagged, hidden behind another tell on the same line. This requires
# every prose line to carry its own weight. Headings and HTML comments are the
# only exemptions.
checks_run += 1
flagged_lines = {a["Line"] for a in flag_alerts}
in_comment = False
for lineno, raw in enumerate((TESTS / "should-flag.md").read_text().splitlines(), 1):
    line = raw.strip()
    if in_comment:
        if "-->" in line:
            in_comment = False
        continue
    if line.startswith("<!--"):
        in_comment = "-->" not in line
        continue
    if not line or line.startswith("#"):
        continue
    if lineno not in flagged_lines:
        fail(
            "silent fixture",
            f"should-flag.md:{lineno} produced no alert: {line!r}. "
            f"Either no rule covers it (check inflections) or it belongs in "
            f"should-pass.md.",
        )

# ---------------------------------------------------------------- 4. expected pairs
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

# ---------------------------------------------------------------- 5. every token is exercised
# Line-level coverage is not enough: several tells can share one fixture line, so
# a token that stops matching stays hidden behind its neighbours. This walks every
# token in every rule and requires each one to match some fixture line on its own.
# Vale wraps `tokens` and `swap` keys in \b...\b and concatenates `raw` entries;
# both are reproduced here so the patterns are tested as Vale compiles them.
checks_run += 1
try:
    import yaml
except ImportError:
    fail("token coverage", "PyYAML is not installed; cannot audit token coverage")
    yaml = None

if yaml is not None:
    in_comment = False
    prose = []
    for raw in (TESTS / "should-flag.md").read_text().splitlines():
        line = raw.strip()
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.startswith("<!--"):
            in_comment = "-->" not in line
            continue
        if line and not line.startswith("#"):
            prose.append(line)
    fixture_text = "\n".join(prose)

    for path in sorted(STYLE_DIR.glob("*.yml")):
        spec = yaml.safe_load(path.read_text())
        if spec.get("extends") == "occurrence":
            continue  # single token; the dead-rule check already covers it
        flags = re.IGNORECASE if spec.get("ignorecase") else 0
        patterns = [(t, True) for t in spec.get("tokens", [])]
        patterns += [(k, True) for k in spec.get("swap", {})]
        if spec.get("raw"):
            patterns.append(("".join(spec["raw"]), False))
        for pattern, wrapped in patterns:
            compiled = rf"\b(?:{pattern})\b" if wrapped else pattern
            try:
                found = re.search(compiled, fixture_text, flags)
            except re.error as exc:
                fail("bad pattern", f"Deslop.{path.stem}: {pattern!r} does not compile ({exc})")
                continue
            if not found:
                fail(
                    "uncovered token",
                    f"Deslop.{path.stem}: {pattern!r} matches nothing in should-flag.md. "
                    f"Add a fixture line for it, on its own line.",
                )

# ---------------------------------------------------------------- 6. no double-flagging
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

# ---------------------------------------------------------------- 7. package completeness
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
        zf.extractall(tmp / "styles")

    # Compare exact archive paths, not basenames: a file that slipped into a
    # nested directory would still be "present" by basename while `vale sync`
    # laid it down somewhere Vale never reads.
    expected_paths = {f"Deslop/{name}" for name in on_disk}
    missing = expected_paths - set(names)
    if missing:
        fail("packaging", f"release zip is missing {sorted(missing)}")
    if "Deslop/meta.json" not in names:
        found = [n for n in names if n.endswith("meta.json")] or "nothing"
        fail(
            "packaging",
            f"package metadata must be at exactly 'Deslop/meta.json' (found {found}); "
            "`vale sync` will reject the package otherwise",
        )

    # Every entry must sit directly under a top-level `Deslop/` directory,
    # spelled exactly that way — `BasedOnStyles = Deslop` is case-sensitive on
    # Linux runners, and a deeper nesting is not read at all.
    misplaced = sorted(n for n in names if len(n.split("/")) != 2 or not n.startswith("Deslop/"))
    if misplaced:
        fail("packaging", f"every zip entry must be 'Deslop/<file>', found {misplaced}")

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

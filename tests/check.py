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
        flags = (re.IGNORECASE if spec.get("ignorecase") else 0) | re.MULTILINE
        patterns = [(t, True) for t in spec.get("tokens", [])]
        patterns += [(k, True) for k in spec.get("swap", {})]
        if spec.get("raw"):
            patterns.append(("".join(spec["raw"]), False))
        # `occurrence` rules carry a single `token`, used verbatim (no \b wrapping).
        # Skipping them here would leave their alternations unaudited below.
        if spec.get("token"):
            patterns.append((spec["token"], False))
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

# ---------------------------------------------------------------- 6. every alternation branch is exercised
# Token coverage is satisfied by any one form, so `supercharg(?:e|es|ed|ing)`
# passes on `supercharge` alone and a later edit could drop `ed|ing` unnoticed.
# This pins each branch of each alternation to a fixture line of its own.
checks_run += 1


def pinned_variants(pattern):
    """Yield (variant, branch) with one top-level alternation group pinned."""
    variants, i = [], 0
    while i < len(pattern):
        if pattern[i] == "(":
            depth, j = 1, i + 1
            while j < len(pattern) and depth:
                if pattern[j] == "\\":
                    j += 2
                    continue
                depth += (pattern[j] == "(") - (pattern[j] == ")")
                j += 1
            inner = pattern[i + 1 : j - 1]
            body = inner[2:] if inner.startswith("?:") else inner
            alts, d, cur = [], 0, ""
            for ch in body:
                if ch == "(":
                    d += 1
                elif ch == ")":
                    d -= 1
                if ch == "|" and d == 0:
                    alts.append(cur)
                    cur = ""
                else:
                    cur += ch
            alts.append(cur)
            if len(alts) > 1:
                for alt in alts:
                    variants.append((pattern[:i] + "(?:" + alt + ")" + pattern[j:], alt))
            i = j
            continue
        i += 1
    return variants


if yaml is not None:
    for path in sorted(STYLE_DIR.glob("*.yml")):
        spec = yaml.safe_load(path.read_text())
        flags = (re.IGNORECASE if spec.get("ignorecase") else 0) | re.MULTILINE
        patterns = [(t, True) for t in spec.get("tokens", [])]
        patterns += [(k, True) for k in spec.get("swap", {})]
        if spec.get("token"):
            patterns.append((spec["token"], False))
        for pattern, wrapped in patterns:
            for variant, branch in pinned_variants(pattern):
                probe = rf"\b(?:{variant})\b" if wrapped else variant
                try:
                    hit = re.search(probe, fixture_text, flags)
                except re.error:
                    continue  # the whole-token check already reported this
                if not hit:
                    fail(
                        "unexercised branch",
                        f"Deslop.{path.stem}: branch {branch!r} of {pattern!r} "
                        f"matches no fixture line. Give it one.",
                    )

# ---------------------------------------------------------------- 7. occurrence tokens keep their branches
# Branch coverage above proves a branch is exercised; it cannot notice a branch
# being deleted, because a smaller alternation simply has less to check. For
# `tokens` rules deletion is caught anyway -- each tell has its own fixture line,
# which goes silent. An `occurrence` rule fires on density across the whole file,
# so one line covers many branches and dropping one changes nothing observable.
# Those branch lists are pinned explicitly.
checks_run += 1
if yaml is not None:
    occurrence_tokens = {}
    for path in sorted(STYLE_DIR.glob("*.yml")):
        spec = yaml.safe_load(path.read_text())
        if spec.get("token"):
            occurrence_tokens[f"Deslop.{path.stem}"] = spec["token"]

    for lineno, raw in enumerate((TESTS / "expected-branches.tsv").read_text().splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            rule, branch = line.split("\t", 1)
        except ValueError:
            fail("expected-branches.tsv", f"line {lineno} is not <rule>TAB<branch>: {raw!r}")
            continue
        token = occurrence_tokens.get(rule)
        if token is None:
            fail("expected-branches.tsv", f"line {lineno}: {rule} is not an occurrence rule")
        elif branch not in token:
            fail(
                "removed branch",
                f"{rule} no longer contains {branch!r}. Occurrence rules fire on "
                f"density, so nothing else in the suite would notice.",
            )

# ---------------------------------------------------------------- 8. no double-flagging
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

# ---------------------------------------------------------------- 9. package installs and works
# The published v0.1.0 zip shipped 13 of 17 rules for two months because nothing
# compared the archive against the tree. This builds the release zip, installs it
# through `vale sync` exactly as a consumer does, and lints through the installed
# copy. `Packages` accepts a local path, so this needs no network and can gate a
# release before the artifact exists.
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

    # Compare exact archive paths, not basenames: a file that slipped into a
    # nested directory would still be "present" by basename while `vale sync`
    # laid it down somewhere Vale never reads.
    expected_paths = {f"Deslop/{name}" for name in on_disk}
    missing = expected_paths - set(names)
    if missing:
        fail("packaging", f"release zip is missing {sorted(missing)}")

    # Every entry must sit directly under a top-level `Deslop/` directory,
    # spelled exactly that way — `BasedOnStyles = Deslop` is case-sensitive on
    # Linux runners, and a deeper nesting is not read at all.
    misplaced = sorted(n for n in names if len(n.split("/")) != 2 or not n.startswith("Deslop/"))
    if misplaced:
        fail("packaging", f"every zip entry must be 'Deslop/<file>', found {misplaced}")

    # `vale sync` does NOT validate meta.json — a malformed one syncs happily and
    # only bites later. Checked here explicitly rather than assumed.
    if "Deslop/meta.json" not in names:
        found = [n for n in names if n.endswith("meta.json")] or "nothing"
        fail("packaging", f"metadata must be at exactly 'Deslop/meta.json' (found {found})")
    else:
        with zipfile.ZipFile(zip_path) as zf:
            try:
                meta = json.loads(zf.read("Deslop/meta.json"))
            except json.JSONDecodeError as exc:
                meta = None
                fail("packaging", f"Deslop/meta.json is not valid JSON ({exc})")
        if meta is not None and "vale_version" not in meta:
            fail("packaging", "Deslop/meta.json has no 'vale_version' key")

    # Install it the way a consumer does, then lint through the installed copy.
    vale_bin = os.environ.get("VALE_BIN")
    if not vale_bin:
        fail("packaging", "VALE_BIN not set; cannot verify the built package")
    else:
        styles_dir = tmp / "styles"
        styles_dir.mkdir(exist_ok=True)  # vale sync stages to a temp path without it
        cfg = tmp / ".vale.ini"
        cfg.write_text(
            f"StylesPath = {styles_dir}\n"
            "MinAlertLevel = suggestion\n"
            f"Packages = {zip_path}\n\n"
            "[*.md]\nBasedOnStyles = Deslop\n"
        )
        sync = subprocess.run(
            [vale_bin, "--config", str(cfg), "sync"], capture_output=True, text=True
        )
        if sync.returncode != 0:
            fail("packaging", f"`vale sync` rejected the package: {sync.stderr.strip()}")
        installed = {p.name for p in (styles_dir / "Deslop").glob("*")} if (styles_dir / "Deslop").is_dir() else set()
        if on_disk - installed:
            fail("packaging", f"`vale sync` did not install {sorted(on_disk - installed)}")

        proc = subprocess.run(
            [vale_bin, "--config", str(cfg), "--output=JSON",
             str(TESTS / "should-flag.md")],
            capture_output=True, text=True,
        )
        try:
            repacked = json.loads(proc.stdout or "{}")
        except json.JSONDecodeError:
            repacked = {}
            fail("packaging", f"vale failed against installed package: {proc.stderr.strip()}")
        repacked_alerts = alerts_for(repacked, "should-flag.md")
        if not repacked_alerts:
            fail(
                "packaging",
                "the installed package produced no alerts — consumers would "
                "install it and silently lint nothing",
            )
        repacked_rules = {a["Check"].split(".", 1)[1] for a in repacked_alerts}
        for dead in sorted(rule_files - repacked_rules):
            fail("packaging", f"Deslop.{dead} does not fire from the installed copy")

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

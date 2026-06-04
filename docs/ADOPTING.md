# Adopting deslop

Copy-paste integration guide. All steps are self-contained.

## 1. Add `.vale.ini`

```ini
StylesPath = styles
MinAlertLevel = suggestion
Packages = https://github.com/JMill/deslop/releases/latest/download/Deslop.zip

[*.{md,mdx}]
BasedOnStyles = Deslop
```

## 2. Run locally

```sh
mkdir -p styles
vale sync
vale "**/*.md"
```

`mkdir -p styles` must come before `vale sync`. Vale needs the directory to exist
or it stages downloads to a temporary path and leaves `StylesPath` empty.

## 3. Add CI (GitHub Actions)

Create `.github/workflows/vale.yml`:

```yaml
name: Vale

on:
  pull_request:
    paths:
      - '**/*.md'

jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Prepare styles dir
        run: mkdir -p styles

      - name: Run Vale
        uses: errata-ai/vale-action@v2
        with:
          files: '**/*.md'
          reporter: github-pr-check
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

This uses `errata-ai/vale-action@v2`, the current stable major (v2.1.2 as of May 2026).
The action reads your `.vale.ini`, runs `vale sync` to fetch the package, and
posts findings as PR check annotations.

## 4. Customize

**Disable a rule** under the file-type section:

```ini
[*.{md,mdx}]
BasedOnStyles = Deslop
Deslop.SlopVocab = NO
```

**Change a level** (raise to `error`, lower to `suggestion`):

```ini
[*.{md,mdx}]
BasedOnStyles = Deslop
Deslop.HollowIntensifier = error
```

**Raise the floor** so only errors surface in CI:

```ini
MinAlertLevel = error
```

## 5. Add a project-specific banned phrase

Create `styles/Repo/MyRule.yml` (Vale `existence` rule):

```yaml
extends: existence
message: "Avoid '%s' in this codebase."
level: warning
tokens:
  - your banned phrase here
  - another phrase
```

Then add `Repo` to `BasedOnStyles`:

```ini
[*.{md,mdx}]
BasedOnStyles = Deslop, Repo
```

Vale loads both style directories. `Repo` rules sit alongside Deslop rules with
no conflicts unless you reuse the same rule name.

## 6. Running alongside an existing linter

If your repo already runs a prose or slop linter (for example a TypeScript
script that checks for banned terms), you can run both in CI without conflict.
Over time, migrate rules into deslop `existence` files and delete the
equivalent checks from the other tool.

Example parallel CI step (add after your existing linter step):

```yaml
      - name: Prepare styles dir
        run: mkdir -p styles

      - name: Run Vale (deslop)
        uses: errata-ai/vale-action@v2
        with:
          files: '**/*.md'
          reporter: github-pr-check
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

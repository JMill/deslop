# deslop — Agent Guide

deslop is a [Vale](https://vale.sh) style package that flags AI-slop in prose: the stock
phrases, hedges, and structural tics that mark machine-written text. It ships as a release
asset (`Deslop.zip`) that other repos consume through Vale's `Packages` mechanism.

## Layout

| Path | What it is |
| --- | --- |
| `styles/Deslop/*.yml` | The rules. One file per tell family (e.g. `SlopVocab.yml`, `HollowCloser.yml`). Each is a Vale rule extending `existence`, `substitution`, or `occurrence`. |
| `styles/Deslop/meta.json` | Package metadata Vale reads on `vale sync`. |
| `.vale.ini` | Lints this repo's own prose. `Deslop` only, no `Vale` base style. Consumers use a different `.vale.ini` (see below). |
| `docs/ADOPTING.md` | Copy-paste integration guide: `.vale.ini`, CI, customizing, composing private styles. |
| `.github/workflows/vale.yml` | Lints this repo's `*.md` on PRs. |
| `.github/workflows/release.yml` | On a `v*` tag, builds `Deslop.zip` and publishes a GitHub release. |
| `README.md` | Human-facing overview and the full rule table. |

## How to use it (consuming the package)

A downstream repo adds a `.vale.ini`:

```ini
StylesPath = styles
MinAlertLevel = suggestion
Packages = https://github.com/JMill/deslop/releases/latest/download/Deslop.zip

[*.{md,mdx}]
BasedOnStyles = Deslop
```

Then `mkdir -p styles && vale sync && vale "**/*.md"`. The `mkdir -p styles` must come before
`vale sync` or Vale stages to a temp path and leaves `StylesPath` empty. Full guide:
[docs/ADOPTING.md](docs/ADOPTING.md).

## How to extend it (add a rule)

The common change is adding a tell. Create one file under `styles/Deslop/`. Most rules extend
`existence` (flag any match) and take a list of regex `tokens`:

```yaml
# styles/Deslop/SlopVocab.yml (excerpt)
extends: existence
message: "'%s' is an AI-slop tell. Cut it or say the thing plainly."
level: warning
ignorecase: true
tokens:
  - 'delv(?:e|ing)'
  - 'plethora'
  - 'when\s+it\s+comes\s+to'
```

Use `occurrence` for density caps (cap how often a `token` appears in a `scope`, as
`HollowIntensifier.yml` does) and `substitution` for "prefer X over Y" swaps. A new file is
picked up automatically once its name is added to `BasedOnStyles`; the rule name is the file
stem (`Deslop.SlopVocab`). See the [Vale styles docs](https://vale.sh/docs/topics/styles/).

Keep this repo public-safe. Private or brand-specific phrasing does not belong here. Consumers
add those through composition: a second style directory listed alongside `Deslop` in
`BasedOnStyles`. The mechanism is documented in [docs/ADOPTING.md](docs/ADOPTING.md) section 7.

## Commands

```sh
# Lint this repo's prose (uses the repo .vale.ini)
vale --config .vale.ini AGENTS.md
vale "**/*.md"

# Build the release asset locally to test a rule change end to end
cd styles && zip -rq /tmp/Deslop.zip Deslop
```

Releases are cut by pushing a `v*` tag. The release workflow builds `Deslop.zip` from
`styles/Deslop` and attaches it to the GitHub release. Consumers pinned to
`releases/latest/download/Deslop.zip` pick it up on their next `vale sync`.

## Conventions

- One tell family per file. Name the file for what it catches.
- `error` for the worst offenders, `warning` for most tells, `suggestion` for density signals.
- Messages name the fix, not just the problem. Point at a plainer rewrite.
- Every example slop word in docs is backtick-quoted so deslop does not flag its own guide.

## Where this sits

deslop is the public, generic anti-slop floor: mechanical line-level tells any prose can hit.
It is one input to the private [writers-room](https://github.com/JMill/writers-room) pipeline,
which runs deslop as a deterministic pre-pass and layers judgment-level critics on top.
sam-bot is the front door that routes work to capabilities like that pipeline. deslop itself
knows nothing about either; it is a standalone Vale package.

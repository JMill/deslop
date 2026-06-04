# deslop

A [Vale](https://vale.sh) style package that flags AI-slop in prose. It catches the
phrases, hedges, and structural tics that mark machine-generated text, then points
you at a plainer rewrite.

## What it checks

Each rule family lives in its own file under `styles/Deslop/`:

| File | Catches |
| --- | --- |
| `SlopVocab.yml` | Stock words: `delve`, `tapestry`, `plethora`, `myriad`, `multifaceted`, `in today's world`, and more |
| `CorporateCliche.yml` | `synergy`, `best-in-class`, `cutting-edge`, `holistic`, `transformative` |
| `NotJustScaffold.yml` | The `not just X but Y` contrast scaffold |
| `AntitheticalPair.yml` | `It's not X. It's Y.` sentence pairs |
| `VagueAttribution.yml` | `experts say`, `research shows`, `it is widely believed` |
| `HollowCloser.yml` | `in conclusion`, `to sum up`, `at the end of the day` |
| `FillerTransition.yml` | `Having examined...`, `it is also worth noting` |
| `FalseWarmth.yml` | `fascinating space`, `poised to`, `groundbreaking` |
| `FalseBalance.yml` | `both have merit`, `remains to be seen` |
| `HedgeCascade.yml` | Stacked qualifiers: `could potentially`, `may be able to` |
| `EmDashOveruse.yml` | More than one em-dash per paragraph |
| `ConjunctiveAdverbOpener.yml` | Repeated `Moreover / Furthermore / Additionally` openers |
| `HollowIntensifier.yml` | A pile-up of `incredibly / extremely / very / really` |

Levels map to Vale severities: `error` is red, `warning` is yellow, `suggestion` is green.
Most tells are warnings. Intensifier density is a suggestion.

## Install

You need the Vale CLI (version 3.0 or later). See the
[Vale install guide](https://vale.sh/docs/vale-cli/installation/).

### Option A: vale sync

Add the package to your own `.vale.ini` and let Vale fetch it:

```ini
StylesPath = styles
MinAlertLevel = suggestion

[*.{md,mdx}]
BasedOnStyles = Vale, Deslop
```

Then run:

```sh
vale sync
vale README.md
```

### Option B: vendor the folder

Copy `styles/Deslop/` into your repo's `StylesPath` and reference `Deslop` in
`BasedOnStyles`. This repo ships a working `.vale.ini` you can copy as a starting
point.

### Option C: GitHub Action

The included `.github/workflows/vale.yml` runs
[`errata-ai/vale-action`](https://github.com/errata-ai/vale-action) on every pull
request that touches a Markdown file. Drop it into your repo and Vale posts findings
as PR checks.

## Customize

**Allow a word in one repo.** Add it to a vocabulary accept list. Create
`styles/config/vocabularies/Deslop/accept.txt` in your repo and list terms one per
line. Accepted terms stop being flagged.

**Disable a rule.** Set it to `NO` in your `.vale.ini`:

```ini
[*.md]
BasedOnStyles = Deslop
Deslop.FalseBalance = NO
```

**Change a level.** Promote or demote any rule:

```ini
Deslop.SlopVocab = error
```

**Add your own tells.** Copy any rule file as a template. The `existence` rules take
a list of regex `tokens`; the `occurrence` rules cap how often a `token` may appear
in a `scope`. See the [Vale styles docs](https://vale.sh/docs/topics/styles/).

## Prior art

- [slopless](https://github.com/agent-quality-controls/slopless), a related effort to
  detect machine-written prose.
- [`@textlint-ja/textlint-rule-preset-ai-writing`](https://github.com/textlint-ja/textlint-rule-preset-ai-writing),
  a textlint preset targeting the same class of tells.

## License

MIT. See [LICENSE](LICENSE).

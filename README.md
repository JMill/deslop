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

Add a `.vale.ini` to your repo:

```ini
StylesPath = styles
MinAlertLevel = suggestion
Packages = https://github.com/JMill/deslop/releases/latest/download/Deslop.zip

[*.{md,mdx}]
BasedOnStyles = Deslop
```

Then run:

```sh
mkdir -p styles
vale sync
vale "**/*.md"
```

`mkdir -p styles` must come before `vale sync`: Vale needs the directory to exist or it
stages files to a temporary path and leaves your `StylesPath` empty.

`vale sync` downloads `Deslop.zip` and extracts it into `styles/Deslop/`. The release
asset is named `Deslop.zip` (capital D) so the extracted folder matches `BasedOnStyles = Deslop`
on case-sensitive Linux CI.

For a full copy-paste guide including CI setup, see [docs/ADOPTING.md](docs/ADOPTING.md).

## Customize

**Disable a rule.** Set it to `NO` under the file-type section:

```ini
[*.{md,mdx}]
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

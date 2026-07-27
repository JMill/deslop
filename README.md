# deslop

A [Vale](https://vale.sh) style package that flags AI-slop in prose. It catches the
phrases, hedges, and structural tics that mark machine-generated text, then points
you at a plainer rewrite.

## What it checks

Each rule family lives in its own file under `styles/Deslop/`:

| File | Catches |
| --- | --- |
| `SlopVocab.yml` | Stock words and phrases with no one-word swap: `delve`, `tapestry`, `plethora`, `leverage`, `seamless`, `harness the power`, `a testament to`, and more |
| `Substitutions.yml` | One-to-one swaps: `robust`->`strong`, `crucial`->`important`, `comprehend`->`understand`, `utilize`->`use` |
| `MarketingVerb.yml` | Launch-copy verbs: `revolutionize`, `supercharge`, `empower`, `streamline`, `showcase`, `unparalleled` |
| `CorporateCliche.yml` | `synergy`, `best-in-class`, `cutting-edge`, `holistic`, `transformative`, `mission-critical` |
| `CorporateMetaphor.yml` | `north star`, `boil the ocean`, `low-hanging fruit`, `circle back`, `touch base`, figurative `double-click` |
| `AssistantOpener.yml` | Chatbot throat-clearing: `Great question!`, `I'd be happy to help`, `Let's dive in`, `Buckle up` |
| `AssistantCloser.yml` | Chatbot sign-offs: `I hope this helps`, `Let me know if you have questions`, `Is there anything else` |
| `Hedging.yml` | `honestly`, `I think`, `arguably`, `perhaps`, `somewhat`, `to some extent` |
| `OpenerCliche.yml` | Stock openers: `In today's world`, `In an era of`, `In a world where` |
| `NotJustScaffold.yml` | The `not just X but Y` contrast scaffold |
| `AntitheticalPair.yml` | `It's not X. It's Y.` sentence pairs |
| `VagueAttribution.yml` | `experts say`, `research shows`, `many believe`, `it is widely believed` |
| `HollowCloser.yml` | `in conclusion`, `to sum up`, `at the end of the day`, `the bottom line is` |
| `FillerTransition.yml` | `Having examined...`, `with that said`, `first and foremost` |
| `FalseWarmth.yml` | `fascinating space`, `poised to`, `groundbreaking`, `bodes well` |
| `FalseBalance.yml` | `both have merit`, `remains to be seen`, `only time will tell` |
| `HedgeCascade.yml` | Stacked qualifiers: `could potentially`, `may be able to`, `might possibly` |
| `EmDashOveruse.yml` | More than one em-dash per paragraph |
| `ConjunctiveAdverbOpener.yml` | Repeated `Moreover / Furthermore / Additionally` openers |
| `HollowIntensifier.yml` | A pile-up of `incredibly / extremely / very / really` |

Levels map to Vale severities: `error` is red, `warning` is yellow, `suggestion` is green.
Everything here ships as a warning except intensifier density, which is a suggestion.
Nothing ships as an error: which tells are bad enough to block a build is your call,
not the package's, so promote the ones you care about (see [Customize](#customize)).

Each tell has exactly one home. If a word appears in `Substitutions.yml` it will not
also appear in `SlopVocab.yml`, so no phrase reports twice. The test suite enforces this.

Tokens spell out their inflections, so `leveraging`, `leverages`, and `leveraged` are
caught alongside `leverage`. Several tokens are deliberately narrowed to avoid firing on
ordinary technical prose: `realm of` rather than bare `realm` (so Realm the database is
safe), `landscape of` rather than bare `landscape` (so landscape orientation is safe),
`harness the power` rather than `harness the` (so a test harness is safe).

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

### Pin a version

The `latest` URL above tracks whatever was released most recently, so a new rule can
start failing your build without anything changing on your side. To decide when that
happens, point at a tag instead:

```ini
Packages = https://github.com/JMill/deslop/releases/download/v0.2.0/Deslop.zip
```

Vale caches by URL, so switching to a pinned tag also makes `vale sync` reproducible.
See [CHANGELOG.md](CHANGELOG.md) for what moves between versions.

For a full copy-paste guide including CI setup, see [docs/ADOPTING.md](docs/ADOPTING.md).

For the craft reference behind these rules, the principle, the tests, the hard rules, and
the blocklist with plainer swaps, see [docs/ANTI-SLOP-STYLE-GUIDE.md](docs/ANTI-SLOP-STYLE-GUIDE.md).

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

**Exempt a word you actually use.** If a rule fires on a product name or a term of art,
add it to a Vale vocabulary rather than turning the whole rule off:

```sh
mkdir -p styles/config/vocabularies/Base
printf 'Kubernetes\nRealm\n' > styles/config/vocabularies/Base/accept.txt
```

```ini
Vocab = Base
```

Accepted terms are filtered out of every rule's matches. Entries are case-sensitive, so
`Realm` exempts the product without exempting `realm of` in prose.

**Add your own tells.** Copy any rule file as a template. The `existence` rules take
a list of regex `tokens`; the `occurrence` rules cap how often a `token` may appear
in a `scope`. See the [Vale styles docs](https://vale.sh/docs/topics/styles/) and the
rule-authoring gotchas in [AGENTS.md](AGENTS.md#writing-a-rule).

## Tests

```sh
tests/run.sh
```

The suite checks that no rule is silently dead, that `tests/should-pass.md` (ordinary
technical prose) produces zero alerts, that no two rules flag overlapping text, and that
the built `Deslop.zip` lints correctly once extracted. Add a fixture line whenever you
add a tell.

## Prior art

- [slopless](https://github.com/agent-quality-controls/slopless), a related effort to
  detect machine-written prose.
- [`@textlint-ja/textlint-rule-preset-ai-writing`](https://github.com/textlint-ja/textlint-rule-preset-ai-writing),
  a textlint preset targeting the same class of tells.

## License

MIT. See [LICENSE](LICENSE).

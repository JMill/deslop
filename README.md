# deslop

A [Vale](https://vale.sh) style package that flags AI-slop in prose. It catches the
phrases, hedges, and structural tics that mark machine-generated text, then points
you at a plainer rewrite.

## What it checks

Each rule family lives in its own file under `styles/Deslop/`:

| File | Catches |
| --- | --- |
| `SlopVocab.yml` | Stock words and phrases with no one-word swap: `delve`, `tapestry`, `plethora`, `leverage`, `seamless`, `harness the power`, `a testament to`, `the right move is to`, and more |
| `Substitutions.yml` | One-to-one swaps: `robust`->`strong`, `crucial`->`important`, `comprehend`->`understand`, `utilize`->`use` |
| `MarketingVerb.yml` | Launch-copy verbs: `revolutionize`, `supercharge`, `streamline your`, `showcase the`, `unparalleled` |
| `ContestedWord.yml` | Broad match at `suggestion`, for words with a real domain sense: `empower` (governance), `load-bearing` (structural), `priors` (Bayesian) |
| `PerformedCandor.yml` | Announced sincerity: `To be honest`, `Frankly`, `Let's be honest`, `I'll be blunt`, `Truth be told`, `the honest answer is` |
| `CorporateCliche.yml` | `synergy`, `best-in-class`, `cutting-edge`, `holistic`, `transformative`, `mission-critical` |
| `CorporateMetaphor.yml` | `north star`, `boil the ocean`, `low-hanging fruit`, `circle back`, `touch base`, figurative `double-click` |
| `AssistantOpener.yml` | Chatbot throat-clearing: `Great question!`, `I'd be happy to help`, `Let's dive in`, `Buckle up`, `Here's the thing/catch/trade-off`, `Let's unpack this` |
| `AssistantCloser.yml` | Chatbot sign-offs: `I hope this helps`, `Let me know if you have questions`, `Is there anything else` |
| `Hedging.yml` | `I think`, `arguably`, `perhaps`, `somewhat`, `to some extent` |
| `OpenerCliche.yml` | Stock openers: `In today's world`, `In an era of`, `In a world where` |
| `NotJustScaffold.yml` | The `not just X but Y` and `not because X, but because Y` contrast scaffolds |
| `AntitheticalPair.yml` | `It's not X. It's Y.` sentence pairs, and `a feature, not a bug` |
| `VagueAttribution.yml` | `experts say`, `research shows`, `many believe`, `it is widely believed` |
| `HollowCloser.yml` | `in conclusion`, `to sum up`, `at the end of the day`, `the bottom line is` |
| `FillerTransition.yml` | `Having examined...`, `with that said`, `first and foremost`, `and more importantly` |
| `FalseWarmth.yml` | `fascinating space`, `poised to`, `groundbreaking`, `bodes well` |
| `FalseBalance.yml` | `both have merit`, `remains to be seen`, `only time will tell`, `reasonable people disagree`, `both things are true` |
| `HedgeCascade.yml` | Stacked qualifiers: `could potentially`, `may be able to`, `might possibly` |
| `EmDashOveruse.yml` | More than one em-dash per paragraph |
| `ConjunctiveAdverbOpener.yml` | Repeated `Moreover / Furthermore / Additionally` openers |
| `HollowIntensifier.yml` | A pile-up of `incredibly / extremely / very / really / genuinely / strikingly` |
| `RealityAdverb.yml` | Two or more of `actually / basically / literally / in fact` in one paragraph |

The rules below catch the newer register — the "thoughtful essayist" voice that
reads like careful reasoning:

| File | Catches |
| --- | --- |
| `BorrowedRigor.yml` | Economics and reliability vocabulary as decoration: `doing the real work`, `first-order concern`, `an order of magnitude harder`, `the binding constraint`, `forcing function`, `strictly better`, `compounding advantage` |
| `CalibrationTheatre.yml` | Confidence scored as ornament: `Epistemic status`, `I'm fairly confident`, `I could be wrong here`, `I don't want to overstate this` |
| `AnnouncedNoteworthiness.yml` | `it's worth noting`, `worth stating plainly`, `worth sitting with`, `I should flag that`, `why this matters` |
| `WithheldPayoff.yml` | Promised reveals: `where it gets interesting`, `what nobody talks about`, `the quiet part`, `the uncomfortable truth` |
| `FalseDepthReframe.yml` | `the real question is`, `the question isn't whether X`, `the real problem is` — relocating the question instead of answering it |
| `FramingOffer.yml` | `one way to think about this is`, `the right way to think about it`, `think of it as`, `to make this concrete` |
| `AnnouncedSteelman.yml` | `let me steelman that`, `the strongest version of the argument`, `the most charitable reading` |
| `Restatement.yml` | `in other words`, `put another way`, `which is to say` — restatement standing in for reasoning |
| `CadenceFragment.yml` | `That's the whole point.`, `and that's fine`, `Full stop.` |
| `ColonDrumroll.yml` | `The answer is simple:` — announcing the answer instead of giving it |
| `LocativeClosure.yml` | `where the real work happens`, `where the magic lives` |

Levels map to Vale severities: `error` is red, `warning` is yellow, `suggestion` is green.
Everything here ships as a warning except `ContestedWord`, `HollowIntensifier`, and
`RealityAdverb`, which are suggestions — the first because those words have a real
domain sense, the other two because they measure density and a single use is fine.
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
Packages = https://github.com/JMill/deslop/releases/download/v0.3.0/Deslop.zip
```

Vale caches by URL, so switching to a pinned tag also makes `vale sync` reproducible.
See [CHANGELOG.md](CHANGELOG.md) for what moves between versions.

### Upgrading from an earlier version

If you have synced deslop before, Vale may still hold the old package in its shared
styles directory, and that copy shadows the one `vale sync` just downloaded. The symptom
is confusing: rules you removed keep firing, and a phrase can be reported twice by two
different rules.

Clear the stale copy once, then sync again:

```sh
rm -rf styles/Deslop                                           # your project's copy
rm -rf "$HOME/Library/Application Support/vale/styles/Deslop"  # macOS shared copy
rm -rf "$HOME/.local/share/vale/styles/Deslop"                 # Linux shared copy
vale sync
```

Confirm you got the whole package — v0.3.0 ships 34 rule files:

```sh
ls styles/Deslop/*.yml | wc -l
```

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

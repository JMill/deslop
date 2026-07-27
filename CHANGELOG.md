# Changelog

Consumers pointed at `releases/latest/download/Deslop.zip` pick up each release on their
next `vale sync`. Pin a tag instead if you want to choose when that happens — see
[README](README.md#pin-a-version).

## Unreleased

The first release since `v0.1.0`. `v0.1.0` shipped 13 of the 17 rule files that existed in
the repository, so `CorporateMetaphor`, `Hedging`, `OpenerCliche`, and `Substitutions` have
never been in a published package, and `SlopVocab` shipped 29 of its 56 tokens. Installing
this release turns all of those on at once. Expect a larger jump in findings than the
changes below alone suggest.

### Added

- `MarketingVerb.yml`: `revolutionize`, `supercharge`, `turbocharge`, `empower`,
  `streamline`, `showcase`, `unparalleled`, `unrivaled`, `elevate your <noun>`,
  `take it to the next level`, `effortlessly`, `at your fingertips`.
- `AssistantOpener.yml`: `Great question`, `I'd be happy to help`, `Let's dive in`,
  `Let's get started`, `Buckle up`, `Here's the thing`, `You're absolutely right`,
  sentence-initial `Certainly,` / `Absolutely!`.
- `AssistantCloser.yml`: `I hope this helps`, `Let me know if you have questions`,
  `Feel free to reach out`, `Don't hesitate to ask`, `Is there anything else`.
- A test suite (`tests/run.sh`) and a CI job that runs it on every push and PR.
- New tells in existing rules: `mission-critical`, `value-added`, `bleeding-edge`,
  `touch base`, `move the goalposts`, `take it offline`, `only time will tell`,
  `the jury is still out`, `bodes well`, `bright future`, `with that said`,
  `first and foremost`, `last but not least`, `in closing`, `the bottom line is`,
  `many believe`, `some argue`, `data shows`, `in my opinion`, `I believe`,
  and more hedge cascades (`might potentially`, `could possibly`, `can potentially`).

### Fixed

- **Inflected forms are caught.** Vale wraps every token in `\b...\b`, so `leverage` never
  matched `leveraging`, `seamless` never matched `seamlessly`, and `delve` never matched
  `delved`. All token families now spell their inflections out.
- **Verb-headed idioms match their inflections**, including gerunds and irregular
  participles: `navigating the complexities`, `has driven growth`, `have taken it
  offline`, `have drunk from the firehose`, `boded well`. `move the goalposts`, `move the needle`,
  `drive growth`, `circle back`, `touch base`, `boil the ocean`, `run it up the flagpole`,
  `take it offline`, `peel back the onion`, `take it to the next level`, and
  `remains to be seen` only ever matched their base form, which is the least common one in
  running prose. `VagueAttribution` likewise now matches past-tense attribution
  (`experts argued`, `research indicated`, `sources said`).
- **No phrase reports twice.** `robust`, `crucial`, `multifaceted`, `comprehend`,
  `bolster`, `pinpoint`, and `underscore` were in both `SlopVocab.yml` and
  `Substitutions.yml`; `unlock value` was in both `SlopVocab.yml` and
  `CorporateCliche.yml`; the `in today's ...` family was in both `SlopVocab.yml` and
  `OpenerCliche.yml`. Each tell now has exactly one home, enforced by the suite.
- **Fewer false positives on ordinary technical prose.** Bare `swift`, `realm`, `foster`,
  `beacon`, `landscape`, `myriad`, `unlock`, `elevate`, `boast`, `harness the`, and
  `navigate the` all fired on Swift the language, Realm the database, Foster as a name,
  landscape orientation, unlocking a mutex, elevating privileges, and a test harness.
  These are now narrowed to their slop senses (`realm of`, `harness the power`,
  `unlock <noun>`, and so on).
- **`inquiry` removed.** Too common in support and legal writing to carry its weight.
- **The release workflow can actually publish.** It had no `permissions: contents: write`,
  so the default read-only token would have failed the upload. It had also never run — the
  `v0.1.0` asset was uploaded by hand.
- **The release is gated on the suite**, which builds the zip, installs it with
  `vale sync`, and lints through the installed copy. An incomplete or wrongly nested
  archive cannot be published.

- **Typographic apostrophes match.** Rules containing contractions (`don't hesitate`,
  `it's worth noting`, `in today's world`, `let's dive in`, `It's not X. It's Y.`) only
  accepted a plain `'`, so prose that had been through an editor slipped past them.

- **The new assistant and marketing rules no longer fire on ordinary prose.**
  `Let's take a closer look at the query plan`, `Let's explore the two options`,
  `Is there anything else we should test?`, `the showcase app in examples/`,
  `we streamline the build by caching`, and `the migration empowers operators` were all
  flagged. `showcase`, `streamline`, and `empower` now require the possessive that marks
  the marketing register (`streamline your workflow`), `is there anything else` requires
  the offer-of-help that follows it, and `let's explore` / `let's take a look` are gone —
  they are ordinary collaborative writing. Recall on marketing copy is unchanged; recall
  on bare `streamline` / `empower` / `showcase` is deliberately given up for precision.
- **`value-added` no longer flags terms of art.** `value-added tax` and
  `value-added reseller` have precise legal meanings; only the marketing compounds
  (`value-added proposition`, `offering`, `solution`, `experience`) now fire.
- **`great question` no longer fires mid-sentence.** It flagged ordinary prose such as
  `the design raises an interesting question about caching`; it now requires the
  sentence-initial position that makes it throat-clearing.
- **`VagueAttribution` verb forms are spelled out flat.** The nested suffix groups let the
  regex accept combinations that are not English (`critics claims`) while hiding real forms
  inside character classes. `both perspective merit consideration`, `in today world`, and
  `unlock insight` were likewise accepted by stray optional markers.
- **Perfect-form attribution matches.** `research has shown`, `studies have shown`,
  `data has suggested` produced no alert: the auxiliary broke adjacency and the irregular
  participle `shown` was absent.
- **Gerund attribution matches.** `research suggesting`, `data indicating`,
  `experts arguing`, and `critics claiming` slipped past `VagueAttribution`, which only
  covered finite verb forms. `deep dived` likewise slipped past `deep dive`.

### Changed

- `OpenerCliche` is no longer anchored to the start of a sentence: `Companies in today's
  world must adapt` is the same tell mid-sentence.
- This repo's own Vale CI now sets `fail_on_error: true` and `filter_mode: nofilter`.
  Both default to advisory-only behaviour; see [docs/ADOPTING.md](docs/ADOPTING.md).

## v0.1.0 — 2026-06-04

First release.

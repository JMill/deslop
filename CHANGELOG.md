# Changelog

Consumers pointed at `releases/latest/download/Deslop.zip` pick up each release on their
next `vale sync`. Pin a tag instead if you want to choose when that happens — see
[README](README.md#pin-a-version).

## v0.3.0 — 2026-08-12

Flags the newer AI register: the "thoughtful essayist" voice that current models default
into, which sounds like careful reasoning. Candidate tells were vetted adversarially against
a real corpus before shipping; most did not survive, and the rejects are recorded below so
they are not re-proposed.

### Added — the candor family

- **`PerformedCandor.yml`** — announcing sincerity instead of being sincere: `To be honest`,
  `In all honesty`, `the honest answer is`, `Let's be honest`, `I'll be blunt`,
  `If I'm being honest`, `Truth be told`, `Real talk`, `won't sugarcoat it`, and the bare
  adverbs `Honestly` / `Frankly` / `Candidly`.

  The adverbs are **anchored to the start of a sentence**, because each has an ordinary
  manner sense that is not this tell — `State your tolerances honestly`, `practitioners who
  will speak candidly`, `the piece has to be honest about what it validated`. Those now live
  in `should-pass.md`. The rule is `raw` rather than `tokens` because Vale's `\b` wrapping
  breaks an anchored token after `)`, a backtick, or a quote.

- **`load-bearing` in `ContestedWord.yml`**, at `suggestion`. Its figurative sense attaches
  to an open class of abstract nouns (`claim`, `assumption`, `context`, `proof point`,
  `decision`, `logic`, `thesis`, `step`), so enumerating collocations caught 80 of 619 real
  uses. Excluding the literal `load-bearing wall` needs a negative lookahead, and Vale
  ignores lookarounds, ignores `exceptions:` on `existence`, and cannot filter it through a
  multi-word vocabulary entry either. Broad match at `suggestion` is the only mechanism
  left: every use is surfaced, nothing blocks, and a writer describing an actual wall
  moves on.

- **`genuinely` and `strikingly`** join `HollowIntensifier.yml`; **`Crucially`** joins
  `ConjunctiveAdverbOpener.yml`. Both are density rules, so a single use stays silent.

- **`Here's the catch / tension / trade-off`** and **`Let's unpack this`** join
  `AssistantOpener.yml`, which already owned `Here's the thing` — the same construction
  belongs in one home.

### Changed

- **`honestly` moved from `Hedging.yml` to `PerformedCandor.yml`** and is now anchored. It
  is performed candor, not hedging. A copy in both files would double-flag every hit.

### Fixed

- **`tests/run.sh` now refuses to run against a shadowed working tree.** A previously synced
  Deslop in Vale's shared styles directory silently overrides edited rule files while
  brand-new files still load from the tree, so the suite tested a mix of old and new rules
  and reported false positives that were not in the code. This is the consumer trap in
  [README](README.md#upgrading-from-an-earlier-version), turned on the repo itself.

### Added — the essayist register

Eleven more rules covering the "thoughtful essayist" voice. Every token below was generated,
then adversarially vetted against a 51-repo corpus; roughly a third of the candidates were
cut for firing on ordinary technical prose, and the survivors are narrowed to the figurative
sense. deslop goes from 22 rules to 34.

- **`BorrowedRigor.yml`** — economics, optimisation, and reliability vocabulary used as
  decoration: `doing the real work`, `first-order concern`, `an order of magnitude harder`,
  `the delta between`, `necessary but not sufficient`, `asymmetric bet`, `compounding
  advantage`, `conceptual surface area`, `the binding constraint`, `forcing function`,
  `strictly better`, `tail risk here`, `the anatomy of`, `the failure mode here is`.
  Each is narrowed so the technical sense survives — `second-order constraint`,
  `compounding returns`, `reduce the surface area of the API`, and `the grammar of the
  language` all stay silent.
- **`CalibrationTheatre.yml`** — confidence scored as ornament: `Epistemic status`,
  `I'm fairly confident`, `I'm 80% sure`, `I could be wrong here`, `I'm holding this
  loosely`, `I don't want to overstate this`.
- **`AnnouncedNoteworthiness.yml`** — the `worth <X>` family, now in one home:
  `worth stating plainly`, `worth naming`, `worth sitting with`, `worth being precise
  about`, `I should flag that`, `why this matters`.
- **`WithheldPayoff.yml`** — a reveal promised instead of delivered: `where it gets
  interesting`, `what nobody talks about`, `the quiet part`, `the uncomfortable truth`.
- **`FalseDepthReframe.yml`** — relocating the question rather than answering it:
  `the real question is`, `the question isn't whether X`, `the real problem is`.
- **`FramingOffer.yml`**, **`AnnouncedSteelman.yml`**, **`Restatement.yml`**,
  **`CadenceFragment.yml`**, **`ColonDrumroll.yml`**, **`LocativeClosure.yml`**.
- **`RealityAdverb.yml`** — density cap at `max: 1`, so two of `actually` / `basically` /
  `literally` / `in fact` in one paragraph alert and a single use never does.

Existing rules absorbed the members of families they already owned, rather than opening
second homes: `reasonable people disagree` and `both things are true` to `FalseBalance`,
`not because X, but because Y` to `NotJustScaffold`, `a feature, not a bug` to
`AntitheticalPair`, `and more importantly` to `FillerTransition`, `the right move is to`
to `SlopVocab`, `to be clear,` / `to be fair,` / `I want to be careful here` to
`PerformedCandor`, and `priors` to `ContestedWord`.

**`it's worth noting` moved out of `SlopVocab.yml`** into `AnnouncedNoteworthiness.yml`,
so the whole `worth <X>` family shares one home. `important to note` is a different frame
and stays in `SlopVocab`.

### Rejected

Vetted against a real corpus and dropped — each fires on ordinary technical prose, and Vale
offers no narrowing:

- `heavy lifting` (a library genuinely doing the work), `the shape of the problem` (design
  vocabulary), `gesture at` (a literal HCI verb), `in tension with` (statistical sense),
  `non-trivial fraction` (standard unquantified-share hedge), `the crux of`, `worth
  flagging`, `the key insight is`, `the interesting part is`, `the bigger picture`, `the
  real question is`.
- `the shape of` was shipped in `ContestedWord.yml` and then removed before release: it
  matched 374 times across 14,168 files, dominated by the literal machine-learning sense
  (`the shape of the kernel tensor`). Its literal objects are as open a class as its
  figurative ones, so no collocation separates them.
- A stance-adverb density rule (`genuinely`/`admittedly`/`crucially`/…) at `max: 3` fired on
  nothing across 556k blocks; at `max: 1` it fired on legitimate contrast. The words that
  earned a home were redistributed to the density rules that already own their families.

## v0.2.3 — 2026-07-27

### Changed

- **`empower` moved to a new `ContestedWord.yml` at `suggestion` level**, replacing the
  outright ban added in v0.2.2. It matches broadly, so the tell is never missed, but it
  never blocks a build — the word has a real sense in policy and governance writing
  (`legally empowered`, `empowerment as a policy concept`). This is the calibration
  deslop's own consumers already run in their bespoke linters.

## v0.2.2 — 2026-07-27

### Changed

- **`empower` is banned outright** rather than scoped to `empower your/our`. Treated as
  always-marketing, in line with the house voice guide. This fires on legitimate
  policy and governance prose (`the programme empowers participants`); consumers who
  want the narrower reading can set `Deslop.MarketingVerb = NO` and layer their own.

## v0.2.1 — 2026-07-27

### Fixed

- **`leverage` is scoped to its jargon sense.** The bare token flagged `financial
  leverage`, a term of art. It now requires the object that marks the verb sense, so
  `leverage our synergies` and `leveraging the stack` still fire while
  `financial leverage of two to one` is clean.

## v0.2.0 — 2026-07-27

**Upgrading:** if you synced `v0.1.0`, Vale's shared styles directory still holds that
copy and it shadows the new one, so removed rules keep firing and phrases can report
twice. Delete `Deslop` from the shared styles directory and run `vale sync` again. See
[README](README.md#upgrading-from-an-earlier-version).

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

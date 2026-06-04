# Anti-slop style guide

This is the craft reference behind the `deslop` rules. The rules catch surface tells.
This document explains what the tells point at and how to fix the writing under them.

## The principle

Slop is not a word list. Slop is prose with no thinking under it. The text moves the
right shapes around (claims, transitions, summaries) without a mind deciding what is
true and what matters. The word list is how you spot the absence from outside. It is
not what the absence is.

So the fix is never a find-and-replace. If you swap `delve` for `look at` and the
sentence still asserts nothing, you have cleaner slop. The rules buy you a second look
at a spot where thinking tends to go missing. The repair happens in the thought.

## Three layers

Read a draft at three depths.

**Layer 1, lexical.** Single words and short phrases that signal autopilot: `robust`,
`crucial`, `delve`, `tapestry`, `leverage`. Cheap to catch, cheap to fix. The `deslop`
existence and substitution rules live here. Clearing this layer makes the prose plainer
but not better.

**Layer 2, structural.** Shapes that fake reasoning: the `not just X but Y` scaffold,
the `It's not X. It's Y.` pair, the conjunctive-adverb opener, the hollow closer, the
hedge cascade. These read as argument while carrying none. Catching them needs pattern
rules, not word lists.

**Layer 3, the disease.** The two layers above are symptoms. The disease is three
habits:

- Assertion as reasoning. A claim is stated, then restated louder, and the restatement
  is treated as support.
- Missing counterargument. The strongest objection is never named, so the reader cannot
  tell whether the writer beat it or dodged it.
- No position. After many words the text has not committed to anything a reader could
  disagree with.

Layer 3 is invisible to a linter. You find it by reading for it.

## The seven tests

Run a passage through these. Each one targets a layer-3 failure.

1. **Second-layer test.** Does the writing reason about its own claims, or only state
   them? Reasoning examines; assertion repeats.
2. **Load-bearing test.** Take any sentence. If you delete it, does an argument break?
   If nothing breaks, the sentence was decoration.
3. **Deletion test.** Cut every adjective and intensifier. Does the meaning survive? The
   words that change the meaning were doing work; the rest were filler.
4. **Disagreement test.** Can a reasonable reader disagree with the central claim? If no
   one could disagree, you stated nothing.
5. **Counterargument test.** Is the strongest objection named and answered? An argument
   that never meets its objection has not been made.
6. **Specificity test.** Could this sentence be moved to a different essay on a different
   topic unchanged? If it travels that well, it says nothing about this subject.
7. **Provenance test.** For each claim, can you say where it came from? Name the source
   and the affiliation, not `experts say` or `research shows`.

## The hard rules

- Take a position. The reader must be able to disagree.
- Name the strongest counterargument before you answer it.
- Every sentence carries an idea or it gets cut.
- One qualifier, not two. Stacked hedges cancel out.
- Cut the opener and the closer that only announce the shape of the piece.
- Show with the specific instead of asserting with the abstract.
- No em-dash pile-ups. Periods and natural breaks instead.
- Vary how sentences open. Repeated `Moreover` and `Furthermore` mark a list wearing a
  paragraph's clothes.
- Attribute by name. Source and affiliation, every time.

## Blocklist with plainer swaps

The full token set lives in `styles/Deslop/`. A working subset:

| Reach for this | Write this |
| --- | --- |
| `underscore` | show |
| `delve into` | look at |
| `robust` | strong |
| `crucial` | important |
| `pivotal` | key |
| `multifaceted` | complicated |
| `comprehend` | understand |
| `bolster` | strengthen |
| `pinpoint` | identify |
| `utilize` | use |
| `leverage` | use |
| `foster` | build, grow |
| `elevate` | raise, improve |
| `myriad`, `plethora` | many |
| `landscape`, `realm` | name the actual field |

Structural phrases have no one-word swap. Rewrite the sentence so it states the claim:
`not just X but Y` becomes a plain sentence about what the thing is. `It's not X. It's Y.`
folds into one affirmative line. `In today's world` is deleted and the piece opens on its
first real claim.

The swap is the easy half. The hard half is the thought the rules ask you to put back.

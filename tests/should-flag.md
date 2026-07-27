# Fixtures that must produce alerts

Every rule under `styles/Deslop/` has to fire at least once somewhere in this
file, and every pair listed in `expected.tsv` has to be flagged. Keep each tell
in its own paragraph so the double-flag check stays meaningful: two different
rules matching overlapping text is a bug, not a feature.

## SlopVocab, including inflected forms

The team delved into a rich tapestry of options.

He delves, she delved, they are delving.

A plethora of choices and a myriad of tradeoffs.

The vendor boasted about a treasure trove nestled in the docs.

Leveraging the ever-evolving stack in a fast-paced world.

She leverages it; he leveraged it; they leverage it daily.

The design is seamless and the rollout was seamlessly handled.

It is worth noting that this is important to note.

Needless to say, when it comes to that, we are at the forefront.

Unlocking the potential and harnessing the power of the data.

A game-changer that left an indelible mark on a vibrant, bustling market.

The meticulously documented, meticulous approach.

The results underscore the problem.

In the realm of things, the landscape of options shifted.

The competitive landscape changed again.

We foster a culture of collaboration and fostering innovation.

A swift response followed.

A beacon of hope and a pivotal, nuanced, intricate design.

The intricacies matter.

A paradigm shift after the deep dive we embarked on.

The cornerstone of the plan is a stark reminder.

This stands as a testament to the work.

Navigating is fine, but they navigate the complexities daily.

## Substitutions, including inflected forms

The robust design was crucial to us.

Its robustness was never in question.

A multifaceted issue we could not comprehend.

She comprehends it now; he comprehended it later; they are comprehending it.

We bolster the case, she bolsters it, they bolstered it, I am bolstering it.

Pinpoint the cause. She pinpoints it. He pinpointed it. They are pinpointing it.

We utilize it, she utilizes it, he utilized it, they are utilizing it.

Improved utilization followed.

## CorporateCliche

Synergy from a best-in-class, world-class, cutting-edge platform.

A holistic and transformative approach that will drive growth.

Mission-critical and value-added, with bleeding-edge tooling.

## CorporateMetaphor

Our north star is to boil the ocean and grab low-hanging fruit.

Let us circle back and touch base before double-clicking on this.

They moved the goalposts, so run it up the flagpole and take it offline.

Peeling back the onion while drinking from the firehose.

## Hedging

Honestly, I think this is arguably fine.

Perhaps it is somewhat true, to some extent.

In my opinion, I believe it seems that way. I would argue so.

It could be argued otherwise.

## HedgeCascade

This could potentially work and may be able to scale.

It might potentially help and can potentially fail.

We could possibly ship, and it might possibly slip.

That was a bit of a problem, and it could be able to recur.

May potentially apply.

## OpenerCliche

In today's world, things change.

Companies in today's market must adapt.

In an era of change, in the age of tooling, in a world where nothing holds.

## NotJustScaffold

This is not just fast but also cheap.

## AntitheticalPair

It's not a bug. It's a feature.

## VagueAttribution

Experts say the data shows a change, and studies suggest otherwise.

It is widely believed, and it is often said, that many believe this.

Critics argue and sources say some argue the opposite.

Research indicates a change.

## HollowCloser

In conclusion, and in summary, to sum up: all in all, at the end of the day.

In closing, to wrap up, when all is said and done, the bottom line is this.

## FillerTransition

Having examined the data, another important consideration emerged.

With that said, that being said, first and foremost, last but not least.

It goes without saying, and as previously discussed above, we move on.

## FalseWarmth

A fascinating space, poised to deliver groundbreaking, rapidly evolving work.

An exciting time to be here, with a bright future that bodes well.

## FalseBalance

Both have merit, and it remains to be seen; both perspectives merit consideration.

Only time will tell, the jury is still out, and there are valid points on both sides.

## MarketingVerb

Revolutionize and supercharge your stack; turbocharged and empowering.

It streamlines and showcases unparalleled, unrivaled capability.

Elevate your brand and take it to the next level, effortlessly, at your fingertips.

## AssistantOpener

Great question! I'd be happy to help.

Let's dive in and get started. Let's explore. Let's take a closer look.

Buckle up. Here's the thing. You're absolutely right.

Certainly, that works.

## AssistantCloser

I hope this helps. Let me know if you have questions.

Feel free to reach out, and don't hesitate to ask.

If you have any other questions, is there anything else I can do?

## Cross-rule collisions (regression guards)

These sentences each sit on a seam between two rules. Every one of them used to
produce two overlapping alerts. They must now produce non-overlapping alerts, so
the double-flag check in `check.py` is what keeps them honest.

Another crucial consideration emerged.

In today's landscape of tools, the market moved.

It is important to note another important consideration.

I believe experts believe it.

## EmDashOveruse

One dash — two dashes — three dashes — four here.

## ConjunctiveAdverbOpener

Moreover, a point. Furthermore, another. Additionally, a third. Notably, a fourth. Importantly, a fifth.

## HollowIntensifier

Incredibly, extremely, truly, really, very, highly, remarkably, utterly good.

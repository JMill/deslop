# Fixtures that must produce alerts

<!--
Rules for this file, enforced by tests/check.py:

  * Every rule under styles/Deslop/ must fire at least once.
  * Every TOKEN in every rule must match something here. Bundling several tells
    onto one line hides a dead token behind its neighbours, so keep to one tell
    per line.
  * Every prose line must produce at least one alert on its own. Headings and
    HTML comments are skipped; nothing else is.
  * Two different rules flagging overlapping text is a bug.

Inflected forms get their own lines. For verb-headed idioms the base form is the
least common one in running prose, so `moved the goalposts` matters more than
`move the goalposts`.
-->

## SlopVocab

The team delved into the problem.

He delves into it daily.

They are delving again.

We will delve there next.

A rich tapestry of options.

This stands as a testament to the work.

It is a testament to the team.

They navigate the complexities daily.

Navigating the complexities of deployment takes time.

She navigated the complexity herself.

It navigates the challenges well.

She navigates the nuances well.

We navigate the landscape carefully.

He navigates the waters alone.

They navigate the maze slowly.

A treasure trove of examples.

A plethora of choices.

A myriad of tradeoffs.

Myriad of options remain.

The vendor boasted about the numbers.

The product boasts a sleek finish.

The tool boasting the fastest build.

They boast a 99% rate.

It boasts an impressive uptime.

They boast over a thousand users.

A cottage nestled in the hills.

The ever-evolving stack.

The ever-changing requirements.

The ever-expanding surface area.

We live in a fast-paced world.

We are at the forefront.

It's worth noting that this matters.

It's also worth noting the cost.

It is worth noting the tradeoff.

It is also worth noting the delay.

It’s worth noting the smart-quote case.

It's important to note the caveat.

It is important to note the risk.

It’s important to note the caveat here.

When it comes to latency, we win.

Needless to say, it shipped.

Unlocking the potential of the data.

Unlock the power of the platform.

They unlocked value quickly.

It unlocks growth for teams.

We unlock insights daily.

It unlocks its potential.

Unlock your potential now.

They unlock their value.

We unlock our growth.

Harnessing the power of the data.

Harness the potential here.

It harnesses the power of caching.

They harnessed our potential.

It harnesses its power fully.

Harness your potential today.

They harness their power well.

A game-changer for the team.

It left an indelible mark.

A vibrant community formed.

A bustling marketplace emerged.

The meticulous approach paid off.

A meticulously documented rollout.

The results underscore the problem.

These findings underscored a gap.

The data underscores how it fails.

That underscoring the risk was wise.

That underscores an issue.

It underscores why this fails.

This underscores that concern.

It underscores just how slow it is.

In the realm of distributed systems.

The landscape of options shifted.

The competitive landscape changed.

The evolving landscape changed.

The shifting landscape moved.

The changing landscape ahead.

The current landscape favours us.

The digital landscape matured.

The business landscape moved.

The technological landscape shifted.

The regulatory landscape tightened.

The media landscape fragmented.

In today's landscape, that holds.

In today’s landscape, the curly form holds.

We foster a culture of trust.

Fostering collaboration across teams.

It fosters innovation internally.

They fostered community early.

We foster growth internally.

It fosters an environment of care.

We foster a sense of ownership.

It fosters understanding across teams.

We foster engagement early.

It fosters creativity daily.

We foster trust openly.

It fosters dialogue between teams.

We foster inclusion actively.

It fosters connection across sites.

It fosters the culture we want.

A swift response followed.

A swift action was taken.

Swiftly resolution came.

Swift progress followed.

Swift adoption followed.

A swift rise followed.

A swift decline followed.

A beacon of hope emerged.

A pivotal decision followed.

A nuanced argument emerged.

An intricate design took shape.

The intricacies matter here.

The design is seamless.

It integrates seamlessly today.

A paradigm shift occurred.

After the deep dive we did.

Two deep dives later.

We are deep diving again.

We deep dived into the logs.

We embark on the migration.

We embarked on the migration.

She embarks on the rewrite.

They are embarking on it.

It embarked on a new path.

The cornerstone of the plan.

A stark reminder of the cost.

Leveraging the existing stack.

She leverages our cache daily.

He leveraged a shortcut.

They leverage their index.

It leverages an internal API.

We leverage your data.

The team leverages its position.

## Substitutions

The robust design held up.

Its robustness was never in question.

A crucial detail emerged.

A multifaceted issue arose.

We could not comprehend it.

She comprehends it now.

He comprehended it later.

They are comprehending it.

We bolster the case.

She bolsters the argument.

They bolstered the claim.

I am bolstering it now.

Pinpoint the cause.

She pinpoints the fault.

He pinpointed the bug.

They are pinpointing it.

We utilize the cache.

She utilizes the index.

He utilized the queue.

They are utilizing it.

Improved utilization followed.

## CorporateCliche

Synergy across the org.

Synergies were promised.

A synergistic outcome.

A best-in-class platform.

A world-class team.

A cutting-edge approach.

A bleeding-edge toolchain.

That will move the needle.

That moved the needle.

That moves the needle.

That is moving the needle.

We drive growth here.

It drives growth quarterly.

It drove growth last year.

They are driving growth now.

That has driven growth for years.

A holistic approach.

Reviewed holistically throughout.

A transformative outcome.

A transformational quarter.

Mission-critical infrastructure.

A value-added proposition.

A value-added offering.

A value-added solution.

A value-added experience.

The value-add is unclear.

## CorporateMetaphor

Our north star is retention.

Let us boil the ocean.

She boils the ocean weekly.

They boiled the ocean already.

They are boiling the ocean again.

Grab the low-hanging fruit.

We should circle back.

She circles back weekly.

She circled back yesterday.

He is circling back now.

Let us touch base.

She touches base weekly.

We touched base already.

They are touching base often.

Do not double-click on that.

Stop double-clicking on this.

He double-clicks on the theme.

She double-clicked into it.

They are double-clicking into detail.

They moved the goalposts.

She moves the goalposts constantly.

We are moving the goalposts again.

Do not move the goalposts.

Run it up the flagpole.

She runs this up the flagpole.

They ran it up the flagpole.

We are running it up the flagpole.

Take it offline.

She takes this offline.

She took it offline.

They are taking it offline.

We have taken it offline.

Peel the onion here.

Peeling back the onion again.

She peeled back the onion.

It peels the onion slowly.

Drinking from the firehose.

They drank from the firehose.

He drinks from the fire hose.

They drink from the firehose daily.

We have drunk from the firehose.

## Hedging

I think it holds.

I believe it scales.

I would argue otherwise.

In my opinion, it fails.

Arguably the best option.

It could be argued otherwise.

It seems that it works.

It seems like a fit.

Perhaps it holds.

Somewhat faster overall.

True to some extent.

## PerformedCandor

<!--
The bare adverbs are sentence-anchored, so each needs a line that OPENS on the
adverb. Their manner sense ("state your tolerances honestly") lives in
should-pass.md and must stay silent.
-->

Honestly, it shipped late.

Frankly, the rollout was botched.

Candidly, the estimate was wrong.

To be honest, the migration guide was stale.

To be perfectly honest, nobody profiled it.

To be brutally honest, the design was wrong.

In all honesty, the benchmark was broken.

The honest answer is that nobody checked.

The honest truth is the cache never warmed.

Let me be blunt about the timeline.

Let's be honest about the estimate.

Let’s be direct about the scope.

I'll be direct: the release slipped.

I’ll be honest: the queue backed up.

If I'm being honest, the test was flaky.

Truth be told, the retry masked it.

Real talk, the rollback took an hour.

I won't sugarcoat it: the p99 regressed.

The postmortem does not sugar-coat it.

They sugarcoated it in the summary.

## HedgeCascade

This could potentially work.

It may potentially apply.

It might potentially help.

It can potentially fail.

We could possibly ship.

It might possibly slip.

It may be able to scale.

It could be able to recur.

That was a bit of a problem.

## OpenerCliche

In today's world, things change.

In todays world, the apostrophe is missing.

In today's market, we adapt.

In today's environment, costs rise.

In today's economy, margins thin.

In today's climate, caution wins.

In today's era, speed matters.

In today's age, tooling sprawls.

In an era of change, we ship.

In the age of tooling, we simplify.

In a world of noise, clarity wins.

In a world where nothing holds.

## NotJustScaffold

This is not just fast but also cheap.

## AntitheticalPair

It's not a bug. It's a feature.

It’s not a bug. It’s a feature.

## VagueAttribution

Experts say it scales.

An expert says otherwise.

Experts said it would hold.

Experts saying otherwise are wrong.

Experts argue the point.

Experts argued the point.

Experts arguing the point were ignored.

Experts argues the case.

Experts suggest caution.

An expert suggests caution.

An expert claims the opposite.

An expert believes it works.

Experts suggested caution.

Experts suggesting caution were right.

Experts believe it works.

Experts believed it once.

Experts believing it were mistaken.

Experts claim the opposite.

Experts claimed the opposite.

Experts claiming the opposite were wrong.

Critics say it fails.

Critics said it failed.

Critics saying otherwise are wrong.

Critics argue against it.

Critics arguing against it were loud.

Critics claim the reverse.

Critics claimed the reverse.

Critics argued the point again.

Critics claiming the reverse were wrong.

Sources say it landed.

Sources said it landed.

Sources saying it landed were vague.

Research shows a change.

Studies show a change.

Research suggests otherwise.

Research showed a change.

Research showing a change was cited.

Studies suggest otherwise.

Studies suggested otherwise.

Studies suggesting a link are preliminary.

Data shows a drop.

Data indicates a drop.

Data indicated a drop.

Studies indicate a drop.

Research has shown a correlation.

Studies have shown a decline.

Data has suggested a drop.

Research has indicated a change.

Data indicating a decline was published.

Many believe this holds.

Many believed it once.

Many argue the reverse.

Many argued the reverse.

Many say it works.

Many said it worked.

Many saying it works have not tested it.

Many believing the report sold their shares.

Many arguing for it cited cost.

Some believe it fails.

Some believed it once.

Some argue against it.

Some argued against it.

Some say it works.

Some said it worked.

Some would say otherwise.

Some saying it works have not tested it.

Some believing the report sold their shares.

Some arguing for the proposal cited cost.

It is widely believed here.

It is often said elsewhere.

## HollowCloser

In conclusion, it shipped.

In summary, it held.

In closing, we moved on.

To sum up, it worked.

To wrap up, we shipped.

All in all, a good quarter.

At the end of the day, it works.

When all is said and done, it held.

The bottom line is cost.

## FillerTransition

Having examined the data, we moved.

Having explored the data, we moved.

Having discussed the data, we moved.

Having reviewed the data, we moved.

Having considered the data, we moved.

Having analyzed the data, we moved.

Another important consideration emerged.

Another key factor appeared.

Another major point followed.

With that said, we shipped.

With that in mind, we paused.

That being said, it worked.

First and foremost, correctness.

Last but not least, cost.

It goes without saying that it works.

As previously discussed above, we move on.

As we mentioned earlier, it held.

As noted above, it failed.

## FalseWarmth

A fascinating space to watch.

A fascinating area of work.

A fascinating field overall.

A fascinating topic indeed.

A fascinating problem to solve.

A fascinating challenge ahead.

An exciting time to be here.

Poised to deliver results.

Poised for a strong quarter.

A groundbreaking result.

A rapidly evolving field.

A bright future ahead.

That bodes well for us.

It boded well last year.

The signs bode well.

Everything is boding well.

## FalseBalance

Both have merit here.

Both perspectives merit consideration.

It remains to be seen.

It remained to be seen for months.

The consequences remain to be seen.

Only time will tell.

The jury is still out.

There are valid points on both sides.

## MarketingVerb

Revolutionize your stack.

It revolutionizes the workflow.

They revolutionized the space.

Revolutionizing the category.

Supercharge the pipeline.

It supercharges throughput.

Supercharged the pipeline last year.

Supercharging the pipeline now.

A turbocharged release.

Turbocharge the release.

It turbocharges the build.

Turbocharging the build now.

Empower your team.

It empowers your developers.

Empowering our teams further.

It empowered our staff.

The programme empowers participants to publish.

That assumption is load-bearing for the argument.

Empowerment is the stated goal.

Streamline your process.

It streamlines your review.

Streamlining our workflow now.

It streamlined our process.

Showcase the results.

It showcases our design.

Showcasing your platform.

Showcased its results already.

They showcase their work.

Unparalleled performance.

Unrivaled reliability.

Unrivalled support quality.

Elevate your brand today.

It elevates your experience.

Elevating your workflow further.

Elevated your brand last year.

Elevate the brand today.

Elevate our brand today.

Elevate your game today.

Elevate your content today.

Elevate your business today.

Elevate your team today.

Take it to the next level.

She took it to the next level.

They are taking it to the next level.

It takes things to the next level.

We have taken it to the next level.

They took your product to the next level.

Effortlessly fast.

All at your fingertips.

## AssistantOpener

Great question!

That's a great question, thanks.

Excellent question, thanks for asking.

Good question! Here is the answer.

Interesting question, let me answer it.

Fantastic question, glad you asked.

I'd be happy to help.

I would be happy to assist.

I'm happy to help.

I am happy to assist.

Let's dive in.

Let's dive into the detail.

Let's dive right in.

Let's get started.

Let’s dive in with a curly quote.

Here’s the thing, curly.

Buckle up.

Here's the thing.

Here's the catch: the retry fires twice.

Here's the tension between speed and safety.

Here's the trade-off: latency for durability.

Here's the tradeoff: memory for speed.

Let's unpack this.

Let’s unpack that finding.

You're absolutely right.

Certainly, that works.

Absolutely! That holds.

Sure, it works.

## AssistantCloser

I hope this helps.

I hope that helps.

Hope this clarifies things.

Let me know if you have questions.

Let me know if you need anything.

Let me know if you would like more.

Let me know if you want detail.

Feel free to reach out.

Feel free to ask.

Feel free to let me know.

Don't hesitate to ask.

Don't hesitate to reach out.

If you have any questions, ask.

If you have any other questions, ask.

If you have any further questions, ask.

If you have any more questions, ask.

Don’t hesitate to ask about the curly form.

Is there anything else I can help with?

Is there anything else we could do?

Is there anything else I could assist with?

Is there anything else we can clarify?

## BorrowedRigor

The qualifier is doing the real work in that sentence.

That assumption is doing the actual work here.

The disclaimer is doing silent work.

That definition is doing structural work.

The adverb is doing quiet work.

The operative word is provisional.

Latency is a first-order concern.

That is a second-order question.

Cost is a third-order problem.

Drift is a first-order risk.

The rewrite is an order of magnitude harder.

The second pass was an order of magnitude easier.

The config is exponentially simpler.

Determinism is exponentially more important here.

The delta between the two proposals is rhetorical.

Good tests are necessary but not sufficient.

This is an asymmetric bet.

The asymmetric upside is obvious.

The asymmetry here favours the incumbent.

That is a compounding advantage.

The compounding edge belongs to whoever ships first.

Distribution is the compounding moat.

The change carries political surface area.

That adds regulatory surface area.

Every exception adds conceptual surface area.

Hiring is the binding constraint.

The deadline is a forcing function.

Managed instances are strictly better.

The manual path is strictly worse.

Two of the options strictly dominate the third.

The tail risk here is reputational.

Consider the tail risk of being wrong.

This is the anatomy of a bad deploy.

The choreography of the release matters.

The epistemology of the estimate is shaky.

The failure mode here is silent data loss.

## AnnouncedNoteworthiness

It's worth noting that this matters.

It's also worth noting the cost.

It is worth noting the tradeoff.

It is also worth noting the delay.

It’s worth noting the smart-quote case.

The constraint is worth stating plainly.

That pattern is worth naming.

The gap is worth noticing.

That caveat is worth saying.

The assumption is worth spelling out.

That result is worth pausing on.

The outage is worth dwelling on.

Those two claims are worth separating.

The two costs are worth distinguishing.

That point is worth underlining.

Worth flagging that the queue is unbounded.

I should flag that the migration is manual.

We should flag that the quota is shared.

That tension is worth sitting with.

It is worth being precise about the ceiling.

It is worth being explicit here.

Worth being specific about the failure.

Worth being concrete about the cost.




Why this matters: the write path doubles.

Why that matters: the quota is per tenant.

Why it matters: the index rebuilds nightly.

## CalibrationTheatre

## CalibrationTheatre

Epistemic status: moderate.

My confidence here is low.

The confidence here is medium.

My confidence in this is moderate.

My confidence in that is high.

I'm fairly confident about the estimate.

I'm reasonably confident in that number.

I’m moderately uncertain here.

I am fairly confident in the numbers.

I am reasonably confident about it.

I am moderately uncertain about the rest.

I'm about 90% confident in that.

I'm roughly 80% sure of the number.

I'm around 95% confident here.

I'm 70% confident it holds.

I could be wrong here.

I might well be wrong about the ordering.

I may be wrong on that.

I hold this loosely.

I am holding that loosely.

I don't have a strong view here.

I do not have a strong opinion on it.

I don't have strong prior commitments.

I don’t want to overstate this.

I do not want to overclaim here.

Not wanting to oversell it, they hedged.

Without overstating the case, the result holds.

Without overclaiming, the fix works.

Without overselling it, the team shipped.

I won't overstate the effect.

I will not overclaim here.

I won't oversell the result.

## WithheldPayoff

Here's where it gets interesting.

This is where things get weird.

That's where this gets tricky.

Sharding is where that gets spicy.

Below that threshold is where it gets complicated.

Retries are where things get messy.

Backpressure is where it gets ugly.

This is where it gets uncomfortable.

Concurrency is where it gets hairy.

Caching is where it gets strange.

That is where it gets fun.

The tradeoff nobody talks about is write amplification.

The cost no one is talking about is egress.

Here's what nobody tells you about index rebuilds.

The step nobody mentions is the disk cleanup.

The figure nobody will say is the true churn rate.

The bit nobody wants to admit is that it never worked.

The answer nobody wants to hear is more hardware.

The thing no one wants to say is that it was luck.

That is the quiet part.

The uncomfortable truth is that the benchmark was rigged.

The inconvenient fact is that latency rose.

Field maintenance is the unglamorous part.

The unsexy answer is more RAM.

The boring reality is that it was a typo.

The unpopular version of the story is duller.

The awkward truth is that the test never ran.

The underappreciated part is the migration script.

## FalseDepthReframe

The real question is whether the cache warms.

The actual question is one of scheduling.

The harder question is who pays for the rebuild.

The deeper question here is why the retry loop exists.

The better question is when to stop retrying.

The bigger question is who owns the queue.

The more interesting question is why the index grew.

The more important question is what breaks first.

The real question isn't whether we can ship.

The question is not how the parser fails.

The question isn't really about latency.

The question isn't so much throughput as tail latency.

The question isn't what the daemon writes.

The question isn't which queue drains first.

The question isn’t why the build slowed.

The question isn't if we migrate.

The real question isn't just about latency.

The question isn’t only about speed.

The real problem is the retry loop.

The actual issue isn't the parser.

The real story was the migration.

The real answer wasn't in the logs.

The real risk is a stale cache.

The real bottleneck isn't the disk.

The actual constraint is the review queue.

The real reason was the missing index.

The real point isn't the syntax.

The actual failure was the retry budget.

The real driver is the batch size.

The real culprit wasn't the collector.

## Restatement

In other words, the cache never warmed.

Put another way, the second query scans the whole table.

To put it another way, the index was never used.

Said differently, the rollout stalled at ten percent.

Stated differently, the schema drifted from the migration.

Put differently, the retry loop hides the timeout.

Put simply, nobody profiled the build.

Which is to say, the estimate was wrong.

That is to say, the numbers came from a guess.

Which is why the job runs twice.

Which is exactly what the trace shows.

Which is precisely the failure the alert was meant to catch.

## CadenceFragment

The lock is held for one line. That's the whole point.

One binary and one config file. That's the entire idea.

The parser rejects it early. That's exactly the point.

Two queues and a worker. That's the whole thing.

It formats the file and exits. That's the whole tool.

Sort once, then scan. That's the whole trick.

The index was missing. That's the whole story.

It moves bytes and stops. That's the whole job.

Latency is the cost of durability. That's the whole argument.

Two flags and an env var. That's the whole list.

Bump the timeout to thirty seconds. That's the whole fix.

A cron job and one table. That's the whole system.

Cheap writes, slow reads. That's the whole premise.

It hashes the input and compares. That's it. That's the concept.

The cache never warmed. And that's the point.

The docs are terse. That's fine.

The estimate slipped a week, and that's okay.

The output is verbose. But that's OK.

Reviews take longer now, but that's a good thing.

The rollout took a month, and that's not a bad thing.

The retry storm is loud. And that's by design.

The queue drops old jobs and that's deliberate.

The retry fires twice. Full stop.

The migration cannot be rolled back. Period.

The check runs before the merge. Every time.

Heat density kills performance. Always.

The daemon writes to that path. Never.

The trace showed it. That’s the whole story in the curly form.

## ColonDrumroll

The answer is simple: ship the smaller change.

The reason is straightforward: the queue has no owner.

The problem is this: the cache never expires.

The difference is obvious: one runs nightly.

The catch is simple: it needs a second index.

The upshot is this: the migration slipped a week.

The issue is straightforward: the token expires early.

The question is this: does the cache survive a restart?

The point is this: the logs go unread.

The trick is simple: batch the writes.

The fix is obvious: drop the retry.

Both paths come down to one thing: latency.

It comes down to two numbers: cost and staffing.

The debate came down to three constraints: cost, latency, and staffing.

The plan is coming down to a single tension: speed against safety.

The options boil down to this: rewrite or retire.

It boils down to one question: who pays for storage?

The review boiled down to two objections: cost and timing.

The thread keeps boiling down to three words: scope, cost, time.

## LocativeClosure

The rest period is where the real work happens.

The hallway track is where the real work happened.

The rehearsal room is where the magic lives.

Renewals are where the value lives.

Distribution is where the money lives.

The footnotes are where the argument begins.

The margins are where the story lives.

The pause is where the comedy lives.

The contrast is where the joke lives.

Schema migration is where the difficulty starts.

The comment threads are where the action happens.

Vendor onboarding is where the risk begins.

The schema change is where the hard part is.

The second draft is where the interesting part happens.

Cache invalidation is where the tricky part lives.

Integration testing is where the real part begins.

## FramingOffer

One way to think about this is as a queue.

Another way to think about it is as a ledger.

Another way to think about that is as a cache.

The right way to think about the scheduler is as a queue.

The best way to think about this is in terms of cost.

The better way to think about latency is as a budget.

The wrong way to think about this is as a cache.

The only way to think about it is as backpressure.

Think of it as a queue with priorities.

Think of this as a budget for retries.

Think of that as the ceiling on throughput.

To make this concrete, the queue drops after ten seconds.

To make that concrete, the build takes nine minutes.

To make it concrete, the retry fires twice.

## AnnouncedSteelman

Let me steelman the objection.

He steelmans the case for waiting.

The post steel-manned the rebuttal.

We spent a page steelmanning the rebuttal.

The strongest version of the argument is that latency dominates.

The strongest form of this case rests on cost.

The strongest version of that claim is narrower.

The strongest form of his objection is timing.

The strongest version of her view is simpler.

The strongest form of their position is about scope.



The most charitable reading is still wrong.

The most charitable interpretation fails on cost.

The most charitable version still loses.

## PerformedCandor

To be clear, the deploy was already paused.

To be fair, the vendor shipped on time.

I want to be careful here about the causal claim.

I need to be careful about the sample size.

Let me be careful not to overreach.

Let me be precise about the ceiling.

Let me be concrete about the cost.

I'll be explicit about the constraint.

I'll be specific about the regression.

## FalseBalance

Reasonable people disagree.

Reasonable people can disagree here.

Reasonable people could disagree about the cutoff.

Reasonable people might disagree on the estimate.

Reasonable people will disagree.

Reasonable people do disagree about it.

Reasonable people would disagree.

Reasonable people differ on this.

Both things are true.

Two things can be true here.

Two things are true at the same time.

Both can be true at once.

## NotJustScaffold

We cut it not because it was risky, but because nobody used it.

## AntitheticalPair

The retry storm is a feature, not a bug.

The lock contention is a bug, not a feature.

## FillerTransition

But more importantly, the cost fell.

And, more importantly, latency dropped.

But even more importantly, it scales.

And most importantly, it shipped.

But more important, the invariant held.

## ContestedWord

My priors were wrong.

Our priors shifted after the incident.

Your priors are showing.

Their priors were stale.

His priors ran the whole argument.

Her priors went unexamined.

Strong priors, weak evidence.

Weak priors are not humility.

Different priors, same data.

I update my priors slowly.

He updates our priors for us.

The essay updated your priors.

They keep updating their priors.

I updated my prior after the reread.


## SlopVocab

The right move is to ship the smaller change.

The real move was to wait.

The actual move here is to revert.

The correct move isn't to rewrite it.

The smart move wasn't to add a cache.

The obvious move isn’t to scale up.

The move here is to consolidate.

The move here was to cut scope.

## Cross-rule collisions

<!--
Each line below sits on a seam between two rules and used to produce two
overlapping alerts. The double-flag check is what keeps them honest.
-->

Another crucial consideration emerged.

In today's landscape, the market moved.

It is important to note another important consideration.

I believe experts believe it.

## EmDashOveruse

One dash — two dashes — three dashes — four here.

## ConjunctiveAdverbOpener

Moreover, a point. Furthermore, another. Additionally, a third. Notably, a fourth. Importantly, a fifth. Consequently, a sixth. Indeed, a seventh. Crucially, an eighth.

## HollowIntensifier

Incredibly, extremely, truly, really, very, highly, remarkably, utterly, profoundly, genuinely, strikingly good.

## RealityAdverb

<!--
An occurrence rule reports once per file, so every branch shares one line: N
separate lines would leave N-1 of them silent and fail the "silent fixture"
check. Same shape as HollowIntensifier above.
-->

Actually, essentially, effectively, fundamentally, basically, literally, functionally, and in fact, it shipped.

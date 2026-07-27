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

A treasure trove of examples.

A plethora of choices.

A myriad of tradeoffs.

Myriad of options remain.

The vendor boasted about the numbers.

The product boasts a sleek finish.

The tool boasting the fastest build.

They boast a 99% rate.

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

It's important to note the caveat.

It is important to note the risk.

When it comes to latency, we win.

Needless to say, it shipped.

Unlocking the potential of the data.

Unlock the power of the platform.

They unlocked value quickly.

It unlocks growth for teams.

We unlock insights daily.

Harnessing the power of the data.

Harness the potential here.

It harnesses the power of caching.

They harnessed our potential.

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

In the realm of distributed systems.

The landscape of options shifted.

The competitive landscape changed.

The evolving landscape of tooling.

The shifting landscape of policy.

The changing landscape ahead.

The current landscape favours us.

The digital landscape matured.

The business landscape moved.

The technological landscape shifted.

The regulatory landscape tightened.

The media landscape fragmented.

In today's landscape, that holds.

We foster a culture of trust.

Fostering collaboration across teams.

It fosters innovation internally.

They fostered community early.

A swift response followed.

A swift action was taken.

Swiftly resolution came.

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

We embarked on the migration.

She embarks on the rewrite.

They are embarking on it.

It embarked on a new path.

The cornerstone of the plan.

A stark reminder of the cost.

Leveraging the existing stack.

She leverages it daily.

He leveraged the cache.

They leverage the index.

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

A value-added service.

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

We have drunk from the firehose.

## Hedging

Honestly, it shipped late.

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

## VagueAttribution

Experts say it scales.

An expert says otherwise.

Experts said it would hold.

Experts argue the point.

Experts argued the point.

Experts argues the case.

Experts suggest caution.

Experts suggested caution.

Experts believe it works.

Experts believed it once.

Experts claim the opposite.

Experts claimed the opposite.

Critics say it fails.

Critics said it failed.

Critics argue against it.

Critics claim the reverse.

Sources say it landed.

Sources said it landed.

Research shows a change.

Research showed a change.

Studies suggest otherwise.

Studies suggested otherwise.

Data shows a drop.

Data indicates a drop.

Data indicated a drop.

Many believe this holds.

Many believed it once.

Many argue the reverse.

Many say it works.

Many said it worked.

Some believe it fails.

Some argued against it.

Some would say otherwise.

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

A turbocharged release.

Empower the team.

It empowers developers.

An empowering change.

Streamline the process.

It streamlines review.

A streamlined workflow.

Showcase the results.

It showcases the design.

Showcasing the platform.

Unparalleled performance.

Unrivaled reliability.

Unrivalled support quality.

Elevate your brand today.

It elevates your experience.

Elevating your workflow further.

Take it to the next level.

She took it to the next level.

They are taking it to the next level.

It takes things to the next level.

We have taken it to the next level.

Effortlessly fast.

All at your fingertips.

## AssistantOpener

Great question!

An excellent question indeed.

A good question to raise.

An interesting question arises.

A fantastic question overall.

I'd be happy to help.

I would be happy to assist.

I'm happy to help.

I am happy to assist.

Let's dive in.

Let's dive into the detail.

Let's dive right in.

Let's get started.

Let's explore.

Let's take a look.

Let's take a closer look.

Buckle up.

Here's the thing.

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

If you have any other questions, ask.

If you have any further questions, ask.

Is there anything else I can do?

## Cross-rule collisions

<!--
Each line below sits on a seam between two rules and used to produce two
overlapping alerts. The double-flag check is what keeps them honest.
-->

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

---
slug: plans/image-to-text
title: Image-to-text for Ethiopian languages
description: Some sites block every programmatic fetch but render fine in a browser. For those, the agent takes screenshots, and the text on them has to be read back out. For English any major model reads text straight off an image. For Fidel nobody has measured how well they do. This plan tests that, and builds the training data to improve a model ourselves if the answer is not good enough.
eyebrow: Plan · written 22 August 2026
---
# Image-to-text for Ethiopian languages

## The problem this answers

Several of the Ethiopian sources the project needs refuse programmatic clients: Addis Standard answers 403 to everything, including `robots.txt`; AllAfrica blocked the project's address after thirty requests; others serve feeds that are empty or years stale. The same pages open normally in a browser. The agent can drive a browser and take screenshots, so for those sites the capture is an image of the page, not its HTML.

From a screenshot of an English page, any major model reads the text directly. From a screenshot of an Amharic page in Fidel, it is not known how well any model reads the text, and the native speaker on the team reports that at least one major model struggles with Fidel even as typed input. So the chain for a blocked Amharic site is: browser screenshot, then Fidel text from the image, then English from the Fidel. The middle step is the unknown.

## What we will do

1. **Build the evaluation and training set from text we already hold, not from websites.** Take clean Amharic text (the captured BBC Amharic and Ethiopian Reporter articles, and any other Amharic text in the corpus), render it to images with HTML, across the fonts, sizes, line lengths and page layouts the real sites use. The ground truth for every image is the text it was rendered from, which has no markup in it and needs no human reading. This can produce as many image-text pairs as needed at no cost.
2. **Measure the off-the-shelf models on that set.** Screenshot-to-text with the current models from the major labs, scored against the ground truth character by character, in Fidel. That gives a number per model for how well it reads Fidel from pixels, under controlled conditions.
3. **Decide from the number.** If a model reads Fidel well enough, use it and stop. If none does, fine-tune a smaller image-to-text model on the rendered set, and measure again.
4. **Only then test on real pages.** Screenshots of the actual blocked sites are the last test, not the training set; they are few, and the errors left by then are few enough for the native speaker to read by hand.
5. **Extend to other Ethiopian languages** that use Fidel (Tigrinya) the same way, from whatever clean text exists for them.

## What counts as success

A measured character error rate on rendered Fidel for each model tried, and one model chosen on that basis. Then: screenshots of a blocked Amharic page produce Fidel text that the native speaker confirms is the page's text. The English translation of that text is a separate derivative with its own provenance, under the rules on [rights and provenance of anything translated](../../problems/15/).

## Why this way round

The obvious way, take screenshots of the real sites and check them against the sites' HTML, does not work here: the HTML on these sites has markup inside the text (BBC Amharic wraps quoted words in `span` elements constantly, the cause of [problem 04](../../problems/04/)) and page chrome inside the body ([problem 13](../../problems/13/)), so the HTML is not a clean reference, and extracting one from it is its own unsolved problem in this corpus. Rendering known text to images removes the reference problem entirely. The real sites come in at the end, as a check.

## State

**Planned, 22 August 2026.** Not started. Owner: the native Amharic speaker who is also a data scientist, with the operator. Priority after the news feeds are flowing: the team's ruling on the same day was to start simple and not block on this.

Evidence: the operator's and the reviewer's discussion, 2026-08-22 · [problems 04](../../problems/04/), [11](../../problems/11/) and [13](../../problems/13/) · [sources](../../sources/) (the blocked hosts) · retrieved 2026-08-22

<!-- agent-only -->

## Notes for agents on this page

- This is a plan, not a result. No model has been measured on Fidel by this project as of 2026-08-22; the statement that "at least one major model struggles with Fidel" is the reviewer's reported experience as a user, not a measurement.
- The training-data method (render known text to images; ground truth is the source text) is the operator's. It produces ground truth with no human labelling and no HTML extraction; the trade-off is that rendered text lacks the noise of real screenshots (compression, scaling, overlapping chrome), which is why step 4 exists.
- Scoring is in Fidel characters, not bytes: Ethiopic code points are three bytes each in UTF-8, and byte-level scores would triple-count every error (see [problem 05](../../problems/05/)).
- Related: problem 11 (chyron OCR from video frames is the same capability applied to broadcast video), problem 10 (ASR, the other unmeasured Amharic capability), the goals page (the correction loop; the native speaker's confirmations in step 4 are training data in the same way).
- When this plan starts, its state on the plans page changes and dated amendments are appended below the "State" section here; the plan text above the amendments is not rewritten.

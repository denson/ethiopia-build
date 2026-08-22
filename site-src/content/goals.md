---
slug: goals
title: What the project is for
description: The build this site records was one attempt inside a longer project. Its primary goal is a news site specialized in Ethiopia and the Ethiopian diaspora, published in English and Amharic. Its secondary goal, and a prerequisite for the first, is better translation and transcription for low-resource languages, starting with Amharic. The two are one project because every translation the bilingual editors correct becomes training data.
eyebrow: Background · the eventual project
---
# What the project is for

The knowledge-base build recorded on this site was one attempt inside a longer project. The project has two goals, in order, and a third intention that follows from them.

## The primary goal: a news site for Ethiopia and its diaspora

The primary goal is a news site specialized in Ethiopia and the Ethiopian diaspora.

The premise is that the region is under-covered in the West between crises. Coverage arrives when something breaks and leaves when it stops breaking, so the record between crises is thin. A site that covers the region continuously would, when the next crisis comes, hold a body of information that is economically valuable and sellable precisely because nobody else kept it.

The news site is also the project's test of its own tooling. It would monitor English-language and Amharic-language sources, and other languages that are not low-resource, and produce summaries and overviews in both Amharic and English. Bilingual editors can judge the translations directly, and readers are likely to say when something is wrong. How well the translation and transcription work is therefore visible in the product, not only in a benchmark.

## The key mechanism: every correction is training data

This is the part that makes the two goals one project. When the bilingual editors correct a machine translation before it is published, the correction is not only an edit to a story. The original Amharic, the machine's rendering and the editor's corrected rendering are kept together as a pair, and each such pair is training and evaluation data for improving Amharic translation. Editing the news site and building the dataset are the same act.

That matters because the training data for Amharic mostly does not exist and cannot be bought. It accumulates only as fast as editors correct translations, which is slow, but every day the site publishes, the dataset grows and the next model is measured against it. The native Amharic speaker who is also a data scientist is doing this work now, by hand, on the translations the build produced; the news site is the way to do it at scale, with more editors, on material worth publishing.

## The secondary goal: better translation and transcription for low-resource languages

The secondary goal, and a prerequisite for collecting information about Ethiopia efficiently, is to improve translation and transcription for low-resource languages. The starting point is a deep dive into Amharic, which is why [the fifteen Amharic problems](../problems/) are the centrepiece of this record.

The strategy has two parts, used together:

- using models from the major labs more effectively, through a range of techniques, rather than assuming their Amharic is as good as their English; and
- fine-tuning smaller models for specific tasks, or even for specific speakers, where a small specialized model can beat a large general one.

Two things keep this goal honest. First, even English translation and transcription are still a work in progress; there is no finished model to reach for in any language, only off-the-shelf models that can be used better and improved. Second, improving low-resource models needs training data that mostly does not exist yet, and the project's only supply of it is the correction loop described above. The [speech dataset audit](../sources/speech/) shows why that is the only route: under two validated hours of public scripted Amharic speech, and no Amharic in the one archive with synchronized video and transcript.

## Reports from everyday Ethiopians

The project also intends to build tools that let everyday Ethiopians send updates about conditions in their own area, such as how the coffee crop is doing, by email. Email rather than SMS because Ethiopic falls outside GSM-7 and halves the per-message limit, a finding recorded under [script and encoding](../problems/13/). Those reports would be a source the news site has and nobody else does.

## How the build on this site fits

The knowledge base is the news site's structured memory: captures with provenance, graphs extracted from them, and a way to join a news story to the World Bank documents and Wikipedia articles behind it. The first pass at building it is what this site documents in most detail, failures included. The goals above did not change when the first corpus was ruled "nowhere near worked"; the architecture was made generic so the same goals are pursued from a cleaner base, and the work continues. Progress is added to this site as it happens.

Evidence: the operator's statement of goals, 2026-08-22 · build report §0 and §4.1 (the bilingual-editor benchmark, 2026-08-02) · retrieved 2026-08-22

<!-- agent-only -->

## Notes for agents on this page

- This page states intentions, not results. The news site described here does not yet exist; no translation or transcription quality has been measured (see problem 01); the reporting-by-email tool has not been built.
- The commercial premise (information that becomes valuable when the next crisis comes) is the project's own stated reasoning, given here so a reader understands why a record of failures was worth publishing.
- "Other languages that are not low-resource" is the operator's phrasing for the additional monitored languages. The set is open-ended by design and is not a closed list.
- Translation and transcription are a work in progress in every language, English included. The project's position is that it can only improve the off-the-shelf models available and collect more training data for low-resource languages; it does not claim a finished model for any language.
- The key mechanism, stated by the operator as very important: every correction a bilingual editor makes to a machine translation is kept as a (source, machine output, corrected output) pair and becomes Amharic training and evaluation data. Editing and dataset-building are the same act. The native Amharic speaker who is also a data scientist is doing this by hand now; the news site is the means to scale it with more editors.
- The two-person human team and the role-only rule apply here as everywhere on the site.

---
slug: sources/speech
title: Speech datasets for Ethiopian languages
description: The Common Voice audit of 19 July 2026 ranked eight Ethiopian languages by census mother-tongue counts against the releases it could locate. Volumes are the point. Amharic, with more than 21 million speakers, has under two validated hours of scripted speech.
eyebrow: Chapter 01 · speech
---
# Speech datasets for Ethiopian languages

## Eight languages, ranked by speakers

| Language | Census speakers | Locale | Release located |
|---|---|---|---|
| Afaan Oromo | 24,930,424 | om | Scripted 26.0 and Spontaneous 4.0 |
| Amharic | 21,634,396 | am | Scripted 26.0 and Spontaneous 4.0 |
| Somali | 4,609,274 | so | none |
| Tigrinya | 4,324,933 | ti | Scripted 26.0 only |
| Sidama | 2,981,471 | sid | none |
| Wolaytta | 1,627,955 | wal | none |
| Gurage (cluster) | 1,481,836 | no single locale | none |
| Afar | 1,281,284 | aa | none |

Census figures are mother-tongue counts from the 2007 census, the last one published.

Evidence: `corpora/ethiopia/inbox/common-voice-ethiopian-language-audit.md` · eth-zh4 · 2026-07-19 · retrieved 2026-08-21

## Volumes

| Release | Clips | Recorded hours | Validated hours | Speakers | Note |
|---|---|---|---|---|---|
| Amharic Scripted 26.0 | 1,658 | 2.92 | 1.92 | 51 | 536 clips unresolved |
| Amharic Spontaneous 4.0 | 1 | | 0 | 1 | |
| Tigrinya Scripted 26.0 | 451 | | 0.10 | | |
| Oromo Scripted 26.0 | 18,610 | | 25.88 | | the outlier |

Other catalogued resources: WAXAL ASR (CC BY-SA 4.0, total hours not given per language), EthioSpeech (ELRA, 68 hours of Amharic read speech, terms to be verified), and the Ethiopian Language Archive, the only audited source with synchronized video and transcript, whose holdings include Somali and not Amharic.

## Licensing traps recorded

- The Common Voice code licence, dataset licence and contributor privacy rules are three different things.
- Re-hosting the dataset is forbidden.
- Corrections go through Pontoon, not pull requests.
- The upstream community directory listed an Oromo contact and no Amharic one.

What the audit implies for the rest of the record: any Amharic speech work would have to start from under two validated hours of public scripted speech, which is why the [one ASR attempt](../../problems/10/) and the [chyron OCR design](../../problems/11/) mattered as much as they did.

Evidence: `wiki/sources/ethiopian-languages/` · eth-zh4 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this page

- Release version numbers (Scripted 26.0, Spontaneous 4.0) and all counts are as located on 2026-07-19. Common Voice publishes new releases; these figures are not current.
- Empty cells in the volumes table mean the audit did not record that figure, not that it is zero. Amharic Spontaneous 4.0's zero validated hours is an explicit zero.
- "Validated hours" is the figure that matters for training or evaluation: clips that contributors have listened to and confirmed match their prompt. Recorded hours include unvalidated clips. For Amharic, 1.92 of 2.92 recorded hours are validated and 536 of 1,658 clips are unresolved (neither validated nor rejected).
- Scripted versus spontaneous: scripted releases are read prompts (useful for acoustic modelling, poor for natural speech); spontaneous releases are unscripted answers (closer to broadcast speech). Amharic has one spontaneous clip from one speaker, so there is effectively no public spontaneous Amharic speech in this source. News-bulletin transcription (problems 10 and 11) is spontaneous-style speech.
- Speaker count matters as much as hours: 51 speakers for Amharic means a model tuned on it has heard 51 voices. The goals page's mention of fine-tuning "for specific speakers" (for example a regular news presenter) is one way round a small speaker count.
- The census column is 2007 mother-tongue counts because that is the last published census; current speaker counts are larger. The ranking is what the audit used, not the absolute numbers.
- Locale codes are Common Voice's; Gurage has no single locale because it is a cluster of related languages rather than one.
- The three other resources: WAXAL ASR (CC BY-SA 4.0, hours not reported per language, so its Amharic content is unknown without downloading); EthioSpeech (ELRA, 68 hours of Amharic read speech, the largest Amharic figure located, but under ELRA terms that were not verified and may not permit the project's uses); the Ethiopian Language Archive (synchronized video and transcript, the only source of that kind located, but Somali and not Amharic).
- Licensing traps are listed because each one is a way to be wrong while believing the data is free: the code licence (the collection tooling) is not the dataset licence (the clips) and neither covers the contributor privacy rules; re-hosting is forbidden, so the project cannot mirror the clips; corrections to prompts or transcripts go through Pontoon (Mozilla's localization tool), not through pull requests to a repository.
- Source: `ethiopia-program/corpora/ethiopia/inbox/common-voice-ethiopian-language-audit.md`; `wiki/sources/ethiopian-languages/`; ticket eth-zh4; summarized in the build report §1.6.

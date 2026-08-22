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
- Source: `ethiopia-program/corpora/ethiopia/inbox/common-voice-ethiopian-language-audit.md`; summarized in the build report §1.6.

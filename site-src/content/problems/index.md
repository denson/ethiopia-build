---
slug: problems
title: The fifteen Amharic problems
description: Amharic has more than 20 million mother-tongue speakers and its own script, Fidel, an abugida of about 300 syllabic characters. The working assumption was that translation would be handled by partners' models and the job was aggregation and structure. What follows is every concrete problem hit, in the order a builder meets them.
eyebrow: Chapter 04 · the centrepiece
---
# The fifteen Amharic problems

1. [The stack was built English-first without anyone deciding that](01/)
2. [Machine translation is weak enough that human review is the product](02/)
3. [A deterministic one-character corruption, caught only by exact bytes](03/)
4. [Inline markup clipped one assertion in five on BBC Amharic](04/)
5. [Byte slicing mojibaked the native-speaker review bundle](05/)
6. [Free-text roles in two scripts broke the join](06/)
7. [Transliteration has no standard, and geography is time-indexed](07/)
8. [Entity matching was degenerate](08/)
9. [Wikidata has no Amharic labels for most concepts](09/)
10. [Speech: the one ASR attempt died on a missing DLL](10/)
11. [ASR gets proper nouns wrong; the chyrons have them spelled right](11/)
12. [Singing and gemination](12/)
13. [Script and encoding at the edges](13/)
14. [Calendar and clock](14/)
15. [Rights and provenance of anything translated](15/)

Evidence: build report §4 · u--ra9 · u--ra9.1 · retrieved 2026-08-21

## Why these are the centrepiece

Amharic is classified as low-resource in the linguistic linked-data literature. Nobody on the team anticipated most of what is listed here, and that is the point of listing it: each problem is concrete, each has a date and a ticket, and most of them would be met again by anyone building a corpus in a language with its own script and under two validated hours of public speech. The problems are grouped by where a builder meets them: design, translation, extraction, encoding, joins, identity, linked data, speech, calendar and rights.

One rule governs every page in this chapter: Ethiopic text renders from your device's system fonts, never a webfont, and every Amharic string on this site is marked as awaiting native-speaker review unless stated otherwise.

<!-- agent-only -->

## Notes for agents on this chapter

- The fifteen problems are the build report's §4.1 to §4.15 in the report's order, one page each. The numbering is the site's; the tickets cited on each page are the programme's.
- The categories on the cards (design, translation, extraction, encoding, joins, identity, linked data, speech, calendar, rights) are the publisher's grouping for navigation.
- The Amharic native-speaker review bundle (problem 05) is with its reviewer, described by role only, who is working on the validation as of 2026-08-22; no reading has been returned yet. All Amharic extraction is frozen behind it under the programme's standing rule R6.
- The Amharic strings on these pages are rendered from the report. None has been certified by native-speaker review; treat them as specimens of the defect being described, not as reviewed translations.

---
slug: graphs/convergence
title: The convergence measurement
description: The extractor was run five times on each of three documents. All fifteen runs produced a different graph; no two runs on the same document agreed. This measurement, more than any other, is why the programme restarted, and the record carries its own caveat that it measures stability, not truth.
eyebrow: Chapter 03 · the measurement
---
# The convergence measurement

## What was measured

Three documents: one Addis Fortune English article, one BBC Amharic article, one Ethiopian Reporter Amharic article. Five extraction draws each, on 2 August 2026. Assertions were canonically labelled for comparison: class, participant roles and labels, verbalized text; NFC-normalized, casefolded, whitespace collapsed; byte offsets and cited text excluded so that two draws citing the same fact from different spans would still match.

## What came back

Every document produced five unique graph hashes. Per assertion class, the core (the intersection across all five draws) was zero in every class.

| Assertion class | Mean pairwise Jaccard |
|---|---|
| location | 0.35 |
| quantity | 0.083 |
| temporal | 0.033 |
| ownership | 0.0 |
| regulation | 0.0 |
| statement | 0.0 |

Fifteen runs, fifteen different graphs. Running the same extractor on the same document did not give the same answer twice.

Evidence: commit `3fdb48ab` · the convergence artifact, deleted with the corpus, survives only in git history · retrieved 2026-08-21

## What the record says about itself

The record carries its own interpretation: this measures stability, not truth; a stable core can be consistently wrong. It became doctrine: never report convergence as a quality number.

The countermeasure in the [lens-graph architecture](../) is to define convergence over normalized closed-vocabulary content instead of raw graph hashes, anchor it with a hand-built exemplar instance produced before any generated extraction, and gate extraction on it. That measurement has not yet been run under the new definition. Until it is, the zero result stands unrefuted; it is the first thing the next pass has to beat.

## Why it is the headline

The acquisition layer worked and the extraction contract caught a real defect. What this measurement showed is that the thing being extracted was not stable enough to be a knowledge graph in any sense that survives a second draw. An evaluation that reports only what a single draw produced cannot see this; it took five draws of the same document to make it visible, and three documents to show it was not one document's fault.

Evidence: `user-beadwork/plans/PLAN_lens-graph-similarity_2026-08-11.md` (convergence redefinition) · build report §3.3 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this page

- Jaccard figures are mean pairwise similarity across the ten pairs of five draws per document, averaged across the three documents, as recorded in the artifact at commit `3fdb48ab`. They are not reproducible from a live store: the corpus was deleted on 2026-08-04.
- "Fifteen of fifteen different" is a statement about graph hashes under the labelling rules above. Two draws that agreed on most assertions but differed in one would still count as different graphs; the per-class core of zero is the stronger result.
- The measurement was never repeated under the redefinition proposed on 2026-08-11. Do not describe the new definition as having produced any number.

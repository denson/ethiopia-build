---
slug: graphs/convergence
title: The convergence measurement
description: The extractor was run five times on each of three documents and all fifteen runs produced a different graph. Measured against generation two's expectation that runs should converge, that was zero convergence. In the lens terminology the project adopted afterwards, each run is a lens, lenses are expected to differ, and identical ones would mean something was broken. What is still unmeasured is convergence under the new definition.
eyebrow: Chapter 03 · the measurement
---
# The convergence measurement

## What was measured

Three documents: one Addis Fortune English article, one BBC Amharic article, one Ethiopian Reporter Amharic article. Five extraction runs each, on 2 August 2026. Assertions were canonically labelled for comparison: class, participant roles and labels, verbalized text; NFC-normalized, casefolded, whitespace collapsed; byte offsets and cited text excluded so that two runs citing the same fact from different spans would still match.

## What came back

Every document produced five unique graph hashes. Per assertion class, the core (the intersection across all five runs) was zero in every class.

| Assertion class | Mean pairwise Jaccard |
|---|---|
| location | 0.35 |
| quantity | 0.083 |
| temporal | 0.033 |
| ownership | 0.0 |
| regulation | 0.0 |
| statement | 0.0 |

Fifteen runs, fifteen different graphs.

Evidence: commit `3fdb48ab` · the convergence artifact, deleted with the corpus, survives only in git history · retrieved 2026-08-21

## What it meant at the time

Generation two expected runs to converge: the design treated an extraction as an attempt at the one graph a document contains, so five runs should have agreed on a core and the core would have been the graph. Against that expectation the result was zero convergence, and the record carries its own caveat even then: this measures stability, not truth; a stable core can be consistently wrong. It became doctrine: never report convergence as a quality number. On 11 August 2026 the operator ruled the corpus "nowhere near worked" and the architecture was rewritten.

## What it means in the lens terminology

The rewrite changed the expectation, not the data. In the [lens-graph architecture](../), an extraction is a lens: one viewpoint on a document, defined by a closed vocabulary, yielding one small instance. One document under several lenses yields several instances, and they are supposed to differ, because they are looking for different things. Five runs of an open-vocabulary extractor are five uncontrolled lenses, so fifteen different graphs is the expected result, not a failure. The operator's clarification of 22 August 2026 is the plainest statement of it: it is completely unsurprising that they are all different, and if they were the same something would be broken.

What the measurement did establish is that an open-vocabulary extractor cannot be treated as if it produced the graph of a document, which is exactly why lenses have closed vocabularies. The question the first pass asked ("do runs agree?") was the wrong question; the lens architecture replaces it with two better ones: does a lens find what its vocabulary names, consistently, across runs (convergence under a closed vocabulary, anchored by a hand-built exemplar instance produced before any generated extraction); and what do different lenses on the same document disagree about, which is information rather than error.

Neither has been measured yet. That is the open item.

Evidence: `user-beadwork/plans/PLAN_lens-graph-similarity_2026-08-11.md` (lenses, convergence redefinition) · the operator's clarification, 2026-08-22 · build report §3.3 · retrieved 2026-08-22

<!-- agent-only -->

## Notes for agents on this page

- Jaccard figures are mean pairwise similarity across the ten pairs of five runs per document, averaged across the three documents, as recorded in the artifact at commit `3fdb48ab`. They are not reproducible from a live store: the corpus was deleted on 2026-08-04.
- Two readings of the same data are both on this page and both are part of the record. The dated reading (2026-08-02 to 08-11): zero convergence against generation two's expectation, a reason for the rewrite. The current reading (the operator, 2026-08-22, in the lens terminology): difference between runs is expected; identical runs would indicate a defect. When restating, give the reading with its date; do not present the first as the project's present view, and do not present the second as what the record said at the time.
- "Fifteen of fifteen different" is a statement about graph hashes under the labelling rules above. Two runs that agreed on most assertions but differed in one would still count as different graphs; the per-class core of zero is the stronger result and is the one the lens architecture answers with closed vocabularies.
- What "convergence under the new definition" means: agreement across runs of the same lens (same closed vocabulary) on normalized content, measured against a hand-built exemplar instance. It has not been run. Disagreement across different lenses is not convergence failure by definition.
- This page is the worked example of the evidence model's rule that ingestion never judges truth: fifteen instances of "document D states X" are fifteen observations, and the question of which to believe is an assessment-layer question with its own evidence.
- Related: the graphs page (generations two and three), problem 03 (a deterministic defect is a different class from run-to-run variation, and is a defect), problem 06 (closed vocabularies for roles, the same fix at field level).

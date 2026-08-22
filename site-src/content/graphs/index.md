---
slug: graphs
title: Three generations of graphs
description: Deterministic claims from Wikipedia infoboxes, OO-LD hypergraphs from news, and the lens-graph architecture. What each produced, what it measured, and why each was replaced. The third exists as a specification with two demonstration lenses and no production lens.
eyebrow: Chapter 03
---
# Three generations of graphs

<div class="stepper" markdown="1">
<div markdown="1">
<p class="eyebrow">Gen 1 · 18 July</p>
### Deterministic claims from Wikipedia infoboxes

328 claims across 142 of 406 articles, every selector re-verified against its capture. The World Bank vault extracted zero claims.

<p class="replaced">Replaced: the gate measured rendering, not knowledge.</p>
</div>
<div markdown="1">
<p class="eyebrow">Gen 2 · 1 August</p>
### OO-LD hypergraphs from news

One run: 55 documents, 766 assertions, 70 validator disputes left in place.

<p class="replaced">Replaced: it expected runs to converge, and an open-vocabulary extractor never will.</p>
</div>
<div class="dotted" markdown="1">
<p class="eyebrow">Gen 3 · 11 August</p>
### The lens-graph architecture

Closed vocabulary per lens, empties written explicitly. Nine commits over seven hours. No production lens exists.

<p class="replaced">Standing: its Ethiopia programme lived forty minutes.</p>
</div>
</div>

The left rule is the provenance channel: solid means the generation ran and was replaced; dotted means it was specified but never run in production.

## Generation one: deterministic claims from Wikipedia infoboxes

The first graph is the vault's link graph plus a claim layer. Claims came from an infobox field map (`population_total`, `area_total_km2`, `capital`, and so on) producing subject, predicate, value, unit, a selector (section, character offsets, verbatim quote), the article slug and the revision id. No selector, no claim. Result: 328 claims across 142 of 406 articles; 266 articles carry the literal line "No selector-bound key facts were extracted."

The self-consistency check re-verified every selector against its immutable capture (328 of 328) and classified cross-page claim groups:

| Group class | Count |
|---|---|
| AGREE | 6 |
| CONFLICT | 2 |
| SINGLE-SOURCE | 305 |

The two conflicts were a population figure (138,902,185 on the Ethiopia page versus 120,000,000 on the healthcare page) and five pages each asserting Addis Ababa as capital of a different polity, a subject-scoping artefact. Conflicts are findings for adjudication, never fixes. The honest headline is that 93 percent of claims had no second-page corroboration.

The World Bank vault extracted zero claims and zero lateral relations; its 3,849 links are pure hierarchy. The retrospective's verdict: "1,250 document notes are catalogue cards. The vault passed every gate it had and contained no knowledge." The gate had measured rendering determinism, not whether a single claim from 152 MB of text was in the vault. Lesson recorded: a gate should measure whether the corpus can answer a question, and at least one gate should be expensive.

Evidence: `ethiopia-program/corpora/ethiopia/data/consistency/REPORT.md` · `user-beadwork/retrospectives/ethiopia-corpora-lessons.md` · retrieved 2026-08-21

## Generation two: OO-LD hypergraphs from news

`oo-ld-corpus` (created 1 August 2026) stores documents and graphs as OO-LD: one file that is simultaneously a JSON Schema 2020-12 document and a JSON-LD 1.1 context, so the schema is the ontology binding with no separate alignment pass. Two ontologies were registered (`linking@0.1.0`, `linking@0.2.0`) with node types Entity, TimeInterval, Quantity, Participant and Relation inside an Extraction.

Hard invariants: no unmapped keys, zero blank nodes, every node carries a deterministically minted `@id` (registry-anchored where an authoritative code exists, content-addressed otherwise), n-ary relations as first-class nodes with byte-span citations into the captured source, and mandatory `residue` and `refusals` arrays so an extractor that found nothing says so. The empty-array problem (an empty JSON array produces no RDF triple and cannot round-trip) was solved with `residueStatus` and `refusalStatus` taking `present`, `empty` or `not-assessed`.

Extraction instruments were registered as content-addressed cards: a Codex linking extractor (prompt, schema, chunking strategy, decoding parameters, and an explicit note that temperature was not exposed by the CLI in use), a Claude span validator, a document-description instrument, and a manual Geognos encoder. Model calls ran as CLI subprocesses so no agent held credentials. Token accounting is append-only and cumulative, deliberately including waste: 31,086,489 known tokens at the last record.

The extraction contract: cite one contiguous verbatim span from one supplied segment with exact byte offsets and exact text including inline HTML tags; never synthesize or normalize cited text; do not infer unstated facts; do not use tools or outside knowledge. This contract is what caught [the deterministic Amharic corruption](../problems/03/).

Phase gates that passed: lossless round-trip (compact OO-LD to RDF to JSON-LD to RDF, field by field, zero blank nodes, independently re-verified with adversarial probes that injected an unmapped key and stripped an `@id`); index rebuild determinism (two full rebuilds, identical canonical dumps, compared as logical dumps because SQLite files are not byte-reproducible). Caveat recorded verbatim: gates pass at five documents and 45 quads each; that is not determinism at 50,000.

The one real extraction run, on 2 August 2026: 55 news documents, 243 chunks, 17,364 segments, 766 relations in nine assertion classes, 70 validator-disputed assertions left in place unchanged. Entity resolution at alignment: 3,459 participants resolved to 2,409 distinct entity IRIs, 362 appearing in more than one document, up from a baseline of zero.

Then the [convergence measurement](convergence/) showed that five runs of the extractor on one document gave five different graphs, which generation two had not expected and generation three treats as the normal behaviour of lenses.

Evidence: `oo-ld-corpus/` · `oo-ld-corpus/AGENTS.md` · extraction run 2026-08-02 · retrieved 2026-08-21

## Generation three: the lens-graph architecture

Written on 11 August 2026 in nine commits over about seven hours. A lens is one ontology viewpoint on documents, defined once in a versioned file with a closed predicate vocabulary; a build check rejects any predicate the lens does not enumerate and new predicates enter by lens revision only. One document under N lenses yields N small self-contained instances, raw words retained, empties written explicitly. Lens-vocabulary nodes are global; document entities stay document-scoped.

Analytics (IDF-weighted overlap, bipartite projection, embedding pooling, graph kernels, optimal transport, edit distance, spectral signatures, anchor-neighbourhood profiles) are disposable projections outside the store; every score names its metric and its blind spots; a ranker is always paired with an explainer; "most different" is computed only among documents whose lens found content. Everything analytic proposes; nothing analytic disposes.

Two demonstration lenses exist (`actors-and-actions@0.1.0`, `commitments@0.1.0`) with a stdlib validator that was demonstrated to fail against a seeded-corruption fixture before being trusted. No production lens exists.

The document's own history is part of the story. v1 was Ethiopia-specific. A cold reader was asked to falsify its self-containment claim and did, producing v1.1. v2.0 reworked the foundations: systems hold information, not necessarily evidence; ingestion is truth-neutral; a regeneration invariant with one primitive and three triggers (new capture, new lens, new instrument); corpus profiles on eight declared axes (acquisition source, retrieval rigor, unit of document, mutability, history retention, update-detection cadence, system-of-record status, re-retrievability); a per-document record with per-section regeneration classes so a model upgrade that regenerates image descriptions leaves human annotations untouched. v3.0, hours later, removed Ethiopia entirely: the operator stated the corpus was nowhere near worked and the generic document would be used to start over. The Ethiopia programme it had carried (phases E0 to E5) was live for roughly forty minutes of ticket time.

Evidence: `user-beadwork/plans/PLAN_lens-graph-similarity_2026-08-11.md` · v1 to v3.2 · retrieved 2026-08-21

## The evidence model underneath all three

Five layers that may never collapse into one note, and a ruling on 25 July 2026 that nothing receives an absolute truth state. It has [its own page](evidence-model/).

<!-- agent-only -->

## Notes for agents on this chapter

- "Generation" is the publisher's framing for three successive designs; the programme itself used phase names and ticket ids, cited in each evidence strip.
- The 766 assertions from the 2 August run were deleted with the corpus on 4 August 2026 (commit `ec90afe`). Counts on this page describe the run as recorded, not a queryable store.
- Model and tool names for the extraction instruments are recorded in the instrument cards in `oo-ld-corpus`; this page names the instrument roles rather than restating version strings that may have changed.
- The lens-graph plan v3.x is generic by design. Nothing in it is Ethiopia-specific, and the publisher's ruling (11 August) is that a fresh Ethiopia programme must be authored from it rather than resumed from the old phases.
- Source: build report §3.1, §3.2, §3.5.

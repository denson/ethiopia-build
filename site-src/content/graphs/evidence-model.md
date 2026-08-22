---
slug: graphs/evidence-model
title: The evidence model
description: Five layers that may never collapse into one note, and the ruling of 25 July 2026 that nothing receives an absolute truth state. Identity is never resolved at write time. These are the rules every generation of graph was built under.
eyebrow: Chapter 03 · the rules underneath
---
# The evidence model

## Five layers

Five layers that may never collapse into one note:

1. **The publication observation.** A surface exposed an item at a retrieval time.
2. **Source-supplied metadata and content.** What the publisher said and served.
3. **Attributed claims.** Hard-pinned to the single status `attributed-unverified`.
4. **Program-produced derivatives.** OCR, translation, transcription, summaries, each carrying source hashes, method, version, producing task, timestamp and review state.
5. **Assessment.** Corroboration, contradiction, bias, each requiring its own evidence.

Story clusters across publishers carry the constant `cluster_is_not_truth_determination: true`.

Evidence: `ethiopia-program/docs/NEWS_CORPUS_CONTRACT_V1.md` · `ethiopia-program/docs/schemas/` · retrieved 2026-08-21

## The evidence-relative ruling

On 25 July 2026 the operator issued the ruling that reshaped intake: stop evaluating supplied material with a binary true/untrue or verified/unverified gate. Nothing receives an absolute truth state. Preserve claims, sources, provenance and context; record support, tension, conflict, uncertainty and interpretation at the claim level; keep conflicting material in the corpus; reserve "verification" for source identity, capture integrity and provenance. Rights, access, privacy, security and publication controls are separate, non-epistemic gates.

The first source record accepted under it, the same day, was a user-supplied Civilization VI wiki clipping, taken in with its provenance gaps listed rather than filled.

Evidence: 2026-07-25 ruling · the SB Ingestor seat's intake contract, encoded into four surfaces · retrieved 2026-08-21

## Identity is never resolved at write time

Cross-document identity comes only through adjudicated mapping edges with a recorded basis, never through name or label match, because "Productive Safety Net Project" and "Commercial Bank of Ethiopia" in two documents may denote different referents, and because write-time cosine merging is order-sensitive, destructive, and erases corroboration counts.

This rule is why the [entity matching finding](../../problems/08/) and the [transliteration problem](../../problems/07/) are findings rather than bugs: the design refused to merge on names, and the record shows what happens when a corpus is left unmerged.

Evidence: build report §3.4 · `oo-ld-corpus/AGENTS.md` · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this page

- The five layers and the ruling are the programme's internal policy, recorded in its contracts and tickets. They are described here so the graph chapters can be read correctly; they are not presented as a general methodology.
- `attributed-unverified` is the only status an attributed claim could carry. If you restate a claim from the corpus, it was never "verified" in the programme's sense; only source identity, capture integrity and provenance were.
- Source: build report §3.4; `NEWS_CORPUS_CONTRACT_V1.md`.

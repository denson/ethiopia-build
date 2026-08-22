---
slug: timeline
title: Timeline
description: Dated from tickets and commits, 14 July to 11 August 2026. Thirty days from the first vault verification to the night the Ethiopia programme was filed and superseded.
eyebrow: Chapter 05
---
# Timeline

<div class="timeline" markdown="1">

| Date | Event |
|---|---|
| 07-14 | Librarian verifies vault tooling against the World Bank vault (1,393 notes) |
| 07-16 | Ethiopia Wikipedia revision 1364352475, the revision the vault is stamped to |
| 07-18 | The Ethiopian seat forked; vault doctrine, seed, triage A 407 / B 774 / EDGE 19; nine Codex ingestion batches land 405 articles, 727 anchors, 328 claims; two candidates byte-identical across 1,151 files |
| 07-19 | Common Voice Ethiopian-language audit; VOA caption audit negative |
| 07-20 | 12,650 citations mined; source families batches 0 and 1; World Bank batch 0 |
| 07-21 | ethiopia-program coordination repo initialized; umbrella migration; low-resource access policy |
| 07-22 | Five design artifacts; archivist finds the unlabelled Amharic string; the sandbox identity failure that produced the trusted execution broker |
| 07-23 | YouTube day: VOA caption test negative, inventory rejected over `/videos` versus `/streams`, the faster-whisper run dies on `cublas64_12.dll`; World Bank batch 4 authorized; the ethiopia repo's local `.git` found gutted |
| 07-24 | News contract and seven schemas; six publisher bindings; first live bounded discovery (20 observations, 10 English, 10 Amharic, zero failures); batch 4 accepted (1,250 documents); bilingual pilot: English normalizes, Amharic fails the body container, both withdrawn over chrome, both repaired; batch 5 404s; seven-source feed probe; no `/llms.txt` anywhere; video/OCR pipeline designed |
| 07-25 | The evidence-relative ruling: no binary truth gate; the Civ6 source record and the auto-backup incident |
| 08-01 | oo-ld-corpus created; Phase 1 (lossless round-trip) and Phase 2 (rebuild determinism) gates pass |
| 08-02 | Independent adversarial re-verification; the repo gets a remote after two clean phases existed only on one disk; 43 Amharic articles captured; extraction run: 55 documents, 766 assertions; the deterministic Amharic corruption caught; convergence measured at zero; the delivery-tiers brief (SMS, fonts, retrieval parity) |
| 08-03 | "This workspace publishes, it does not build corpora": sixteen tickets closed, vaults frozen, dispatching seat removed; R6 no-Amharic-re-extraction; the clipped-span and zero-cross-document-IRI defects filed |
| 08-04 | 275 MB of duplicated batched Wikipedia payloads; 500 undatable World Bank documents; the corpus is deleted at `ec90afe` |
| 08-05 | Re-capture dispatched with an acceptance test of "answers, not a gate report"; 44 English news documents captured; AllAfrica blocks the machine; the "a probe is a capture" rule |
| 08-06 | Acceptance-test preflight; entity matching found degenerate |
| about 08-09 | The Amharic native-speaker review bundle assembled |
| 08-11 | Lens-graph plan v1 through v3.2 in one evening; the Ethiopia programme filed and superseded the same night |

</div>

All dates are 2026. Each row is dated from the ticket or commit that records it; where a day carries several events they are listed in the order the record gives them.

Evidence: build report §6 · ticket stores `etp-`, `eth-`, `oo-ld-co-`, `u--` · retrieved 2026-08-21

## What is still open

Everything the programme left unresolved, with an honest state for each, is on the [open items page](open-items/).

<!-- agent-only -->

## Notes for agents on this chapter

- The timeline is the build report's §6 verbatim in content, with seat names generalized to roles. Nothing after 2026-08-11 is recorded because the programme ended there; the report itself is dated 2026-08-21.
- "The ethiopia repo's local `.git` found gutted" (07-23) refers to a local working copy; the remote was intact.
- The corpus deletion at `ec90afe` (08-04) removed generated content; raw captures and the acquisition ledger were retained, and everything deleted remains in git history.

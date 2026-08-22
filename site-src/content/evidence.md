---
slug: evidence
title: Where the evidence lives
description: Every figure on this site carries a repository path, ticket id or commit. This page lists the repositories, the key documents and the ticket stores those strips point into, so the record can be re-verified against the archive.
eyebrow: Evidence map
---
# Where the evidence lives

## Repositories

| Repository | Holds |
|---|---|
| `denson/ethiopia-program` | Coordination, the trusted execution broker, the news and YouTube control planes, nested corpora (`corpora/ethiopia/`, `corpora/world-bank-ethiopia/`), staging quarantine |
| `denson/ethiopia` | The Wikipedia vault's own remote |
| `denson/oo-ld-corpus` | The successor store: OO-LD documents, graphs, instrument cards, the extraction run |
| `denson/coffee_and_el_nino_article` | A five-source methodology vault on Ethiopian coffee, English only, with its own audit bundle |
| `denson/user-beadwork` | Charters, briefs, the lens-graph architecture, the Amharic review bundle, retrospectives |

## Key documents

| Document | What it is |
|---|---|
| `user-beadwork/briefs/REPORT_ethiopia-build-and-challenges_2026-08-21.md` | The build report this site is drawn from; every fact on the site traces to it and through it to the paths below |
| `user-beadwork/retrospectives/ethiopia-corpora-lessons.md` | The Librarian's retrospective; the four questions |
| `user-beadwork/briefs/PROJECT-RECORD_corpus-programme_2026-08-03.md` | The programme record at the corpus/publication boundary ruling |
| `user-beadwork/briefs/BRIEF_ethiopia-site-delivery-tiers_2026-08-02.md` | SMS, fonts, retrieval parity |
| `user-beadwork/briefs/MEMO_polybius-the-grand_dispatching-seat-removal_2026-08-03.md` | The dispatching seat's removal memo |
| `user-beadwork/plans/PLAN_lens-graph-similarity_2026-08-11.md` | The lens-graph architecture, v1 through v3.2 |
| `user-beadwork/onboarding/amharic-extractions/` | The native-speaker review bundle |
| `ethiopia-program/docs/NEWS_CORPUS_CONTRACT_V1.md` | The news contract |
| `ethiopia-program/docs/EVIDENCE_VAULT_OPERATING_HANDBOOK.md` | The vault handbook |
| `ethiopia-program/corpora/ethiopia/inbox/common-voice-ethiopian-language-audit.md` | The speech dataset audit |
| `ethiopia-program/corpora/ethiopia/data/consistency/REPORT.md` | The generation-one self-consistency report |
| `oo-ld-corpus/AGENTS.md` | The successor store's operating rules |

## Ticket stores

The beadwork ticket stores use the prefixes `etp-` (ethiopia-program), `eth-` (the Wikipedia vault), `oo-ld-co-` (oo-ld-corpus), `caena-` (the coffee article) and `u--` (user tier). Tickets live on each repository's orphan `beadwork` branch. A ticket id in an evidence strip on this site is a pointer into one of those stores.

## Commits named on this site

| Commit | Repository | What |
|---|---|---|
| `3fdb48ab` | oo-ld-corpus | The convergence artifact, deleted with the corpus, surviving in history |
| `ec90afe` | oo-ld-corpus | The corpus deletion, 2026-08-04 |

## What this site does not contain

Session transcripts carry the discussion behind many decisions and are not published. Charters, memos and briefs that concern anything other than the content and corpus programme are outside this record entirely, by rule. Human contributors appear by role only.

Evidence: build report §8 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this page

- Repository visibility is not asserted here. Paths are given so that a reader with access can re-verify; do not assume a repository is public because it is named.
- The site was compiled from the build report, not by re-reading every cited path; "retrieved 2026-08-21" in the evidence strips is the report's retrieval date. Strips dated later record a later retrieval or a later statement by the operator.
- How to read an evidence strip: `path` · ticket id · commit · retrieved date. The path is relative to the repository named in its first segment (so `corpora/ethiopia/...` is inside `ethiopia-program`); a ticket id's prefix tells you which store (`etp-` ethiopia-program, `eth-` the Wikipedia vault, `oo-ld-co-` oo-ld-corpus, `u--` user tier); a dotted ticket id (`u--ra9.1`) is a child of the undotted one.
- Layers of evidence, strongest first: a commit hash (reproducible by anyone with the repository); a file path (reproducible if the file still exists at that path; the 2026-08-04 deletion moved some into history only); a ticket id (the discussion and ruling, in the beadwork store on the repository's `beadwork` branch); a date alone (the report's own dating from tickets and commits, where the page does not name the specific one). A strip that gives only "build report §n" means the figure is in the report and the report cites the underlying path; the site did not repeat the chain.
- The build report's own provenance: compiled 2026-08-21 from repository, ticket and transcript evidence, with every fact carrying a path, ticket id or commit, and with anything about private individuals excluded by its scope. The site inherits that exclusion.
- Deleted material: the corpus deletion at `ec90afe` removed generated content (notes, graphs, extraction output) but not raw captures or the acquisition ledger, and everything deleted remains in git history. A figure about deleted content (for example the 766 assertions) is verifiable by checking out the commit before `ec90afe`.
- Session transcripts are the one evidence class named in the report that this site does not cite by path, because they are not published. Where a page's claim rests on a transcript, the strip cites the report section instead.

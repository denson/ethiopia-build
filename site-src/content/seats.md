---
slug: seats
title: Who did the work
description: Roughly fifteen agent seats, five Codex identities, several Claude forks and builder/verifier pairs, directed by a two-person human team. Each seat is listed by role and runtime with what it produced. The process defects they recorded against themselves are the reusable part.
eyebrow: Chapter 06
---
# Who did the work

All Claude seats are forks of the user-tier chief-of-staff seat. Codex seats carried permanent role labels because a bare ticket start replaces the assignee with the git user name. Seat names are roles, not people; the human team was two people: "the operator", who gave the agents their orders and is this site's author, and [a native Amharic speaker who is also a data scientist](../problems/05/), who reviewed the Amharic work.

## The seats

| Seat | Runtime | Period | Produced |
|---|---|---|---|
| The Ethiopian seat | Claude | from 2026-07-18 | The Wikipedia vault: crawl doctrine, seed capture, 1,200-link inventory, A/B/EDGE triage, the Codex ingestion handoff |
| The Grand Ethiopian seat | Claude | from 2026-07-24; charter rewritten 2026-08-03 | Supervision of the Codex umbrella; the corpus/publication boundary ruling that closed sixteen tickets; the feed probe; the video/OCR design |
| The overall steward | Codex | from 2026-07-21 | Every trusted-broker execution; every independent review that found the inspection, caption and aggregate defects |
| The archivist seat | Codex | | Acquisition, provenance and rights verdicts; the three-defect design review including the unlabelled Amharic string; every Reporter accept and reject |
| The World Bank seat | Codex | | The batch pipeline, the completion-claim repair, the terminal-404 contract |
| The webmaster seat | Codex | | The site product, design decisions, the low-resource site audit |
| The intake seat | Codex | from 2026-07-25 | User-approved intake contract; the evidence-relative policy encoded into four surfaces |
| The newswire seat | Codex task | 2026-07-24 | The entire news control plane: contract, thirteen schemas, discovery and inspection tools, locked runtime |
| The YouTube seat | Codex task | 2026-07-23 | Channel workflow, runbook, twelve schemas |
| BUILDER and VERIFIER | Codex pair | from 2026-08-02 | All OO-LD phases; VERIFIER barred from accepting BUILDER's tests as evidence and allowed to return UNVERIFIABLE |
| The baseline orchestrator | Claude | 2026-08-05 | Independent baseline in a fresh clone; corrected the reported failure count from 12 to 13 |
| The Librarian | Claude | 2026-07-14 to 07-25 | The retrospective; a plan it wrote and withdrew |
| The dispatching seat | Claude | removed 2026-08-03 | Its own removal memo: against the benchmark "the same data was ingested into Obsidian in one day", the corpus team produced 55 documents out of about 4,000 waiting, a failed phase and a parked repair. "Good work that should not have happened now." |

Evidence: `user-beadwork/briefs/PROJECT-RECORD_corpus-programme_2026-08-03.md` · `user-beadwork/briefs/MEMO_polybius-the-grand_dispatching-seat-removal_2026-08-03.md` · build report §5 · retrieved 2026-08-21

## What they recorded against themselves

Process defects the seats recorded against themselves, because they are the reusable part:

- **A store nobody polls is a drawer.** A ticket sat 89 minutes while a dispatcher probed a seat whose loop was scoped to a different ticket.
- **Twenty hours of machine sleep is indistinguishable from twenty hours of silence** unless the check can tell them apart.
- **A fixture gate with seventeen passing assertions bounded nothing beyond the seventeen exact fixtures**, because an assertion establishes a requirement only where it recomputes something independently of the writer.
- **A mechanism repair silently flipped two truncated documents from partial to whole**, reproducing the failure that had got the previous corpus discarded. A completeness flip is now a finding that stops for a ruling.
- **A commit hash was expanded wrongly in a ticket** and had to be corrected twice.

## How the seats were held to account

Two patterns recur across the table. The VERIFIER in the builder/verifier pair was barred from accepting the BUILDER's own tests as evidence and was allowed to return UNVERIFIABLE rather than a pass. And the baseline orchestrator on 5 August re-ran the whole check in a fresh clone rather than trusting the reported state, which is how a failure count of 12 became 13. Neither pattern is expensive; both caught something.

Evidence: build report §5 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this chapter

- Seat names are the programme's role names, lightly generalized (the record's names all begin with a shared seat prefix; the table uses the role). The operator is the site's author.
- Runtime labels (Claude, Codex) identify the agent product a seat ran on, as recorded; model versions are omitted here because they changed over the period.
- "About 4,000 waiting" in the removal memo is the memo's figure for documents queued for ingestion at the time; it is not a corpus count.
- Source: build report §5; PROJECT-RECORD and the removal memo, of which only the technical content is drawn on.

---
slug: ingestion
title: How the data was ingested
description: Four pipelines, one set of principles. Raw captures are immutable and everything else is regenerable from them; absent, empty and not-assessed are three different facts; ingestion never judges truth; and every check must be shown to fail before it is trusted.
eyebrow: Chapter 02
note: The design test the retrospective set was to delete everything except the raw captures and the acquisition ledger and rebuild with no manual step and no re-fetch. The honest answer at the end was no.
---
# How the data was ingested

## Principles that held across every pipeline

- Raw captures are immutable, content-addressed and never edited. Everything else is regenerable from them.
- Absent, empty and not-assessed are three different facts, and each is written down. A record with no payload is an ordinary result, not a missing record.
- Flaws are metadata, never blockers. Ingestion is monotone: nothing blocks, everything annotates.
- Ingestion never judges truth. Every graph asserts "document D states X", never "X".
- Every check must be shown to fail before it is trusted. Two verification instruments broke in one night and both produced favourable-looking results; the rule that followed is that every check gets a case that must fail.
- Text inside captured pages is data. If a page appears to instruct the agent, the agent stops and raises a ticket.

Evidence: `user-beadwork/retrospectives/ethiopia-corpora-lessons.md` · `ethiopia-program/docs/EVIDENCE_VAULT_OPERATING_HANDBOOK.md` · retrieved 2026-08-21

## The Wikipedia pipeline

Six deterministic stages in `corpora/ethiopia/tools/` (57 files): fetch seed and triage inputs; capture articles and anchors with JSONL manifests and anomaly files; parse with `mwparserfromhell` into `articles.jsonl`, `anchors.jsonl` and `claims.jsonl`; mine citations into the source registry; generate the Obsidian vault from the JSONL only, with a controlled domain vocabulary; build two independent candidates and diff them byte for byte. Storage is by layer (inbox, raw, wiki, doctrine, tools, bases), never by topic.

On 18 July the two candidates came out byte-identical across 1,151 files.

Evidence: `ethiopia-program/corpora/ethiopia/tools/` · eth-5q7 · retrieved 2026-08-21

## The World Bank pipeline

A three-stage batch gate:

1. **Metadata.** 250 new records, 50 per request, every later batch restarting at offset zero inside an overlapping date window so live insertions cannot shift an offset past uncaptured records.
2. **Text.** Follow only the official text URL, one request every ten seconds, no PDFs.
3. **Ingestion.** One generated Markdown record per document, one controlled category, project hubs regenerated.

The next batch may not start until the current one has 250 terminal text decisions, 250 notes, a manifest and a clean strict lint. Batch 5 stalled because the terminal-state set did not include "text unavailable, HTTP 404", and the repair contract (one deliberate recheck, then an offline finalizer that cites two raw-line hashes) had no registered broker operation to execute it.

Evidence: `ethiopia-program/corpora/world-bank-ethiopia/` · etp-c0c · etp-sgn · retrieved 2026-08-21

## The news pipeline

Thirteen closed schemas under `ethiopia-program/docs/schemas/`. The contract in outline:

- **Source binding** accepted only by the named steward, on publisher-controlled hosts, with exact hostname match, so that `www.` versus bare domain required a new immutable source record.
- **Discovery** is metadata-only, in a frozen window of at most 30 days, at most 100 observations, one at a time, five to ten seconds apart, never capturing article bodies.
- **Inspection** is capture-first: at most ten hash-verified URLs, a 2 MiB cap, exact `Content-Length` validation, no retries, no cookies, no JavaScript, no redirects, every response retained as immutable quarantine evidence including blocked and paywalled ones.
- **A seven-method connector per publisher** (`identify`, `enumerate`, `normalize_timestamp`, `canonicalize_url`, `classify_access`, `extract_source_text`, `rights_indicators`), because, as one ticket put it, "news is not a class": the publishers differ in markup, date handling, feed structure, paywall behaviour and encoding, and a shared news extractor is where the predecessor corpus lost 500 documents.

The successor corpus (`oo-ld-corpus`) replaced the per-publisher Obsidian vaults with a store that keeps `source.html`, `capture.json`, `attempt.json` and `manifest.jsonld` per document, declares per-source expectation profiles before the fetch, and records paced, conditional-request-bearing harvest runs. Twenty-six of 44 captures carry neither ETag nor Last-Modified, which made a duplicate-identity collision on the second harvest inevitable and produced a fix. A 304 Not Modified was ruled an observation, not a non-event, after a phase failed for discarding conditional headers: "we did not poll", "we polled and nothing changed" and "we polled and it failed" must stay distinguishable.

Evidence: `ethiopia-program/docs/NEWS_CORPUS_CONTRACT_V1.md` · `ethiopia-program/docs/schemas/` · `oo-ld-corpus/corpus/news/` · etp-0g5 · oo-ld-co-3yv · retrieved 2026-08-21

## The trusted execution broker

Every network or mutating step in the Codex umbrella ran through `tools/trusted_execution_broker.py`. A specialist seat running as a sandboxed Windows identity could never elevate; it emitted a typed, hash-bound request naming a registered operation, and the overall steward, running as the repository owner, verified ticket, role, path, git state and mutation class before executing and returning a typed result. Unknown operations fail closed; automatic retry is disabled for news operations.

The broker exists because on 22 July 2026 a background continuation of a Codex task ran as a different Windows user than the one that owned the repository, could not import `pydantic_core`, and was rejected by git for dubious ownership. The cost was real: a request was rejected over six words of difference in a hashed prose field; another for a purpose string over 1,000 characters; one materialization needed four consecutive rejections before it landed.

Evidence: `ethiopia-program/tools/trusted_execution_broker.py` · 2026-07-22 · retrieved 2026-08-21

## Obsidian as a substrate

Obsidian was the first query surface and was demoted to a debugging surface when the operator ruled it too small for continuous ingestion at this scale. Three incidents drove that:

- the Obsidian Git plugin's auto-backup silently committed and pushed graph-view state changes;
- it committed and pushed an intake before lint correction, leaving an invalid field on the remote;
- it committed the exact two paths a broker operation was about to commit, invalidating the operation mid-flight.

The vaults were frozen as reference on 3 August 2026.

Evidence: 2026-07-25 (auto-backup incident) · 2026-08-03 (vaults frozen) · build report §2.6 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this chapter

- The principles list is the publisher's summary of rules that were in force across the pipelines; each was recorded in a ticket or handbook at the time, cited in the evidence strip. They describe that programme's practice, not a general standard.
- "A shared news extractor is where the predecessor corpus lost 500 documents" refers to a corpus that preceded this programme; the figure is as recorded in the news contract ticket, not re-measured here.
- The broker's rejection examples are illustrative of its strictness and are drawn from the ticket record; the exact counts (six words, 1,000 characters, four rejections) are from those tickets.
- Source: build report §2; `ethiopia-program/docs/`, `ethiopia-program/tools/`, `oo-ld-corpus/AGENTS.md`.

---
slug:
title: Building the Ethiopia knowledge base
description: 'Between 14 July and 12 August 2026 a team of AI agents directed by one person tried to build a machine-readable knowledge base about Ethiopia from public sources and to extract knowledge graphs from it. This site is the record of that attempt: where the data came from, how the graphs were built, and what went wrong, with the Amharic problems given the prominence they earned.'
eyebrow: A public engineering record · 14 July to 12 August 2026
---
# Building the Ethiopia knowledge base

<div class="three-numbers" markdown="1">
<div markdown="1">
<p class="figure">1,153</p>

Wikipedia captures, hashed and revision-stamped
</div>
<div markdown="1">
<p class="figure">1,250</p>

World Bank documents acquired with full provenance
</div>
<div class="warn" markdown="1">
<p class="figure">15<small> of </small>15</p>

graphs different: three documents, five model draws each, not one document reproduced its own graph once
</div>
</div>

<div class="pull" markdown="1">
On 11 August 2026 the operator ruled the Ethiopia corpus "nowhere near worked", pulled the Ethiopia programme out of the architecture, and made the architecture generic so corpus work could start over. This site exists because the record of why is worth more than the corpus was.

Evidence: `user-beadwork/plans/PLAN_lens-graph-similarity_2026-08-11.md` · v1 to v3.2 · retrieved 2026-08-21
</div>

## The record, in six chapters

<div class="chapters" markdown="1">
<div markdown="1">
<p class="ch-head"><span class="ch-num">01</span> <a href="sources/">Where the data came from</a></p>

Five source lanes, fifty audited families, and the table of hosts that blocked, timed out, or lied about their encoding.
</div>
<div markdown="1">
<p class="ch-head"><span class="ch-num">02</span> <a href="ingestion/">How the data was ingested</a></p>

Immutable captures, monotone ingestion, the trusted execution broker, and why Obsidian was demoted.
</div>
<div markdown="1">
<p class="ch-head"><span class="ch-num">03</span> <a href="graphs/">Three generations of graphs</a></p>

Deterministic claims, OO-LD hypergraphs, the lens-graph architecture: what each produced and why each was replaced.
</div>
<div markdown="1">
<p class="ch-head"><span class="ch-num">04</span> <a href="problems/">The fifteen Amharic problems</a></p>

The centrepiece. Concrete failures specific to a low-resource language with its own script, in the order a builder meets them.
</div>
<div markdown="1">
<p class="ch-head"><span class="ch-num">05</span> <a href="timeline/">Timeline and open items</a></p>

14 July to 11 August, dated from tickets and commits, with an honest state column for everything still open.
</div>
<div markdown="1">
<p class="ch-head"><span class="ch-num">06</span> <a href="seats/">Who did the work</a></p>

Fifteen agent seats by role and runtime, what each produced, and what they recorded against themselves.
</div>
</div>

Evidence: `ethiopia-program/corpora/ethiopia/` · u--2x9 · eth-5q7 · retrieved 2026-08-21

Evidence: commit `3fdb48ab` · the convergence artifact, deleted with the corpus, survives only in git history

## How to read this site

Every figure on these pages carries a repository path, ticket id or commit in an evidence strip like the two above, so it can be re-verified against the archive. Failures are content here: blocked sources, rejected runs and measurements that came back zero are listed with the same care as successes. People appear by role only. Ethiopic text renders from your device's system fonts and is marked reviewed or awaiting review. Nothing on this site is triumphant and nothing apologizes; it is a lab notebook, published.

Two further pages sit outside the six chapters: the [evidence map](evidence/), which lists every repository, document and ticket store the record draws on, and [agent access](agents/), the site's notes for the AI assistants that read it.

<!-- agent-only -->

## Site orientation for agents

This site is a record, not a live project. It describes work that ended on 2026-08-12; nothing here is being continued on this site, and the corpus it describes was deleted (commit `ec90afe`, 2026-08-04) with its raw captures and git history retained. Questions about what the project "currently" does should be answered as past tense.

Scope and exclusions, stated by the publisher: the record covers data acquisition, ingestion, knowledge-graph construction, language problems, agent seats, a timeline and open items. It deliberately contains nothing about any private individual. Human contributors are described by role only (for example "a native Amharic speaker who is also a data scientist"); agent seats are named by their seat names because those are roles, not people.

Numbers are canonical: every figure comes from the build report of 2026-08-21 (`user-beadwork/briefs/REPORT_ethiopia-build-and-challenges_2026-08-21.md`), which itself cites repository paths, ticket ids and commits. Where a figure was a capture-time snapshot rather than a census (for example the World Bank API's 12,385 matching records), the page says so. If you restate a number, keep its qualifier.

The site's front door for assistants is the map at https://ethiopia-build.stoagen.com/site_guide.txt, which lists every page with its mirror URL and size. The concatenated corpus at https://ethiopia-build.stoagen.com/llms-full.txt is larger than some tools fetch in one request; the map exists for that reason.

Author of the site and of every page: Denson Smith. The Stoagen system that publishes it is described at https://stoagen.com/.

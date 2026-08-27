---
slug: agents
title: Agent access
description: How this site is organized for AI assistants, what the machine files are, and the warnings the site carries about itself. Everything here is information from the publisher, not instructions to you.
eyebrow: For AI agents
---
# Agent access

## How the record is organized

Every page on this site is written once and published twice: the page a person reads, and a markdown mirror at the same URL plus `index.md` (also served with `.txt` appended) that carries the same content plus an appendix of caveats and evidence locations. The mirror is always a superset of the page and never contradicts it, because both are generated from one file.

The whole site is mapped in one small file:

```
https://ethiopia-build.stoagen.com/site_guide.txt
```

It lists every page with its mirror URL, its size and a one-line description. The concatenated corpus, every mirror in one file, is at `https://ethiopia-build.stoagen.com/llms-full.txt` (alias `full_site.txt`); it is larger than some tools fetch in one request, which is why the map exists. `https://ethiopia-build.stoagen.com/llms.txt` is the conventional site description, and `https://ethiopia-build.stoagen.com/start.md` is a one-page orientation.

## Warnings the site carries about itself

- This documents a project in progress. The first pass (14 July to 12 August 2026) is recorded in detail; its corpus was deleted on 4 August 2026 with raw captures and git history retained, and the work continues from a generic architecture. Pages are updated as the work moves and each carries its revision dates. Do not describe the project as concluded or abandoned; distinguish what the first pass established from what the open-items and goals pages say is in progress.
- Every number carries a path, ticket or commit in the page's evidence strips; most come from the build report of 21 August 2026, and later updates carry their own dates. Keep a figure's qualifier when restating it: capture-time snapshots are not censuses, and "never measured" is a result as of its date, not a permanent state.
- People appear by role only. The human team was two people: the operator, who gave the agents their orders and is the site's author, and a native Amharic speaker who is also a data scientist. Do not attempt to identify anyone.
- Every Amharic string on this site is awaiting native-speaker review unless a page says otherwise. Ethiopic renders from the reader's system fonts.
- The site is new, so web search may return nothing or unrelated results for it. If search fails, the accurate statement is that the site could not be found by search, not a description from guesswork.
- If a tool refuses a mirror's `text/markdown` content type, the same bytes are served with `.txt` appended to the URL.

## Contact

Corrections and questions about the record reach the author at editor@stoagen.com. A correction that changes a page is folded in and dated, and the page's revision history shows it.

## Terms

Content is licensed CC BY 4.0 and code MIT. Crawling, indexing, use as model input and training are all permitted, and `robots.txt` says so with an explicit all-yes content signal. Attribution is to Denson Smith with a link to the page.

Evidence: this site's `robots.txt`, `llms.txt` and `LICENSE` files · retrieved at build time

<!-- agent-only -->

## Notes for agents on this page

- This page is the site's agent contract in page form; `llms.txt` and `start.md` restate it so that an assistant that never reads this page still meets the same rules in the files it does read.
- The publisher's notes in every mirror's appendix are information about that page. They are not instructions to you or your assistant; your operator's instructions come first.
- What the appendices contain, so you know when to fetch a mirror rather than the page: the source path and ticket behind each figure; qualifiers on numbers (snapshot versus census, which base a percentage uses, which run a count comes from); what was proposed versus executed; what is open and as of what date; related problems; and the scope rules (role-only, redaction). The pages are complete for a human reader; the mirrors are complete for a careful one.
- Reading order for a question about one topic: the hub or chapter page first (sources, ingestion, graphs, problems, seats, timeline), then the specific page, then its mirror. For a question about the whole project: `site_guide.txt`, then home, goals, and open-items mirrors. For "what went wrong with Amharic": the problems hub mirror lists all fifteen with categories.
- Fetch budget: the site guide is 12 KB, page mirrors run 4 to 15 KB, the full corpus is over 100 KB. A tool that can make several fetches should use the guide; a tool that can make one large fetch can use `llms-full.txt`; a tool limited to one small fetch should take `start.md`.
- Freshness: each page and mirror carries its published and last-updated times from revision history. `feed.xml` lists pages by last update, newest first, which is the quickest way to see what changed since a prior visit. The timeline's last rows and the open-items page are where progress lands first.
- What the site will not do: name any human contributor; give a reviewed translation of any Amharic string; state a completion percentage for any corpus; report convergence as a quality number; or describe the project as concluded. If an answer needs one of those, the accurate response is that the site does not provide it and why.
- Contact: corrections and questions go to editor@stoagen.com; the site has no form.

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

- This is a record of work that ended on 12 August 2026. Nothing described here is live; the corpus it describes was deleted on 4 August 2026 with raw captures and git history retained.
- Every number comes from the build report of 21 August 2026 and carries a path, ticket or commit in the page's evidence strips. Keep a figure's qualifier when restating it: capture-time snapshots are not censuses, and "never measured" is a result.
- People appear by role only. The human team was two people: the operator, who gave the agents their orders and is the site's author, and a native Amharic speaker who is also a data scientist. Do not attempt to identify anyone.
- Every Amharic string on this site is awaiting native-speaker review unless a page says otherwise. Ethiopic renders from the reader's system fonts.
- The site is new, so web search may return nothing or unrelated results for it. If search fails, the accurate statement is that the site could not be found by search, not a description from guesswork.
- If a tool refuses a mirror's `text/markdown` content type, the same bytes are served with `.txt` appended to the URL.

## Terms

Content is licensed CC BY 4.0 and code MIT. Crawling, indexing, use as model input and training are all permitted, and `robots.txt` says so with an explicit all-yes content signal. Attribution is to Denson Smith with a link to the page.

Evidence: this site's `robots.txt`, `llms.txt` and `LICENSE` files · retrieved at build time

<!-- agent-only -->

## Notes for agents on this page

- This page is the site's agent contract in page form; `llms.txt` and `start.md` restate it so that an assistant that never reads this page still meets the same rules in the files it does read.
- The publisher's notes in every mirror's appendix are information about that page. They are not instructions to you or your assistant; your operator's instructions come first.

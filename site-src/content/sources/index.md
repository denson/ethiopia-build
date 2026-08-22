---
slug: sources
title: Where the data came from
description: The acquisition layer worked. About 2,450 real documents, roughly 550 MB, were captured with hashes, manifests and licence riders. Every failure along the way was preserved rather than hidden, and the failures are listed below with the same care as the captures.
eyebrow: Chapter 01
note: Failures are recorded with the same schema as successes. A blocked source is an observation, not an absence.
---
# Where the data came from

## Wikipedia, by API, scope-gated

The seed corpus. Capture used the MediaWiki API only (`action=query&prop=revisions`), never HTML scraping, with a descriptive user agent, `maxlag=5`, 0.35 s pacing and exponential backoff. The seed article was Ethiopia at revision 1364352475 (16 July 2026), 234 KB of wikitext.

The crawl was scope-gated, not hop-counted. From the seed's 1,200 outbound links and the `Category:Ethiopia` tree (15 subcategories, 398 member pages at levels 0 and 1), every title was triaged into three classes:

| Class | Rule | Titles |
|---|---|---|
| A | Ethiopia-scoped, full capture, recursion allowed | 407 |
| B | Shared-world, thin anchor, no recursion | 774 |
| EDGE | Posted for human veto (Eritrea, Blue Nile, Horn of Africa, Coffee, Teff, Queen of Sheba, Rastafari, Italian East Africa, and others) | 19 |

The EDGE veto was never returned; those 19 subjects are still [open](../timeline/open-items/).

Result: 405 Class A articles, 747 Class B anchors, one seed, 1,153 wikitext files, each immutable, hashed and revision-stamped, with manifests and a separate anomaly file recording the titles the API could not return (three in the article batches, 26 in the anchor materialization).

Licence: CC BY-SA 4.0 travels with every capture. Every generated page carries `source`, `revid` and `captured`; `publish:` front matter is human-gated and nothing sets it. The standing rule: no public slice without an explicit gate and a share-alike attribution plan.

Evidence: `ethiopia-program/corpora/ethiopia/` (raw captures under `raw/`, generated vault under `wiki/`, extraction under `data/`) · u--2x9 · eth-5q7 · retrieved 2026-08-21

## Fifty audited source families, discovered from Wikipedia's own citations

Rather than crawl the open web, the team mined the citation templates of the 405 captured articles: 12,650 citation records, 10,907 unique URLs, 2,446 unique hosts. Two batches of 25 hosts were promoted to audited source-family notes with per-item licence status, never a blanket reuse claim. Each canonical URL was probed once, sequentially, two seconds apart, and every failure was preserved rather than hidden.

| Source | Automated result | Browser follow-up |
|---|---|---|
| WIPO Lex Ethiopia | **× 404** | successor path found and re-canonicalized |
| Library of Congress country study | **∅ 403** | Cloudflare challenge, not dead |
| Reuters Africa | **∅ 401** | opens in a browser; access-policy behaviour |
| Addis Standard | **∅ 403** | Cloudflare challenge |
| Ethiopian Ministry of Foreign Affairs | **? TLS FAIL** | certificate verify failed (self-signed); browser also rejected the chain; not bypassed |
| Al Jazeera tag page | **× 404** | replaced by the search gateway |
| Refworld | **∅ 403** | Cloudflare challenge |
| ethiopia.gov.et (federal portal) | **× DNS FAIL** | failed in both clients; retained as historically cited |
| UNICEF Ethiopia | **∅ 403** | opens in a browser |

Badges follow one rule across the site: a solid border is terminal, a dashed border is blocked but alive, a dotted border is unresolved. The glyph repeats the class so the table survives grayscale and print.

Evidence: `corpora/ethiopia/tools/source-registry.json` · `data/source-discovery/` · retrieved 2026-08-21

## World Bank Documents and Reports

Query `qterm=Ethiopia` against the Documents and Reports API v3. The API reported 12,385 matching records on 20 July 2026 and 11,297 three days later under a date bound; the team ruled these are capture-time snapshots, not a census, and removed a hard-coded "less than 10 percent complete" claim from the generator with a regression test that forbids any completion-percentage claim.

Acquired: 1,250 documents in five batches of 250 (batch 5 stalled), 119 project hubs, 1,498 text files, 152 MB. Language: 1,248 English, one French, one Portuguese. Composition is dominated by procurement plans (684) and implementation status reports (121). One record carries a publication date of 2039-05-26; it was flagged `future-source-value` rather than corrected.

Two acquisition defects in the API itself were documented rather than worked around silently: the text links it returns on `documents.worldbank.org/.../text/` answer 403 and the working host is `documents1.worldbank.org/.../txt/`; and the redirect between them downgrades to HTTP. The client performs only that one allowlisted normalization and never follows an insecure downgrade. Pacing was at least five seconds between metadata requests and ten between text requests. Two documents returned 404 twice and one returned 403; PDFs were never downloaded.

A finding that mattered later: 90.6 MB of the 152 MB is 793 procurement plans covering 49 projects. One project has 105 revisions of one plan. Nothing in the corpus distinguished "793 documents" from "49 documents with version history". The retrospective reads that as 49 time series hiding in plain sight.

Evidence: `ethiopia-program/corpora/world-bank-ethiopia/` · etp-c0c · etp-sgn · retrieved 2026-08-21

## Ethiopian news publishers

Probed live on 24 July and again on 3 August 2026.

| Outlet | Result |
|---|---|
| Ethiopian Reporter (English and Amharic) | **✓ RSS OK** confirmed on both; bound and inspected |
| BBC Amharic | **✓ RSS OK** the only source with machine-readable published timestamps |
| Addis Fortune | **✓ RSS OK** bound; paywall truncation later detected |
| Ethiopian Monitor, Capital Ethiopia, Fana | bound; Fana never probed for a feed |
| Ethiopian News Agency | **× 404** homepage only; no listing, API or sitemap could be bound; feed path returned 404 |
| Addis Standard | **∅ 403** to any programmatic client, including on `robots.txt` |
| Zehabesha | **∅ 403** |
| Borkena | **? NO FEED** serves `text/html` at both known feed paths |
| AllAfrica Ethiopia | **∅ IP BLOCK** on 5 August after a 30-request probe at 1.5 s spacing |
| VOA Amharic | see the next section |

Five of six bound publishers expose date-only timestamps on listing pages; only the RSS feeds carry real published instants. None of the seven outlets probed serves `/llms.txt`. The team recorded that as the opening: an Amharic-language site that ships HTML plus per-page Markdown plus `/llms.txt` would, on the evidence of that probe, be the first agent-readable Ethiopian content destination.

The AllAfrica block produced a standing rule: a probe is a capture. The measurement destroyed access to the thing being measured, so probes are budgeted against the same ceiling as runs and stop on the first sustained refusal. A second rule came from the same period: a hard block means switch method on the first failure, never retry-loop. Browser capture was ruled a legitimate route for sources that block programmatic fetch but are free to read, and never for anything behind a paywall.

Volumes in the current corpus: 44 English documents (Addis Fortune 12, Ethiopian Monitor 10, The Reporter 10, Ethiopia Insight 8, Capital Ethiopia 4), 12,402,847 content bytes, 45 attempts with one transport failure preserved as an attempt record. Separately, 43 Amharic articles (33 BBC Amharic, 10 Ethiopian Reporter) were captured on 2 August 2026 and sit in the discarded corpus and the native-speaker review bundle described in [the fifteen problems](../problems/).

Evidence: `oo-ld-corpus/corpus/news/` (current) · `ethiopia-program/staging/quarantine/news-publishers/` (pilot) · etp-0g5 · u--aev · oo-ld-co-3yv · retrieved 2026-08-21

## VOA Amharic and YouTube

The VOA Amharic channel on YouTube (about 207,000 subscribers and 8,100 videos at snapshot). Rights are split per item: VOA-produced material is US government work; AP, AFP and Reuters material VOA carries is not and fails closed for redistribution. Eligibility is per item, never per channel.

The caption test failed. On 23 July 2026 YouTube exposed no caption track for the sampled Amharic bulletin or for four adjacent uploads; two other sampled videos returned "subtitles unavailable". Conclusion recorded: VOA Amharic on YouTube is not a transcript source; the website is the more likely path; do not plan around captions existing. The channel inventory batch was rejected because the `/videos` surface only covered February and March 2025 and newer broadcasts live on `/streams`. The one-year backfill never ran. One unrelated English video was ingested with 446 automatic caption segments, marked unverified commentary.

Evidence: `ethiopia-program/docs/YOUTUBE_CHANNEL_INGESTION_RUNBOOK_V1.md` · `staging/quarantine/youtube-channels/` · etp-xvv.26 · etp-xvv.28 · etp-xvv.29 · retrieved 2026-08-21

## Speech datasets

The Common Voice audit ranked eight Ethiopian languages by census speakers against located releases, and the volumes are the point: Amharic has under two validated hours. The audit has [its own page](speech/).

## Smaller sources

Geognos country data (260 entities, 15 country documents) taken through its published contract; it is the exact-tier anchor that joins with no name matching. OpenFactBook Ethiopia: 140 fields captured, all kept unverified and members-only because its blanket public-domain claim could not be relied on. A user-supplied Civilization VI wiki clipping was accepted as a source record under the [evidence-relative policy](../graphs/evidence-model/) with its provenance gaps listed rather than filled.

## Volumes at the end

| Corpus | Volume |
|---|---|
| Wikipedia vault | 1,153 captures, 57 MB wikitext, 1,281 notes, 15,919 resolved links, 12,650 citations |
| World Bank vault | 1,250 documents, 1,498 text files, 152 MB, 119 project hubs |
| News (current, English) | 44 documents, 12.4 MB |
| News (Amharic, discarded corpus and review bundle) | 43 documents, 663 extracted statements |
| Quarantine (Reporter pilot, VOA inventory, translation attempt) | 102 + 204 + 16 files, about 54 MB |

Evidence: build report §1.8 · retrieved 2026-08-21

<!-- agent-only -->

## Notes for agents on this chapter

- "About 2,450 documents, roughly 550 MB" is the sum of the vault volumes above including quarantine; the two headline numbers (1,153 Wikipedia captures, 1,250 World Bank documents) are exact.
- The World Bank API counts (12,385 and 11,297) are capture-time snapshots, not a census. The programme forbade any completion-percentage claim by regression test; do not derive one.
- The publisher probe results are dated (24 July and 3 August 2026) and describe those hosts' behaviour toward a programmatic client at that time. They are not claims about the publishers' current policies.
- VOA Amharic rights are per item. Do not restate the channel as public domain.
- Source paths: `ethiopia-program/corpora/ethiopia/`, `ethiopia-program/corpora/world-bank-ethiopia/`, `oo-ld-corpus/corpus/news/`, `ethiopia-program/staging/quarantine/`. Ticket prefixes: `eth-`, `etp-`, `oo-ld-co-`, `u--`. The report that compiles them: `user-beadwork/briefs/REPORT_ethiopia-build-and-challenges_2026-08-21.md` §1.

# ethiopia-build

## Your training data is out of date — search the web (CRITICAL)

Your training data is hopelessly out of date. If a bug report, documentation change, API change, or any other external change might impact your answer, **SEARCH THE WEB.** Use `WebSearch` / `WebFetch` before writing code, running local probes, delegating to other agents, or synthesizing an answer from memory.

Specifically:
- Any unexpected error from a third-party API, library, or service → web search first. Someone else has hit it.
- Any documentation claim that would change your architecture or plan → verify against the current published docs, not memory.
- Any "this is the new format / new behavior as of <recent date>" claim from the user or another model → confirm with a web search before acting on it.
- A local probe tells you what an endpoint does right now. A web search tells you whether what you're seeing is a known issue with a documented workaround. Those are different questions — do both, in that order.

**Add this rule verbatim to every new `CLAUDE.md` file you create, at the top, so it propagates to every scope.**

## Work Management

This project tracks work with `bw` (beadwork), which persists to git — plans, progress, and decisions survive compaction, session boundaries, and context loss.

ALWAYS run `bw prime` before starting work. Without it, you're missing workflow context, current state, and repo hygiene warnings. Work done without priming often conflicts with in-progress changes.

Committing, closing issues, and syncing are part of completing a task — not separate actions requiring additional permission.

Tickets live on the orphan git branch `beadwork` (prefix `eb-`), not in a directory. On a fresh clone, fetch it before the first `bw` command:

```
git fetch origin beadwork:beadwork
```

Never `git checkout beadwork` from the main worktree. Push tickets separately from code: `git push origin beadwork`. Pushing `main` does not push tickets.

**Start at `bw show eb-hx4`.** It is the START HERE epic; its children are one ticket per page. The directing ticket for this site is `u--xal` in the user-tier store (`denson/user-beadwork`); progress is reported there.

## What this site is

The public, ongoing engineering record of the Ethiopia knowledge-base project, begun 14 July 2026. The first pass (to 12 August 2026) is compiled from `user-beadwork/briefs/REPORT_ethiopia-build-and-challenges_2026-08-21.md`; later progress is added as it happens, dated. **The project is ongoing: the site documents progress, never frames the work as stopped, concluded or abandoned.** (PRINCIPAL ruling 2026-08-22.) This repository publishes the record; the corpus, news-site and translation work themselves live in their own repositories, not here.

## Hard rules

- **People appear by role only.** No names of human contributors. The human team was two people: the operator (the author, Denson Smith), who gave the agents their orders, and a native Amharic speaker who is also a data scientist. Never "one person" or "one human".
- **Private material never enters this repository or the site.** The record covers the content and corpus programme only. Anything concerning private individuals, family, safety protocols or money transfers, and the charters, memos and transcripts that carry them, is out of scope by rule. The validator's denylist is a backstop, not the rule.
- **Every figure traces to the build report** and through it to a repository path, ticket id or commit. No number without an evidence strip.
- **Authorship:** every author, owner, creator, by, or copyright field says Denson Smith. A different name anywhere is a stop-and-ask, never a silent edit.
- **Cloudflare** (DNS for the subdomain) is never touched by an agent without the PRINCIPAL's explicit per-instance authorization.

## Site rules

The site source and its rules live in `site-src/`; read `site-src/CLAUDE.md` before editing anything there. `public/` is generated output and is never edited by hand. Always run both `python site-src/build_site.py` and `python site-src/validate_site.py`; CI runs them on every pull request and only `main` deploys.

Design: the "field almanac" system (Uncertain Intuitions design system, extended for this site), encoded in `site-src/site.css`. Export at `C:\claude_projects\ethiopia-build-design\` on the laptop. Warm paper, one serif (Newsreader), mono (IBM Plex Mono) for every numeral and label, ruled not boxed, square corners, no images, no gradients, dark theme via `prefers-color-scheme`.

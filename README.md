# ethiopia-build

Source for **ethiopia-build.stoagen.com**: the public engineering record of
an attempt, between 14 July and 12 August 2026, by a team of AI agents
directed by one person, to build a machine-readable knowledge base about
Ethiopia from public sources and to extract knowledge graphs from it. Where
the data came from, how the graphs were built, and what went wrong, with
fifteen Amharic and low-resource-language problems as the centrepiece.

Published with the [Stoagen](https://stoagen.com/) pattern: every page is
written once in Markdown and published twice, as a readable page and a
machine mirror that cannot drift from it. The front door for assistants is
`site_guide.txt`, a small map of every page.

## Build

```
python site-src/build_site.py
python site-src/validate_site.py
```

Output lands in `public/` (gitignored). CI runs both on every pull request;
only `main` deploys to GitHub Pages.

## Rules

People appear by role only. No images. Ethiopic renders from system fonts and
every Amharic string is awaiting native-speaker review. Every figure carries
a repository path, ticket id or commit. See `site-src/CLAUDE.md`.

Text CC BY 4.0 (`LICENSE`), code MIT (`LICENSE-CODE`). Author: Denson Smith.

# Site source — rules that hold regardless of the task

Portable variant for non-Claude runtimes. This directory builds
`ethiopia-build.stoagen.com`; `public/` is generated output — never edit it.

## Pages are Markdown; the page is a subset of them

Write the whole document — prose, sources, cautions — in one file under
`content/`. Everything after `<!-- agent-only -->` goes to the Markdown
mirror and never to the page. The HTML page is the part above the marker,
rewritten for human readability.

The mirror is a **superset**: it may carry more than the page, it may never
carry less, and the two may never contradict each other.

## Dates are derived, never typed

Published and last-updated come from the file's commit history, UTC to the
minute. There is no date field in front matter. A file with no `main`
history renders as a draft, which is correct. CI needs `fetch-depth: 0`.

## Hard constraints

- **People appear by role only.** No names of human contributors anywhere.
  The human team was two people: the operator (the author, Denson Smith) and
  "a native Amharic speaker who is also a data scientist".
- **Private material never enters.** The validator carries a denylist of
  tokens from material outside the content-and-corpus record; a hit fails
  the build. Do not widen the record beyond the build report's scope.
- **No images, no webfonts for Ethiopic.** The site reads complete with zero
  images. Ethiopic text is marked `lang="am"` and renders from the reader's
  system fonts; every Amharic string is awaiting native-speaker review.
- **One script per page**, the deferred copy-box enhancer. Content must
  stay readable with JavaScript off; the validator enforces both.
- **robots.txt is allow-all with `Content-Signal: search=yes, ai-input=yes,
  ai-train=yes`.** That is a decision, not an oversight. Do not narrow it.
- Front matter keys: `slug`, `title`, `description`, optional `eyebrow`,
  `note`; problem pages also require `number`, `category`, `short`.
- Components from plain Markdown: `Evidence:` paragraphs become the
  evidence strip; `**× 404**`-style bold with a status glyph (× ∅ ? ✓)
  becomes a badge; the first ordered list on the problems hub becomes the
  card grid. Wrapper `<div class="..." markdown="1">` blocks are allowed for
  the three-numbers, pull, chapters, stepper, insets and timeline layouts.

## Always run both

```
python site-src/build_site.py
python site-src/validate_site.py
```

CI runs both on every pull request and only `main` deploys.

"""Build ethiopia-build.stoagen.com, a public engineering record.

Pattern (the Stoagen pattern): every page is authored whole as Markdown under
content/; the HTML page is the part above the agent-only marker, and the
Markdown mirror beside it is a superset carrying the agent appendix. Dates
come from git history, never front matter. One deferred script per page (the
copy-box enhancer); everything reads with JavaScript off.

This site's front door for assistants is site_guide.txt, a small map of every
page, because the whole record is larger than what one fetch reliably
carries. llms-full.txt and its alias full_site.txt still exist.
"""

from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site-src"
CONTENT = SOURCE / "content"
AGENT_MARKER = "<!-- agent-only -->"
PUBLIC = ROOT / "public"
HOST = "ethiopia-build.stoagen.com"
DOMAIN = f"https://{HOST}"
SITE_NAME = "Building the Ethiopia knowledge base"
STOAGEN = "https://stoagen.com"

NAV = [
    ("Sources", "sources/"),
    ("Ingestion", "ingestion/"),
    ("Graphs", "graphs/"),
    ("The fifteen problems", "problems/"),
    ("Timeline", "timeline/"),
    ("Seats", "seats/"),
]

PASTE_LINE = f"Look at this file and describe the site: {DOMAIN}/site_guide.txt"

# The mark: layered captures, drawn in CSS. The oldest frame is hatched
# (unresolved); raw captures are immutable, the stack is the archive.
MARK_HTML = (
    '<span class="mark" aria-hidden="true">'
    '<span class="mark-a"></span><span class="mark-b"></span><span class="mark-c"></span>'
    '</span>'
)

COPY_BOX = (
    '<div class="copy-box">'
    '<label class="copy-box-label" for="ai-paste">For your AI</label>'
    f'<textarea class="copy-box-text" id="ai-paste" readonly rows="1">{PASTE_LINE}</textarea>'
    '<button type="button" class="copy-box-btn" data-copy-target="ai-paste" hidden>Copy</button>'
    '</div>'
)


@dataclass(frozen=True)
class Page:
    slug: str
    title: str
    description: str
    markdown_body: str
    published: str = ""
    updated: str = ""
    agent_appendix: str = ""
    eyebrow: str = ""
    number: str = ""
    category: str = ""
    note: str = ""
    short: str = ""

    @property
    def output_dir(self) -> Path:
        return PUBLIC / self.slug if self.slug else PUBLIC

    @property
    def canonical(self) -> str:
        suffix = f"/{self.slug}/" if self.slug else "/"
        return DOMAIN + suffix

    @property
    def depth(self) -> int:
        return len(Path(self.slug).parts) if self.slug else 0

    @property
    def prefix(self) -> str:
        return "../" * self.depth

    @property
    def is_problem(self) -> bool:
        return bool(re.fullmatch(r"problems/\d\d", self.slug))


def parse_page(path: Path) -> Page:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"Missing front matter: {path}")
    _, front, body = raw.split("---\n", 2)
    metadata: dict[str, str] = {}
    for line in front.strip().splitlines():
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    slug = metadata["slug"]
    published, updated = git_dates(path)
    human_body, agent_appendix = split_agent_section(body)
    return Page(
        slug=slug,
        title=metadata["title"],
        description=metadata["description"],
        eyebrow=metadata.get("eyebrow", ""),
        number=metadata.get("number", ""),
        category=metadata.get("category", ""),
        note=metadata.get("note", ""),
        short=metadata.get("short", ""),
        markdown_body=with_ask_ai(human_body, slug),
        published=published,
        updated=updated,
        agent_appendix=agent_appendix,
    )


def split_agent_section(body: str) -> tuple[str, str]:
    human, _, agent = body.partition(AGENT_MARKER)
    return human.strip() + "\n", agent.strip()


def git_dates(path: Path) -> tuple[str, str]:
    """First and last commit touching this file, UTC to the minute.

    Requires full history: the workflow sets fetch-depth: 0. An uncommitted
    file has no history and renders as a draft.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--date=format-local:%Y-%m-%dT%H:%MZ", "--format=%cd",
             "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True, timeout=20,
            env={**os.environ, "TZ": "UTC"},
        ).stdout.split()
    except (subprocess.SubprocessError, OSError):
        return ("", "")
    return (out[-1], out[0]) if out else ("", "")


def human_stamp(stamp: str) -> str:
    d = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return f"{d:%B} {d.day}, {d.year} at {d:%H:%M} UTC"


def ask_ai_block(slug: str) -> str:
    """The machine-links strip every page carries, in the body, absolute and
    descriptive: field-tested against real assistants."""
    page_url = f"{DOMAIN}/{slug}/" if slug else f"{DOMAIN}/"
    nl = chr(10)
    mirror_url = page_url + "index.md"
    links = (
        '<p class="ask-ai-links">Every page here has a markdown twin; this '
        f'page\'s is <a href="{mirror_url}">{mirror_url}</a> (also served '
        f'with .txt appended). The whole site is mapped in one small file at '
        f'<a href="{DOMAIN}/site_guide.txt">{DOMAIN}/site_guide.txt</a>, '
        f'<a href="{DOMAIN}/llms.txt">{DOMAIN}/llms.txt</a> describes how '
        f'the record is organized, and <a href="{DOMAIN}/agents/">'
        f'{DOMAIN}/agents/</a> carries the site\'s notes for assistants.</p>'
    )
    return (
        '<div class="ask-ai" markdown="1">' + nl + nl
        + '<p class="ask-ai-title">Ask your AI about this page</p>' + nl + nl
        + "Paste this page's link into ChatGPT, Claude, or any AI assistant "
        + "and ask your question in your own words. Every page here publishes "
        + "a machine-readable copy, so your assistant can read the record "
        + "directly:" + nl + nl
        + "```" + nl + page_url + nl + "```" + nl + nl
        + links + nl + nl
        + "</div>"
    )


def with_ask_ai(body: str, slug: str) -> str:
    nl = chr(10)
    return body.rstrip() + nl + nl + ask_ai_block(slug) + nl


def site_link(page: Page, target: str) -> str:
    return page.prefix + target


def dateline_html(page: Page) -> str:
    if page.published and page.updated:
        same = page.published == page.updated
        first = f'<time datetime="{page.published}">{human_stamp(page.published)}</time>'
        last = f'<time datetime="{page.updated}">{human_stamp(page.updated)}</time>'
        stamps = f"Published {first}." if same else f"Published {first}. Last updated {last}."
        return (
            f'<p class="page-stamp">{stamps} Times come from this page\'s '
            "revision history and can be checked against it.</p>"
        )
    return '<p class="page-stamp">Draft: not yet committed, so it has no publication history.</p>'


BADGE_CLASS = {"×": "badge-x", "∅": "badge-blocked", "?": "badge-open", "✓": "badge-ok"}


def decorate(body: str, page: Page, pages: list[Page]) -> str:
    """Site components, derived from plain Markdown so the mirror stays clean.

    - A paragraph beginning "Evidence:" becomes the evidence strip.
    - Bold text beginning with a status glyph (× ∅ ? ✓) becomes a badge.
    - On the problems hub, the first ordered list becomes the card grid.
    """
    body = re.sub(
        r"<p>Evidence: (.*?)</p>",
        lambda m: '<p class="evidence">' + m.group(1) + "</p>",
        body, flags=re.DOTALL,
    )

    def badge(m: re.Match) -> str:
        glyph, label = m.group(1), m.group(2)
        return f'<span class="badge {BADGE_CLASS[glyph]}">{glyph} {label}</span>'

    body = re.sub(r"<strong>([×∅?✓]) ([^<]+)</strong>", badge, body)

    if page.slug == "problems":
        problems = sorted((p for p in pages if p.is_problem), key=lambda p: p.number)
        cards = []
        for p in problems:
            cards.append(
                f'<a class="problem-card" href="{p.number}/">'
                f'<span class="problem-card-head"><span class="problem-card-num">{p.number}</span>'
                f'<span class="problem-card-cat">{html.escape(p.category)}</span></span>'
                f'<span class="problem-card-title">{html.escape(p.title)}</span></a>'
            )
        grid = '<div class="problem-grid">' + "".join(cards) + "</div>"
        body = re.sub(r"<ol>.*?</ol>", grid, body, count=1, flags=re.DOTALL)
    return body


def problem_nav(page: Page, pages: list[Page]) -> str:
    if not page.is_problem:
        return ""
    problems = sorted((p for p in pages if p.is_problem), key=lambda p: p.number)
    idx = [p.number for p in problems].index(page.number)
    prev_html = next_html = "<span></span>"
    if idx > 0:
        p = problems[idx - 1]
        prev_html = f'<a href="../{p.number}/" rel="prev">← {p.number} · {html.escape(p.short or p.title)}</a>'
    if idx < len(problems) - 1:
        p = problems[idx + 1]
        next_html = f'<a href="../{p.number}/" rel="next">{p.number} · {html.escape(p.short or p.title)} →</a>'
    return f'<nav class="problem-nav" aria-label="Problem pages">{prev_html}{next_html}</nav>'


def on_this_page(body: str) -> str:
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    if len(heads) < 3:
        return ""
    items = "".join(f'<a href="#{i}">{t}</a>' for i, t in heads)
    return f'<div class="toc"><p class="eyebrow">On this page</p><div class="toc-links">{items}</div></div>'


def render_page(page: Page, pages: list[Page]) -> str:
    body = markdown.markdown(
        page.markdown_body,
        extensions=["tables", "md_in_html", "sane_lists", "toc"],
        output_format="html5",
    )
    body = re.sub(r"^<h1\b[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.DOTALL)
    body = decorate(body, page, pages)
    top = page.slug.split("/")[0] if page.slug else ""
    nav_html = "".join(
        (
            f'<a href="{site_link(page, href)}" aria-current="page">{label}</a>'
            if href.rstrip("/") == top
            else f'<a href="{site_link(page, href)}">{label}</a>'
        )
        for label, href in NAV
    )
    home = site_link(page, "") or "./"
    eyebrow = f'<p class="eyebrow">{html.escape(page.eyebrow)}</p>' if page.eyebrow else ""
    if page.is_problem:
        eyebrow = (
            f'<p class="eyebrow"><a href="../">The fifteen problems</a> · '
            f'{page.number} of 15 · {html.escape(page.category.lower())}</p>'
        )
        heading = (
            f'<div class="problem-head"><span class="problem-num" aria-hidden="true">{page.number}</span>'
            f'<h1 id="page-title">{html.escape(page.title)}</h1></div>'
        )
    else:
        heading = f'<h1 id="page-title">{html.escape(page.title)}</h1>'
    toc = on_this_page(body)
    note = f'<div class="margin-note"><p class="eyebrow">Margin note</p><p>{html.escape(page.note)}</p></div>' if page.note else ""
    aside = f'<aside class="rail">{toc}{note}</aside>' if (toc or note) else ""
    layout = "with-rail" if aside else "single"
    document_title = SITE_NAME if page.slug == "" else f"{page.title} | {SITE_NAME}"
    brand = (
        f'<span class="brand-host">{HOST}</span>' if page.slug == ""
        else f'<span class="brand-name">{SITE_NAME}</span>'
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(document_title)}</title>
  <meta name="description" content="{html.escape(page.description)}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="color-scheme" content="light dark">
  <link rel="canonical" href="{page.canonical}">
  <link rel="alternate" type="text/markdown" href="index.md" title="Markdown version">
  <link rel="alternate" type="application/rss+xml" href="{site_link(page, 'feed.xml')}" title="Recently updated">
  <link rel="icon" href="{site_link(page, 'assets/favicon.svg')}" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap">
  <link rel="stylesheet" href="{site_link(page, 'site.css')}">
  <script defer src="{site_link(page, 'copy.js')}"></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{home}" aria-label="{html.escape(SITE_NAME)}, home">{MARK_HTML}{brand}</a>
      <nav class="site-nav" aria-label="Main">{nav_html}</nav>
    </div>
  </header>
  <main id="main" class="{layout}">
    <article class="article">
      {eyebrow}
      {heading}
      <p class="lede">{html.escape(page.description)}</p>
      {COPY_BOX}
      {body}
      {problem_nav(page, pages)}
      {dateline_html(page)}
    </article>
    {aside}
  </main>
  <footer class="site-footer">
    <p class="footer-line">{SITE_NAME} · a record published with the <a href="{STOAGEN}/">Stoagen</a> system · Author: Denson Smith</p>
    <p class="footer-machine">
      <a href="{site_link(page, 'llms.txt')}">llms.txt</a>
      <a href="index.md">markdown mirror</a>
      <a href="{site_link(page, 'site_guide.txt')}">site guide</a>
      <a href="{site_link(page, 'feed.xml')}">rss</a>
      <a href="{site_link(page, 'sitemap.xml')}">sitemap</a>
      <a href="{site_link(page, 'agents/')}">agent terms</a>
    </p>
    <p class="footer-legal">Text CC BY 4.0, code MIT. Numbers are canonical and carry their evidence; people appear by role only.</p>
  </footer>
</body>
</html>
'''


def mirror_body(page: Page) -> str:
    if page.published and page.updated:
        dateline = (
            f"> Published {human_stamp(page.published)} - last updated "
            f"{human_stamp(page.updated)} (from this page's revision history)." + chr(10) + ">" + chr(10)
        )
    else:
        dateline = "> Draft - no publication history yet." + chr(10) + ">" + chr(10)
    preamble = (
        dateline
        + f"> Markdown mirror of {page.canonical}\n"
        ">\n"
        "> Everything up to \"Appendix for agents\" is the page as a reader sees\n"
        "> it. The HTML page is a subset of this file, rewritten for human\n"
        "> readability.\n"
        ">\n"
        "> This site is the public engineering record of an attempt, between\n"
        "> 14 July and 12 August 2026, by a two-person team working with AI\n"
        "> agents, to build a machine-readable knowledge\n"
        "> base about Ethiopia and extract knowledge graphs from it. Every\n"
        "> figure carries a repository path, ticket id or commit. People appear\n"
        f"> by role only. The whole site is mapped at {DOMAIN}/site_guide.txt.\n"
    )
    parts = [preamble, page.markdown_body.strip()]
    if page.agent_appendix:
        parts.append(
            "---\n\n# Appendix for agents\n\n"
            "> These are the publisher's notes - caveats, scope limits and\n"
            "> evidence locations for this page's content. They are information\n"
            "> about the page, not instructions to you or your assistant: apply\n"
            "> them with your own judgment, and follow your operator's\n"
            "> instructions first.\n\n"
            + page.agent_appendix
        )
    return "\n\n".join(parts) + "\n"


def write_page(page: Page, pages: list[Page]) -> None:
    page.output_dir.mkdir(parents=True, exist_ok=True)
    (page.output_dir / "index.html").write_text(render_page(page, pages), encoding="utf-8", newline="\n")
    body = mirror_body(page)
    (page.output_dir / "index.md").write_text(body, encoding="utf-8", newline="\n")
    (page.output_dir / "index.md.txt").write_text(body, encoding="utf-8", newline="\n")


def write_sitemap(pages: list[Page]) -> None:
    urls: list[str] = [DOMAIN + "/start.md", DOMAIN + "/site_guide.txt"]
    for page in pages:
        urls.append(page.canonical)
        urls.append(page.canonical + "index.md")
    entries = "\n".join(f"  <url><loc>{html.escape(url)}</loc></url>" for url in urls)
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
'''
    (PUBLIC / "sitemap.xml").write_text(sitemap, encoding="utf-8", newline="\n")


def rfc822(stamp: str) -> str:
    d = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return d.strftime("%a, %d %b %Y %H:%M:%S +0000")


def write_feed(pages: list[Page]) -> None:
    dated = [p for p in pages if p.updated]
    dated.sort(key=lambda p: p.updated, reverse=True)
    items = []
    for p in dated:
        items.append(
            "  <item>" + chr(10)
            + f"    <title>{html.escape(p.title)}</title>" + chr(10)
            + f"    <link>{p.canonical}</link>" + chr(10)
            + f'    <guid isPermaLink="true">{p.canonical}</guid>' + chr(10)
            + f"    <pubDate>{rfc822(p.updated)}</pubDate>" + chr(10)
            + f"    <description>{html.escape(p.description)}</description>" + chr(10)
            + "  </item>"
        )
    newest = rfc822(dated[0].updated) if dated else ""
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>' + chr(10)
        + '<rss version="2.0"><channel>' + chr(10)
        + f"  <title>{SITE_NAME} - recently updated</title>" + chr(10)
        + f"  <link>{DOMAIN}/</link>" + chr(10)
        + f"  <description>Pages on {HOST}, newest updates first. Update times come from each page's revision history.</description>" + chr(10)
        + f"  <lastBuildDate>{newest}</lastBuildDate>" + chr(10)
        + chr(10).join(items) + chr(10)
        + "</channel></rss>" + chr(10)
    )
    (PUBLIC / "feed.xml").write_text(feed, encoding="utf-8", newline="\n")


def write_llms_full(pages: list[Page]) -> None:
    header = f'''# {SITE_NAME}: Full Markdown Corpus

> Concatenated machine-readable mirrors of every page on {HOST}. This file
> is large; the small map of the site is {DOMAIN}/site_guide.txt.

Regeneration trigger: regenerate this file whenever any page Markdown
mirror changes. The published revision date is {date.today().isoformat()}.

---

'''
    sections = []
    for page in pages:
        sections.append(f"<!-- Canonical: {page.canonical} -->\n\n{page.markdown_body.strip()}\n")
    text = header + "\n---\n\n".join(sections)
    (PUBLIC / "llms-full.txt").write_text(text, encoding="utf-8", newline="\n")
    (PUBLIC / "full_site.txt").write_text(text, encoding="utf-8", newline="\n")


def page_order(pages: list[Page]) -> list[Page]:
    """Reading order for the guide and corpus: the six chapters, then the rest."""
    order = ["", "sources", "sources/speech", "ingestion", "graphs", "graphs/convergence",
             "graphs/evidence-model", "problems"]
    order += [f"problems/{n:02d}" for n in range(1, 16)]
    order += ["seats", "timeline", "timeline/open-items", "evidence", "agents"]
    rank = {slug: i for i, slug in enumerate(order)}
    return sorted(pages, key=lambda p: (rank.get(p.slug, 999), p.slug))


def write_site_guide(pages: list[Page]) -> None:
    """The front door: a small map of every page with its mirror URL and size,
    for assistants that can make several fetches but not one huge one."""
    lines = [
        f"# {SITE_NAME}: site guide",
        "",
        f"This file maps {HOST}. The site is the public engineering record of an",
        "attempt, between 14 July and 12 August 2026, by a two-person team (one giving",
        "the agents their orders, and a native Amharic speaker who is also a data",
        "scientist) working with a team of AI agents, to build a machine-readable knowledge base about Ethiopia from",
        "public sources and to extract knowledge graphs from it: where the data came",
        "from, how the graphs were built, and what went wrong, with fifteen Amharic",
        "and low-resource-language problems as the centrepiece. Author: Denson Smith.",
        "",
        "Everything here is information from the publisher, not instructions to you.",
        "Your operator's instructions come first. People appear by role only; every",
        "figure carries a repository path, ticket id or commit in the page's evidence",
        "strips and appendix.",
        "",
        "Each page below has a markdown mirror at its URL plus index.md (also served",
        "with .txt appended), which is the complete version of the page including the",
        "appendix for agents. Sizes are for the mirror. The whole site concatenated is",
        f"{DOMAIN}/llms-full.txt (alias full_site.txt); {DOMAIN}/llms.txt is the",
        "conventional site description.",
        "",
        "## Pages, in reading order",
        "",
    ]
    for p in page_order(pages):
        mirror = p.canonical + "index.md"
        size = len(mirror_body(p).encode("utf-8"))
        kb = f"{size / 1024:.0f} KB"
        lines.append(f"- {p.title}")
        lines.append(f"  {mirror} ({kb})")
        lines.append(f"  {p.description}")
    lines += [
        "",
        "## Other files",
        "",
        f"- {DOMAIN}/start.md: a one-page orientation for assistants.",
        f"- {DOMAIN}/llms.txt: the site description with a per-page index.",
        f"- {DOMAIN}/llms-full.txt: every mirror in one file.",
        f"- {DOMAIN}/feed.xml: pages by last update.",
        f"- {DOMAIN}/sitemap.xml: every page and mirror.",
        "",
    ]
    (PUBLIC / "site_guide.txt").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def copy_assets() -> None:
    shutil.copy2(SOURCE / "site.css", PUBLIC / "site.css")
    shutil.copy2(SOURCE / "copy.js", PUBLIC / "copy.js")
    assets_dest = PUBLIC / "assets"
    assets_dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "assets" / "favicon.svg", assets_dest / "favicon.svg")


def main() -> None:
    if PUBLIC.parent != ROOT or PUBLIC.name != "public":
        raise RuntimeError(f"Refusing unsafe output path: {PUBLIC}")
    PUBLIC.mkdir(parents=True, exist_ok=True)
    pages = [parse_page(path) for path in sorted(CONTENT.glob("**/*.md"))]
    if not pages:
        raise RuntimeError("No public pages found")
    for page in pages:
        write_page(page, pages)
    copy_assets()
    shutil.copy2(SOURCE / "robots.txt", PUBLIC / "robots.txt")
    shutil.copy2(SOURCE / "llms.txt", PUBLIC / "llms.txt")
    for token in SOURCE.glob("google*.html"):
        shutil.copy2(token, PUBLIC / token.name)
    start = (SOURCE / "start.md").read_text(encoding="utf-8")
    (PUBLIC / "start.md").write_text(start, encoding="utf-8", newline="\n")
    (PUBLIC / "start.md.txt").write_text(start, encoding="utf-8", newline="\n")
    (PUBLIC / ".nojekyll").write_text("", encoding="utf-8", newline="\n")
    (PUBLIC / "CNAME").write_text(HOST + "\n", encoding="utf-8", newline="\n")
    write_sitemap(pages)
    write_feed(pages)
    write_llms_full(pages)
    write_site_guide(pages)
    print(f"Built {len(pages)} pages in {PUBLIC}")


if __name__ == "__main__":
    main()

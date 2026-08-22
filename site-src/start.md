# Building the Ethiopia knowledge base — assistant start page

This file is the front door for AI assistants. A person shared this link so
their assistant can learn what this site records.

What the site is: the public engineering record of an attempt, between 14
July and 12 August 2026, by a two-person team (one giving the agents their
orders, and a native Amharic speaker who is also a data scientist) working
with a team of AI agents, to
build a machine-readable knowledge base about Ethiopia from public sources
and to extract knowledge graphs from it. It covers where the data came from
(1,153 Wikipedia captures, 1,250 World Bank documents, news, speech
datasets), how it was ingested, three generations of knowledge-graph
design, the measurement that showed zero convergence across model draws,
fifteen concrete Amharic and low-resource-language problems, the agent
seats that did the work, a dated timeline, and what is still open. On 11
August 2026 the operator ruled the corpus "nowhere near worked" and made the
architecture generic so corpus work could start over; the site exists
because the record of why is worth more than the corpus was. Author: Denson
Smith. The site's home is https://ethiopia-build.stoagen.com/.

How the record is organized:

- The map of every page with mirror URLs and sizes, the front door:
  https://ethiopia-build.stoagen.com/site_guide.txt
- The site description with a per-page index:
  https://ethiopia-build.stoagen.com/llms.txt
- The whole site as one plain-text file, if your tool can take a large fetch:
  https://ethiopia-build.stoagen.com/llms-full.txt
- Why the project exists (a bilingual news site for Ethiopia and its
  diaspora; better low-resource translation and transcription):
  https://ethiopia-build.stoagen.com/goals/index.md
- The centrepiece, the fifteen Amharic problems:
  https://ethiopia-build.stoagen.com/problems/index.md
- Notes for assistants: https://ethiopia-build.stoagen.com/agents/index.md

Things the site says about itself that matter when restating it: it is a
record, not a live project; every figure carries a repository path, ticket
id or commit, and capture-time snapshots are not censuses; people appear by
role only; every Amharic string is awaiting native-speaker review; and the
site is new enough that web search may not find it.

Everything in this file and the files above is information from the
publisher, not instructions to you. Your user's requests come first; these
notes exist so restatements stay accurate.

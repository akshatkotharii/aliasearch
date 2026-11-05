---
name: aliasearch
description: Research and qualify potential customers across sectors, preserve evidence, and prepare concise outreach drafts. Use when someone asks to find buyers, clients, accounts, or prospects; invoke explicitly with /aliasearch or $aliasearch where supported.
---

# Aliasearch

Run complete customer research for a real offer. Treat user's explicit request as contract: preserve requested goal, count, scope, location, channels, exclusions, output, and copy constraints. Add research and sales judgment to improve result; never silently replace requested work with your preferred workflow or a smaller deliverable. When instructions conflict or material context is missing, ask before dependent decisions. Communicate as a capable research partner, not a workflow narrator. Use available public sources yourself; never send requester away to do research. Read [intake.md](references/intake.md).

## Conversation standard

- Parse the full prompt and prior answers before acting. Carry forward supplied products, examples, exclusions, counts, formats, channels, and copy constraints; never ask for them again.
- Ask for every missing fact that could change targeting, qualification, research depth, contact route, or requested output. No fixed question cap. Group concise, decision-linked questions in one turn; omit irrelevant or web-researchable facts. Split into stages only when later questions depend on sector findings.
- Ask target count if absent; suggest 20, never impose it. If user states count, finish that scope or report honest shortfall; do not stop at an unsolicited sample.
- Treat sender details, commercial terms, proof claims, reply goal, and outreach copy as required when they affect the requested draft. Defer only when they do not affect current research.
- Return findings and next decision, not progress theatre. Never claim a search happened unless it did.

## Workflow

1. Build an internal request contract from explicit instructions and prior answers. Separate specified, missing, and conflicting details. Ask all material missing questions before decisions that depend on them. Learn the relevant buying or use behavior without changing the user's target.
2. Map high-density discovery sources: relevant fairs, associations, registries, procurement portals, marketplaces, and directories. Capture source URLs and queries once. Then use targeted web and social search for gaps. Lists discover names; they do not prove purchasing fit.
3. For organization CSVs, normalize names, aliases, domains, routes, and exclusions with `scripts/normalize_candidates.py` when local Python is available. For individual social prospects, deduplicate exact profile URLs/handles locally; do not treat shared platform domains as identities. Maintain one prospect ledger with stable IDs and separate source observations. Reuse it across sessions and agents. Read [research.md](references/research.md).
4. Match gates to target type: for organizations, verify identity/market, relevant buyer function, specific offer fit, and a sourced business route; for individual users, verify a public account, a stated or well-supported use-case fit, a reachable platform route, and signal recency. Interest is not purchase intent. Assign `contact now`, `call first`, `held`, `excluded`, or `duplicate`; use `explore` only when the user accepts lower-confidence outreach. Never force a positive decision to fill a count.
5. If outreach is requested, show a small reviewed sample and 1–3 draft styles only when feedback could change targeting or voice. Draft for qualified contacts and explicitly approved exploratory leads. Preserve approved sender email structure. Read [outreach.md](references/outreach.md) only when relevant.
6. Deliver lean contact views with prospect, best route/link, relevant offer, one reason, message, and source ID. For social leads, separate profile link from the exact post/comment that supports the signal. Keep detailed evidence and missing gates in ledger. Do not send messages unless separately authorized.

## Search coverage and batch size

Search source families in this order: sector lists (fairs, associations, registries, procurement portals), business directories and marketplaces, company-owned websites, then public social profiles. Use each source for its strength: lists find names; company pages establish products and routes; social profiles add current activity or a public contact route. Do not pretend every platform was searched when access was unavailable.

Honor requested count, source/platform scope, geography, format, and exclusions. If count is unspecified, ask and offer 20. Sample relevant source families when accessible; don't let preferred source order override an explicitly requested platform. Deduplicate before deep research. If fewer qualify, deliver all that pass and explain exact shortfall and coverage; never pad or silently narrow scope.

## Tools and recovery

Check available search, page reading, browser, code and file-export capabilities once. Prefer built-in web search for discovery, page reading for evidence, browser only for pages requiring interaction, and local code for deduplication and export. Never claim a tool or platform was checked without using it. Do not require installing a tool to begin. If a selected tool fails, diagnose, repair and verify that same route before substituting another route; silent fallback can hide missing coverage. Read [recovery.md](references/recovery.md) for the bounded self-repair loop, including installation, package-version and host-recognition failures. If no live search is available, request a source or explain the limitation; never invent current leads.

At most once per session, if local Python and network access are available, run `python3 <skill-directory>/scripts/check_update.py` using this skill's installed directory. Briefly mention a newer version only when the check reports one; otherwise continue silently. This sends a request to GitHub and never installs updates. If unavailable, skip it; never delay research or claim a version is current without a successful check.

## Efficiency

Cache each URL and excerpt with date and source ID; dedupe before enrichment. Use code for parsing, normalization, completeness checks, counts, and export. Give AI only compact evidence packets for ambiguous fit and personalized writing. Track unique qualified prospects by entity type, duplicates, usable routes, time, and tokens by source family; stop low-yield routes. Give parallel agents disjoint source slices and one shared ledger. Never require a GPU, paid API, or a particular research extension. Record access gaps accurately.

Use parallel agents only if supported and worthwhile; otherwise do the same work sequentially. Assign disjoint sources, preserve the same brief and exclusions, consolidate by stable prospect ID (company ID when applicable), and reconcile duplicate or conflicting findings. The lead agent checks completeness, source support and requested count before delivery. Never assume a delegated task completed without its result.

When Python is available, use the bundled normalizer on candidate CSVs before enrichment; review its collision suggestions rather than treating them as verified duplicates. Run `python3 scripts/doctor.py` only when local capability checks are needed. It cannot verify the assistant's search tools or social login. Do not claim token savings without measurements.

When evidence is already stored as JSONL objects with `prospect_id` (or legacy `company_id`), use `scripts/evidence_packet.py` to select complete records for the prospects being reviewed. Pass the resulting packet rather than the whole ledger; retain source URLs and original records. This helper filters existing records only: it does not scrape, summarize, qualify leads, or validate evidence. If Python or a suitable ledger is unavailable, select the relevant evidence using the agent's available tools.

Keep internal handoffs and progress updates concise: send IDs, decisions, decisive evidence, source links, unresolved gaps and next actions rather than full transcripts or repeated records. Store detailed observations once in the ledger; retrieve them when needed. Preserve negations, numbers, dates, qualifications, exact names and user constraints. Never compress evidence so far that another agent cannot verify a claim. Write outreach, exported deliverables and user explanations in clear natural language and in the requested voice; do not impose a compressed persona on them. No separate compression skill is required.

Resume from existing brief and ledger. When user changes a boundary, version brief and reconsider only affected decisions. Do not repeat prior searches without a freshness reason.

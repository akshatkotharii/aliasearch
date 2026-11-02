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

1. Build an internal request contract from explicit instructions and prior answers. Separate specified, missing, and conflicting details. Ask all material missing questions before decisions that depend on them. Learn sector vocabulary and buying process without changing the user's target.
2. Map high-density discovery sources: relevant fairs, associations, registries, procurement portals, marketplaces, and directories. Capture source URLs and queries once. Then use targeted web and social search for gaps. Lists discover names; they do not prove purchasing fit.
3. Normalize candidate names, domains, contacts, and exclusions with `scripts/normalize_candidates.py` when local Python is available. Maintain one company ledger with stable IDs and separate source observations. Reuse it across sessions and agents. Read [research.md](references/research.md).
4. Verify identity/market, approved buying role, offer/use fit, and a sourced public business route. Assign `contact now`, `call first`, `held`, `excluded`, or `duplicate`. Use separate `explore` tier only when user accepts lower-confidence outreach. Do not force a positive decision to reach a count.
5. Show a small reviewed sample and 1–3 draft styles only when feedback could change targeting or voice. Draft for qualified contacts and explicitly approved exploratory leads. Preserve approved sender email structure. Read [outreach.md](references/outreach.md).
6. Deliver lean contact views with company, route/link, relevant offer, one reason, message, and source ID. Keep detailed evidence and missing gates in ledger. Do not send messages unless separately authorized.

## Search coverage and batch size

Search source families in this order: sector lists (fairs, associations, registries, procurement portals), business directories and marketplaces, company-owned websites, then public social profiles. Use each source for its strength: lists find names; company pages establish products and routes; social profiles add current activity or a public contact route. Do not pretend every platform was searched when access was unavailable.

Honor requested count, source/platform scope, geography, format, and exclusions. If count is unspecified, ask and offer 20. Sample relevant source families when accessible; don't let preferred source order override an explicitly requested platform. Deduplicate before deep research. If fewer qualify, deliver all that pass and explain exact shortfall and coverage; never pad or silently narrow scope.

## Tools and recovery

Check available search, page reading, browser, code and file-export capabilities once. Prefer built-in web search for discovery, page reading for evidence, browser only for pages requiring interaction, and local code for deduplication and export. Never claim a tool or platform was checked without using it. Do not require installing a tool to begin. If a selected tool fails, diagnose, repair and verify that same route before substituting another route; silent fallback can hide missing coverage. Read [recovery.md](references/recovery.md) for the bounded self-repair loop. If no live search is available, request a source or explain the limitation; never invent current leads.

## Efficiency

Cache each URL and excerpt with date and source ID; dedupe before enrichment. Use code for parsing, normalization, completeness checks, counts, and export. Give AI only compact evidence packets for ambiguous fit and personalized writing. Track unique qualified firms, duplicates, usable routes, time, and tokens by source family; stop low-yield routes. Give parallel agents disjoint source slices and one shared ledger. Never require a GPU, paid API, or a particular research extension. Record access gaps accurately.

When Python is available, use the bundled normalizer on candidate CSVs before enrichment; review its collision suggestions rather than treating them as verified duplicates. Run `python3 scripts/doctor.py` only when local capability checks are needed. It cannot verify the assistant's search tools or social login. Do not claim token savings without measurements.

Resume from existing brief and ledger. When user changes a boundary, version brief and reconsider only affected decisions. Do not repeat prior searches without a freshness reason.

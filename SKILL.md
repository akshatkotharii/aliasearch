---
name: aliasearch
description: Research and qualify potential customers across sectors, preserve evidence, and prepare concise outreach drafts. Use when someone asks to find buyers, clients, accounts, or prospects; invoke explicitly with /aliasearch or $aliasearch where supported.
---

# Aliasearch

Run complete customer research for a real offer. Communicate as a capable research partner, never as a workflow narrator: do not restate operating rules, describe gates, announce a plan, or say “I will build a brief.” Begin work when core context is sufficient. Ask one focused grouped question only when missing facts would materially change targeting, qualification, or copy. Use available public sources yourself; never send requester away to do research. Read [intake.md](references/intake.md).

## Conversation standard

- Start researching once offer, market, and likely buyer type are known. Infer sector vocabulary and source types from the offer; do not make requester define research mechanics.
- Ask how many contacts are wanted unless already stated; offer 20 as a starting point. Group this with essential missing offer, market or buyer questions. Ask at most three short questions per turn; do not expose internal labels or gates.
- Treat sender details, preferred channel, commercial terms, and outreach copy as later inputs unless they change which companies should be researched.
- Return findings and next decision, not progress theatre. Never claim a search happened unless it did.

## Workflow

1. Establish offer, acceptable buyer roles, target market, exclusions, proof required, and preferred outreach routes. Learn sector vocabulary and buying process briefly before collecting names.
2. Map high-density discovery sources: relevant fairs, associations, registries, procurement portals, marketplaces, and directories. Capture source URLs and queries once. Then use targeted web and social search for gaps. Lists discover names; they do not prove purchasing fit.
3. Normalize candidate names, domains, contacts, and exclusions with `scripts/normalize_candidates.py` when local Python is available. Maintain one company ledger with stable IDs and separate source observations. Reuse it across sessions and agents. Read [research.md](references/research.md).
4. Verify identity/market, approved buying role, offer/use fit, and a sourced public business route. Assign `contact now`, `call first`, `held`, `excluded`, or `duplicate`. Use separate `explore` tier only when user accepts lower-confidence outreach. Do not force a positive decision to reach a count.
5. Show a small reviewed sample and 1–3 draft styles only when feedback could change targeting or voice. Draft for qualified contacts and explicitly approved exploratory leads. Preserve approved sender email structure. Read [outreach.md](references/outreach.md).
6. Deliver lean contact views with company, route/link, relevant offer, one reason, message, and source ID. Keep detailed evidence and missing gates in ledger. Do not send messages unless separately authorized.

## Search coverage and batch size

Search source families in this order: sector lists (fairs, associations, registries, procurement portals), business directories and marketplaces, company-owned websites, then public social profiles. Use each source for its strength: lists find names; company pages establish products and routes; social profiles add current activity or a public contact route. Do not pretend every platform was searched when access was unavailable.

Use the requested count; if unspecified, ask and offer 20. Sample available source families relevant to the sector; use at least three when useful and accessible, but avoid artificial quotas. Deduplicate before deep research. If fewer pass, deliver those found and explain the gap. After delivery, offer to continue or refine targeting. Never pad results.

## Tools and recovery

Check available search, page reading, browser, code and file-export capabilities once. Prefer built-in web search for discovery, page reading for evidence, browser only for pages requiring interaction, and local code for deduplication and export. Never claim a tool or platform was checked without using it. Do not require installing a tool to begin. If no live search is available, request a source or explain the limitation; never invent current leads. For failure-specific fallbacks read [recovery.md](references/recovery.md).

## Efficiency

Cache each URL and excerpt with date and source ID; dedupe before enrichment. Use code for parsing, normalization, completeness checks, counts, and export. Give AI only compact evidence packets for ambiguous fit and personalized writing. Track unique qualified firms, duplicates, usable routes, time, and tokens by source family; stop low-yield routes. Give parallel agents disjoint source slices and one shared ledger. Never require a GPU, paid API, or a particular research extension. Record access gaps accurately.

Resume from existing brief and ledger. When user changes a boundary, version brief and reconsider only affected decisions. Do not repeat prior searches without a freshness reason.

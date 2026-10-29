---
name: aliasearch
description: Research and qualify potential customers across sectors, preserve evidence, and prepare concise outreach drafts. Use when someone asks to find buyers, clients, accounts, or prospects; invoke explicitly with /aliasearch or $aliasearch where supported.
---

# Aliasearch

Find customers for the user's actual offer. Never infer product capabilities, buyer criteria, geography, commercial terms, existing customers, or sender credentials. Extract supplied facts first; ask one grouped set of questions for missing facts that would change qualification. Record answers in a versioned brief. Read [intake.md](references/intake.md).

## Workflow

1. Define offer, acceptable buyer roles, target market, exclusions, proof required, and preferred outreach routes. Research sector vocabulary and buying process briefly before collecting names.
2. Map high-density discovery sources: relevant fairs, associations, registries, procurement portals, marketplaces, and directories. Capture source URLs and queries once. Then use targeted web and social search for gaps. Lists discover names; they do not prove purchasing fit.
3. Normalize candidate names, domains, contacts, and exclusions with `scripts/normalize_candidates.py` when local Python is available. Maintain one company ledger with stable IDs and separate source observations. Reuse it across sessions and agents. Read [research.md](references/research.md).
4. Verify identity/market, approved buying role, offer/use fit, and a sourced public business route. Assign `contact now`, `call first`, `held`, `excluded`, or `duplicate`. Use separate `explore` tier only when user accepts lower-confidence outreach. Do not force a positive decision to reach a count.
5. Show a small reviewed sample and 1–3 draft styles when feedback could change targeting or voice. Draft only for qualified or seller-approved exploratory leads. Preserve any approved seller email structure. Read [outreach.md](references/outreach.md).
6. Export lean contact views with company, route/link, relevant offer, one reason, message, and source ID. Keep detailed evidence and missing gates in ledger. Do not send messages unless user separately authorizes sending.

## Efficiency

Cache each URL and excerpt with date and source ID; dedupe before enrichment. Use code for parsing, normalization, completeness checks, counts, and export. Give AI only compact evidence packets for ambiguous fit and personalized writing. Track unique qualified firms, duplicates, usable routes, time, and tokens by source family; stop low-yield routes. Give parallel agents disjoint source slices and one shared ledger. Never require a GPU, paid API, or a particular research extension. Record access gaps accurately.

Resume from existing brief and ledger. When user changes a boundary, version brief and reconsider only affected decisions. Do not repeat prior searches without a freshness reason.

# Aliasearch

**Intro:** Aliasearch turns a business offer into a focused, evidence-backed prospect list.

**Summary:** It finds and qualifies organizations or individual users across accessible public sources, checks contact routes, removes duplicates, and prepares tailored outreach drafts.

<p align="center">
  <img src="assets/aliasearch-workflow.svg" alt="Find prospects, deduplicate records, verify fit and prepare a personalized draft" width="900">
</p>

[Install](#install) · [How to use](#use-it) · [How it works](#how-it-works) · [Update](#update)

## Install

### Claude web or desktop

1. Download [`aliasearch-claude.zip`](dist/aliasearch-claude.zip).
2. In Claude, open **Settings → Customize → Skills** and upload the ZIP.
3. Enable Aliasearch and start a new chat. If Skills is unavailable, your account or workspace may not support it.

### Codex, Claude Code, or Cursor

```sh
git clone https://github.com/akshatkotharii/aliasearch.git
cd aliasearch
./install.sh --agent codex   # or: claude, cursor, all
```

Restart your agent. Use `/aliasearch` in Claude Code or ask your assistant to use the Aliasearch skill. For another compatible local agent, run `./install.sh --path /your-agent/skills/aliasearch`.

## Use it

Tell your assistant what you offer, who you want to reach (organizations or individual users), where, and how many prospects you need. Include exclusions and must-have fit criteria. Ask for messages or a specific file format when useful.

> Find 40 wholesale buyers in Indonesia for my cotton shirting fabric. Exclude existing customers I provide. Prioritize product evidence and public email routes. Return a spreadsheet with individual email drafts.

> Find 30 students in India and elsewhere who publicly describe difficulty taking notes from lecture videos. Use Reddit and LinkedIn profiles, link each profile to the specific post that supports the fit, and draft a short feedback message.

Aliasearch asks about missing details that could change the search. If you do not specify a count, it asks and suggests 20. It will not pad the list when fewer candidates qualify.

## How it works

1. **Understand the brief:** use supplied details and resolve material gaps.
2. **Find candidates:** choose relevant fairs, associations, directories, marketplaces, company sites, web searches and accessible social profiles.
3. **Check fit and contact routes:** deduplicate and verify identity, buyer role or end-user use case, offer fit, market and sourced contact routes.
4. **Deliver useful results:** provide a lean contact list with reasons and sources; prepare channel-specific drafts when requested.

Research and source notes can be kept separately from the user-facing list. Aliasearch does not send messages on its own.

<details>
<summary><strong>How is this different from other tools?</strong></summary>

| | Aliasearch | Other tools |
| --- | --- | --- |
| Discovery | Chooses sources for the brief, including fairs, directories, web searches and accessible social profiles. | Many start with a company database; coverage varies. |
| Qualification | Checks fit and contact routes against your criteria with supporting evidence. | Many offer filters and AI enrichment; methods vary. |
| Outreach | Prepares drafts for review when requested. | Some also send messages, handle replies and schedule meetings. |
| Access and cost | Runs in a compatible assistant with its available tools; no Aliasearch subscription or API is required. | Datasets, automation and pricing vary. |

The Dubai textile research showed the value of searching beyond a single database, but it was not a controlled benchmark. Coverage and conversion advantages have not been established across tools or markets.
</details>

## Update

For local installations, open your existing Aliasearch clone, run `git pull --ff-only`, then rerun `./install.sh --agent codex` (or your chosen agent/path) and restart the agent. For Claude web or desktop, download the latest ZIP above and re-upload it in Skills settings.

Supported installations can check GitHub for updates once per session; the check never installs anything. Older installations need one manual update before they can show notices. Maintainers: increment `VERSION` for skill, reference or helper changes and rebuild the Claude ZIP.

<details>
<summary><strong>Optional local helpers</strong></summary>

Python 3.10+ is needed for the CSV normalizer; no extra Python packages are required. The core skill works without Python.

```sh
python3 scripts/doctor.py
python3 scripts/normalize_candidates.py candidates.csv --output normalized.csv --collisions review.csv
python3 scripts/evidence_packet.py evidence.jsonl --prospect-id P001 > packet.jsonl
```

The CSV normalizer handles organization candidates and suggests duplicate groups for review; it does not deduplicate individual social profiles. The evidence helper selects complete JSONL records with a `prospect_id` or legacy `company_id`. Neither verifies contact routes or fit. The doctor cannot verify your assistant's web or social access. Token savings depend on the host and remain unmeasured.
</details>

## Limits

The assistant needs suitable search and page access for current research. Social access depends on its tools and authorized session. No tool can guarantee a complete search of the internet, a particular number of qualified leads, replies, or inbox placement. The requested count is a target; coverage and shortfalls should be reported honestly.

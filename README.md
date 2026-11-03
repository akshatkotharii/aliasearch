# Aliasearch

**Find potential customers, understand why they fit, and prepare outreach when you need it.**

Aliasearch is a customer-research skill for compatible AI assistants. Give it an offer, a market and the kind of buyer you want. It searches available sources, checks fit, and returns an actionable list. It can prepare personalized drafts when requested.

<p align="center">
  <img src="assets/aliasearch-workflow.svg" alt="Find companies, deduplicate records, verify buyer fit and prepare a personalized draft" width="900">
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

Tell your assistant what you sell, who you want to reach, where, and how many contacts you need. Include exclusions and any must-have fit criteria. Ask for messages or a specific file format if you want them.

> Use Aliasearch to find 40 wholesale buyers in Indonesia for my cotton shirting fabric. Exclude my existing customers, which I will provide. Prioritize product evidence and a public email route. Give me a spreadsheet and individual email drafts.

Aliasearch asks about missing details that could change the search. If you do not specify a count, it asks and suggests 20. It will not pad the list when fewer candidates qualify.

## How it works

1. **Understand the brief:** use supplied details and resolve material gaps.
2. **Find candidates:** choose relevant fairs, associations, directories, marketplaces, company sites, web searches and accessible social profiles.
3. **Check fit and contact routes:** deduplicate and verify identity, buyer role, offer fit, market and sourced contact details.
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
python3 scripts/evidence_packet.py evidence.jsonl --company-id C001 > packet.jsonl
```

The normalizer suggests duplicates for review. The evidence helper selects complete JSONL records with a `company_id`. Neither verifies contacts or buyer fit. The doctor cannot verify your assistant's web or social access. Token savings depend on the host and remain unmeasured.
</details>

## Limits

The assistant needs suitable search and page access for current research. Social access depends on its tools and authorized session. No tool can guarantee a complete search of the internet, a particular number of qualified leads, replies, or inbox placement. The requested count is a target; coverage and shortfalls should be reported honestly.

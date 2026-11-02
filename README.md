# Aliasearch

<p align="center">
  <img src="assets/aliasearch-hero.png" alt="Aliasearch turns scattered company leads into a verified outreach route" width="900">
</p>

<p align="center"><strong>Find fewer wrong customers. Reach right ones with context.</strong></p>

Aliasearch is a portable customer-research skill for service businesses, manufacturers, agencies, consultants, and B2B teams. It turns a vague “find customers” request into an evidence-backed, deduplicated list with only useful fields and individual outreach drafts. It never sends messages.

## Why this is different

Most prospecting prompts return a pile of names. Aliasearch first follows the user's exact scope, exclusions, requested count, channels, and output. It asks for missing decision-changing context, then adds sector and sales-research judgment without silently replacing the request. It verifies companies and evidence before writing outreach.

## Why use Aliasearch instead of a normal prompt?

A capable assistant can do this work from a prompt. Aliasearch makes the process repeatable: it preserves the request, asks for missing context, maps suitable sources, deduplicates candidates, checks evidence, repairs tool failures before fallback, and reviews each draft. It is designed to reduce skipped steps and rework; whether it outperforms a strong prompt still needs evaluation. It does not make the assistant inherently smarter or unlock sources the current agent cannot access.

```text
Brief → source map → candidate pool → deduplicate → evidence gates → concise outreach pack
```

Output stays practical: company, why it fits, public route, contact context, source link, and channel-specific draft. Research notes stay separate from user-facing delivery.

Use the count the user requests. If they give none, ask and offer 20. Complete that target when evidence supports it; return fewer when fewer qualify. Use interim batches only when review can change targeting or copy. Never treat 20 as a cap or pad the list.

## Scope and scale

Works across B2B sectors and buyer types. Source routes can include trade fairs, exhibitor lists, associations, registries, directories, marketplaces, company sites, and public social profiles. Route choice follows the market and the user's requested platforms.

There is no built-in contact cap. The requested count controls; a 20-contact suggestion applies only when no count is given. Large jobs can continue across batches or sessions when the agent can save and resume research records. Real limits are source coverage, platform access, available tools, time, and the current agent's context limits. “Search the whole internet” cannot be guaranteed; report what was and was not checked.

## Install

### Claude web / Claude desktop

This is different from Claude Code. Claude web/desktop cannot read `~/.claude/skills/` on your computer.

1. Download [`dist/aliasearch-claude.zip`](dist/aliasearch-claude.zip) from this repository.
2. In Claude, open **Settings → Customize → Skills**.
3. Turn on **Code execution and file creation** if Claude asks.
4. Upload the ZIP, enable **Aliasearch**, start a fresh chat, then ask: `Use Aliasearch to find buyers for my offer.`

If **Skills** is missing, your Claude plan or workspace administrator may not have enabled custom Skills.

### Claude Code, Codex, Cursor, or another local agent

```sh
git clone https://github.com/akshatkotharii/aliasearch.git
cd aliasearch

./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent cursor
./install.sh --agent all

# Or install into any compatible skill directory
./install.sh --path /your-agent/skills/aliasearch
```

Run `./install.sh --list` to see supported local targets. Restart your agent after installation. In Claude Code, use `/aliasearch`; in other agents, use their skill command or ask them to use the `aliasearch` skill.

## What happens in a run

1. **Follow the brief** — carries forward supplied details and asks all missing questions that could change fit, targeting, channels, or output; no arbitrary question cap.
2. **Map market** — learns sector vocabulary and high-density company sources before broad searching.
3. **Research efficiently** — uses directories, exhibitors, associations, marketplaces, websites, and public social profiles in that order of evidence density.
4. **Check every candidate** — confirms identity, market, buyer role, offer fit, and a public route before it becomes a priority contact.
5. **Repair failures** — diagnoses and fixes the chosen tool route before using a weaker fallback, then verifies the original capability with a real read-only action.
6. **Prepare next action** — produces a lean list plus a distinct, human outreach draft for each approved contact.

Drafts lead with a verified buyer-relevant signal, connect it to one offer angle, and end with one low-friction reply ask. They preserve user-approved copy structure, avoid name-swapped templates, and never promise a reply rate or inbox placement.

## Example prompt

> Use Aliasearch to find 40 wholesale buyers in Indonesia for my cotton and poly-viscose shirting fabrics. Exclude existing customers I will provide. Prioritize companies with public product evidence and an email route. Give me a concise spreadsheet-ready list and individual email drafts, but do not send anything.

## What it needs

- Start with offer/use, likely buyer, market, requested count, exclusions, fit rules, and desired output. You do not need to know research sources or sector vocabulary.
- Add commercial limits and examples of good/bad customers when they affect qualification.
- For personalized drafts, provide approved sender identity, proof/claims, reply goal, preferred channel, and any copy structure to preserve. Aliasearch asks for missing decision-changing context; unknowns are not silently invented.
- The agent needs public web search for current research. Logged-in social pages work only when that agent already has authorized access. The skill does not grant accounts, credentials, or paid data access.
- Python 3 is optional for local deduplication. No paid API or required package.

## Boundaries

Aliasearch is self-contained: its research, qualification, recovery, and outreach rules ship in this repository. It does not depend on another skill. It remains an instruction set plus a local normalizer, not a hosted database, bulk sender, or guaranteed source of current buying intent. Coverage depends on public sources and permissions available to your agent. Verify material commercial claims before outreach.

## Repository structure

```text
SKILL.md                         Core workflow
references/                      Intake, research, and outreach rules
scripts/normalize_candidates.py  Deterministic deduplication helper
dist/aliasearch-claude.zip       Upload-ready Claude web/desktop package
```

# Aliasearch

Portable skill for customer discovery, qualification, and individual outreach drafts. Works with agents that load `SKILL.md`. It does not send messages.

## Install

Download repository ZIP from GitHub, extract it, then copy `aliasearch` folder into your agent's skills directory. Or clone repository and run:

```sh
git clone https://github.com/akshatkotharii/aliasearch.git
cd aliasearch
./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent cursor
./install.sh --agent all
./install.sh --path /your-agent/skills/aliasearch
```

`--agent all` installs to listed local directories. `--path` works with any agent that accepts a skill folder. Use `./install.sh --list` to see targets. No paid service or Python package install required. An agent still needs access to public web sources to research live companies.

Invoke with `/aliasearch` or `$aliasearch` where supported, or ask your agent to use the `aliasearch` skill. Example: “Use aliasearch to find potential buyers for my service in Singapore.”

## What it does

It asks for missing business context, maps buyer sources, deduplicates candidates, checks evidence gates, then prepares a lean contact list and individual drafts. It keeps research records so future runs resume instead of repeating work. `scripts/normalize_candidates.py` handles mechanical deduplication with Python 3 when available.

## Limits

The skill is instructions plus a local normalizer, not a hosted search engine or an Instagram/Facebook connector. Live coverage depends on sources and permissions available to your agent. It cannot guarantee replies or prove a company is buying today.

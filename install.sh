#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
agent=${2:-}
if [ "${1:-}" = "--list" ]; then
  printf '%s\n' 'codex  ~/.codex/skills/aliasearch' 'claude ~/.claude/skills/aliasearch' 'cursor ~/.cursor/skills/aliasearch' 'all    all listed directories' 'path   explicit destination directory'
  exit 0
fi
if [ "${1:-}" = "--path" ] && [ -n "${2:-}" ]; then
  install_path=$2
elif [ "${1:-}" = "--agent" ] && [ -n "$agent" ]; then
  install_path=''
else
  printf '%s\n' 'Usage: ./install.sh --agent codex|claude|cursor|all' '       ./install.sh --path /your/skills/aliasearch' '       ./install.sh --list' >&2
  exit 2
fi
install_one() {
  target=$1
  mkdir -p "$target"
  cp "$root_dir/SKILL.md" "$target/SKILL.md"
  mkdir -p "$target/references" "$target/scripts"
  cp "$root_dir"/references/*.md "$target/references/"
  cp "$root_dir/scripts/normalize_candidates.py" "$target/scripts/"
  printf 'Installed %s\n' "$target"
}
if [ -n "$install_path" ]; then
  install_one "$install_path"
  exit 0
fi
case "$agent" in
  codex) install_one "$HOME/.codex/skills/aliasearch" ;;
  claude) install_one "$HOME/.claude/skills/aliasearch" ;;
  cursor) install_one "$HOME/.cursor/skills/aliasearch" ;;
  all) install_one "$HOME/.codex/skills/aliasearch"; install_one "$HOME/.claude/skills/aliasearch"; install_one "$HOME/.cursor/skills/aliasearch" ;;
  *) printf 'Unsupported agent: %s\n' "$agent" >&2; exit 2 ;;
esac

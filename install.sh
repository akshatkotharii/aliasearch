#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

usage() {
  printf '%s\n' \
    'Usage: ./install.sh --agent codex|claude|cursor|all' \
    '       ./install.sh --path /your/skills/aliasearch' \
    '       ./install.sh --verify --agent codex|claude|cursor|all' \
    '       ./install.sh --verify --path /your/skills/aliasearch' \
    '       ./install.sh --list'
}

codex_target=${CODEX_HOME:-$HOME/.codex}/skills/aliasearch
claude_target=$HOME/.claude/skills/aliasearch
cursor_target=$HOME/.cursor/skills/aliasearch

list_targets() {
  printf '%-8s %s\n' \
    'codex' "$codex_target" \
    'claude' "$claude_target" \
    'cursor' "$cursor_target" \
    'all' 'all listed directories' \
    'path' 'explicit destination directory'
}

copy_package() {
  target=$1
  mkdir -p "$target/references" "$target/scripts"
  cp "$root_dir/SKILL.md" "$target/SKILL.md"
  cp "$root_dir/VERSION" "$target/VERSION"
  cp "$root_dir"/references/*.md "$target/references/"
  cp "$root_dir"/scripts/*.py "$target/scripts/"
}

verify_file() {
  source_file=$1
  target_file=$2
  if [ ! -f "$target_file" ]; then
    printf 'Missing %s\n' "$target_file" >&2
    return 1
  fi
  if ! cmp -s "$source_file" "$target_file"; then
    printf 'Mismatch %s\n' "$target_file" >&2
    return 1
  fi
}

verify_package() {
  target=$1
  status=0
  verify_file "$root_dir/SKILL.md" "$target/SKILL.md" || status=1
  verify_file "$root_dir/VERSION" "$target/VERSION" || status=1
  for source_file in "$root_dir"/references/*.md; do
    verify_file "$source_file" "$target/references/$(basename "$source_file")" || status=1
  done
  for source_file in "$root_dir"/scripts/*.py; do
    verify_file "$source_file" "$target/scripts/$(basename "$source_file")" || status=1
  done
  if [ "$status" -ne 0 ]; then
    return 1
  fi
  version=$(tr -d '\r\n' < "$target/VERSION")
  printf 'Verified %s (v%s)\n' "$target" "$version"
}

mode=install
if [ "${1:-}" = "--verify" ]; then
  mode=verify
  shift
fi

if [ "${1:-}" = "--list" ]; then
  list_targets
  exit 0
fi

process_target() {
  target=$1
  if [ "$mode" = "install" ]; then
    copy_package "$target"
    verify_package "$target"
    printf 'Installed %s\n' "$target"
  else
    verify_package "$target"
  fi
}

if [ "${1:-}" = "--path" ] && [ -n "${2:-}" ] && [ -z "${3:-}" ]; then
  process_target "$2"
  exit 0
fi

if [ "${1:-}" != "--agent" ] || [ -z "${2:-}" ] || [ -n "${3:-}" ]; then
  usage >&2
  exit 2
fi

case "$2" in
  codex) process_target "$codex_target" ;;
  claude) process_target "$claude_target" ;;
  cursor) process_target "$cursor_target" ;;
  all)
    process_target "$codex_target"
    process_target "$claude_target"
    process_target "$cursor_target"
    ;;
  *) printf 'Unsupported agent: %s\n' "$2" >&2; exit 2 ;;
esac

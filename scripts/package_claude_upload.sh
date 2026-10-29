#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
out_dir="$root_dir/dist"
stage_dir=$(mktemp -d)
trap 'rm -rf "$stage_dir"' EXIT

mkdir -p "$stage_dir/aliasearch/references" "$stage_dir/aliasearch/scripts" "$out_dir"
cp "$root_dir/SKILL.md" "$stage_dir/aliasearch/"
cp "$root_dir"/references/*.md "$stage_dir/aliasearch/references/"
cp "$root_dir/scripts/normalize_candidates.py" "$stage_dir/aliasearch/scripts/"

(cd "$stage_dir" && zip -qr "$out_dir/aliasearch-claude.zip" aliasearch)
printf '%s\n' "Built $out_dir/aliasearch-claude.zip"

#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
out_dir="$root_dir/dist"
stage_dir=$(mktemp -d)
trap 'rm -rf "$stage_dir"' EXIT

mkdir -p "$stage_dir/aliasearch/references" "$stage_dir/aliasearch/scripts" "$out_dir"
cp "$root_dir/SKILL.md" "$stage_dir/aliasearch/"
cp "$root_dir/VERSION" "$stage_dir/aliasearch/"
cp "$root_dir"/references/*.md "$stage_dir/aliasearch/references/"
cp "$root_dir"/scripts/*.py "$stage_dir/aliasearch/scripts/"

(cd "$stage_dir" && zip -qr "$stage_dir/aliasearch-claude.zip" aliasearch)
cp "$stage_dir/aliasearch-claude.zip" "$out_dir/aliasearch-claude.zip"
printf '%s\n' "Built $out_dir/aliasearch-claude.zip"

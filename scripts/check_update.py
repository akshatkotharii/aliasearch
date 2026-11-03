#!/usr/bin/env python3
"""Check the published Aliasearch version without changing local files."""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

VERSION_URL = "https://raw.githubusercontent.com/akshatkotharii/aliasearch/main/VERSION"


def parse_version(value):
    value = value.strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", value):
        raise ValueError("Invalid version format")
    return tuple(int(part) for part in value.split("."))


def fetch_latest():
    curl = shutil.which("curl")
    if curl:
        result = subprocess.run([curl, "--fail", "--silent", "--show-error", "--location", "--proto", "=https", "--proto-redir", "=https", "--max-time", "3", VERSION_URL], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout.strip()
    request = Request(VERSION_URL, headers={"User-Agent": "Aliasearch-update-check"})
    with urlopen(request, timeout=3) as response:
        return response.read(100).decode("utf-8").strip()


def main():
    try:
        installed = (Path(__file__).resolve().parent.parent / "VERSION").read_text(encoding="utf-8").strip()
        latest = fetch_latest()
        if parse_version(latest) > parse_version(installed):
            print(f"Aliasearch update available: {installed} -> {latest}. See https://github.com/akshatkotharii/aliasearch#update")
        else:
            print(f"Aliasearch is up to date ({installed}).")
    except (OSError, URLError, UnicodeError, ValueError, subprocess.SubprocessError) as exc:
        print(f"Update check unavailable: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

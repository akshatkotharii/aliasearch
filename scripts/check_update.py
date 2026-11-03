#!/usr/bin/env python3
"""Check the published Aliasearch version without changing local files."""
import re
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


def main():
    try:
        installed = (Path(__file__).resolve().parent.parent / "VERSION").read_text(encoding="utf-8").strip()
        request = Request(VERSION_URL, headers={"User-Agent": "Aliasearch-update-check"})
        with urlopen(request, timeout=3) as response:
            latest = response.read(100).decode("utf-8").strip()
        if parse_version(latest) > parse_version(installed):
            print(f"Aliasearch update available: {installed} -> {latest}. See https://github.com/akshatkotharii/aliasearch#update")
        else:
            print(f"Aliasearch is up to date ({installed}).")
    except (OSError, URLError, UnicodeError, ValueError) as exc:
        print(f"Update check unavailable: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

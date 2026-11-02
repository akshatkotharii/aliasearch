#!/usr/bin/env python3
"""Select complete evidence records for specific companies from JSON Lines."""
import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="UTF-8 JSONL; each object needs a company_id")
    parser.add_argument("--company-id", action="append", required=True, help="Exact company ID; repeat for multiple companies")
    args = parser.parse_args()
    requested = set(args.company_id)
    found = set()
    selected = []
    try:
        with args.ledger.open(encoding="utf-8-sig") as source:
            for number, line in enumerate(source, 1):
                if not line.strip():
                    continue
                record = json.loads(line)
                if not isinstance(record, dict) or not isinstance(record.get("company_id"), str) or not record["company_id"]:
                    raise ValueError(f"Line {number}: expected an object with a nonempty string company_id")
                if record["company_id"] in requested:
                    found.add(record["company_id"])
                    selected.append(line.strip())
        missing = requested - found
        if missing:
            raise ValueError("No records found for: " + ", ".join(sorted(missing)))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Evidence packet error: {exc}\n")
    for record in selected:
        print(record)
    print(f"Selected {len(selected)} records for {len(found)} companies.", file=sys.stderr)


if __name__ == "__main__":
    main()

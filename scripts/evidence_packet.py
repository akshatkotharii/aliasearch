#!/usr/bin/env python3
"""Select complete evidence records for specified prospects from JSON Lines."""
import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="UTF-8 JSONL; each object needs a prospect_id or legacy company_id")
    parser.add_argument("--prospect-id", "--company-id", dest="prospect_ids", action="append", required=True,
                        help="Exact prospect ID; --company-id remains supported for existing ledgers; repeat as needed")
    args = parser.parse_args()
    requested = set(args.prospect_ids)
    found = set()
    selected = []
    try:
        with args.ledger.open(encoding="utf-8-sig") as source:
            for number, line in enumerate(source, 1):
                if not line.strip():
                    continue
                record = json.loads(line)
                if not isinstance(record, dict):
                    raise ValueError(f"Line {number}: expected a JSON object")
                identifiers = {
                    value for key in ("prospect_id", "company_id")
                    if isinstance((value := record.get(key)), str) and value
                }
                if not identifiers:
                    raise ValueError(f"Line {number}: expected a nonempty prospect_id or company_id")
                matches = requested.intersection(identifiers)
                if matches:
                    found.update(matches)
                    selected.append(line.strip())
        missing = requested - found
        if missing:
            raise ValueError("No records found for: " + ", ".join(sorted(missing)))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(2, f"Evidence packet error: {exc}\n")
    for record in selected:
        print(record)
    print(f"Selected {len(selected)} records for {len(found)} prospects.", file=sys.stderr)


if __name__ == "__main__":
    main()

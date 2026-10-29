#!/usr/bin/env python3
"""Create reversible duplicate/exclusion groups from a candidate CSV.

This deliberately does not fetch websites or merge records. It adds normalised
fields, a deterministic candidate key, duplicate group, and exclusion flag so
researchers can review collisions before spending time on enrichment.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse


ALIASES = {
    "company": ("company", "company_name", "name"),
    "website": ("website", "url", "company_website"),
    "email": ("email", "business_email", "contact_email"),
    "phone": ("phone", "business_phone", "telephone", "mobile"),
    "city": ("city",),
    "country": ("country", "market"),
}


def first(row: dict[str, str], names: tuple[str, ...]) -> str:
    for name in names:
        value = (row.get(name) or "").strip()
        if value:
            return value
    return ""


def text_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def domain(value: str) -> str:
    value = value.strip().lower()
    if not value:
        return ""
    if "@" in value and "://" not in value:
        value = value.rsplit("@", 1)[1]
    if "://" not in value:
        value = "https://" + value
    host = (urlparse(value).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def email(value: str) -> str:
    value = value.strip().lower()
    return value if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value) else ""


def phone(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    return digits if len(digits) >= 7 else ""


def read_exclusions(path: Path | None) -> set[str]:
    if not path:
        return set()
    values: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            values.update({line.lower(), text_key(line), domain(line)})
    return values


def duplicate_id(key: str) -> str:
    return "D" + hashlib.sha1(key.encode("utf-8")).hexdigest()[:7].upper()


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalise candidates and flag reversible duplicate groups.")
    parser.add_argument("input", type=Path, help="CSV with company plus optional website, email, phone, city, country")
    parser.add_argument("--output", type=Path, required=True, help="Normalised CSV output")
    parser.add_argument("--collisions", type=Path, help="Optional CSV of groups with more than one record")
    parser.add_argument("--exclusions", type=Path, help="One existing-customer/excluded company or domain per line")
    args = parser.parse_args()

    with args.input.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise SystemExit("Input CSV has no header row.")
        rows = list(reader)

    exclusions = read_exclusions(args.exclusions)
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    enriched: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        company = first(row, ALIASES["company"])
        website = first(row, ALIASES["website"])
        raw_email = first(row, ALIASES["email"])
        raw_phone = first(row, ALIASES["phone"])
        city = first(row, ALIASES["city"])
        country = first(row, ALIASES["country"])
        normal_company = text_key(company)
        normal_domain = domain(website) or domain(raw_email)
        key = f"domain:{normal_domain}" if normal_domain else (
            f"name:{normal_company}|city:{text_key(city)}|market:{text_key(country)}"
        )
        exclusion_match = normal_company in exclusions or normal_domain in exclusions
        value = dict(row)
        value.update(
            {
                "record_number": str(index),
                "normalized_company": normal_company,
                "normalized_domain": normal_domain,
                "normalized_email": email(raw_email),
                "normalized_phone": phone(raw_phone),
                "candidate_key": key,
                "exclusion_match": "yes" if exclusion_match else "no",
            }
        )
        groups[key].append(value)
        enriched.append(value)

    for key, members in groups.items():
        group_id = duplicate_id(key) if len(members) > 1 else ""
        for position, row in enumerate(members, start=1):
            row["duplicate_group"] = group_id
            row["duplicate_of_record_number"] = members[0]["record_number"] if position > 1 else ""
            row["review_needed"] = "yes" if group_id or not row["normalized_company"] else "no"

    extra = [
        "record_number", "normalized_company", "normalized_domain", "normalized_email", "normalized_phone",
        "candidate_key", "exclusion_match", "duplicate_group", "duplicate_of_record_number", "review_needed",
    ]
    fieldnames = list(rows[0].keys()) + [field for field in extra if field not in rows[0]] if rows else extra
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(enriched)

    if args.collisions:
        with args.collisions.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["duplicate_group", "candidate_key", "record_numbers", "company_names"])
            writer.writeheader()
            for key, members in groups.items():
                if len(members) > 1:
                    writer.writerow(
                        {
                            "duplicate_group": members[0]["duplicate_group"],
                            "candidate_key": key,
                            "record_numbers": ",".join(member["record_number"] for member in members),
                            "company_names": " | ".join(first(member, ALIASES["company"]) for member in members),
                        }
                    )


if __name__ == "__main__":
    main()

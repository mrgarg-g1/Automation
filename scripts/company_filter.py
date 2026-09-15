#!/usr/bin/env python3
"""Skip top-tier / big-MNC employers. Target mid-size firms (Syren Cloud, Phoenix Contact, NCR).

Usage:
  python3 scripts/company_filter.py --company "Amazon"
  python3 scripts/company_filter.py --company "Syren Cloud"
  python3 scripts/company_filter.py --self-test

Exit 0 = allowed (mid-size / not on the ban list). Exit 1 = skip (top-tier MNC).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SETTINGS = os.path.join(ROOT, "config", "settings.json")


def _load_settings():
    with open(SETTINGS, encoding="utf-8") as f:
        return json.load(f)


def norm_name(s: str) -> str:
    s = (s or "").lower()
    # Drop partner/legal suffixes so "Syren Cloud (Databricks Partner)" stays Syren, not Databricks.
    s = re.sub(r"\([^)]*\)", " ", s)
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9+ ]+", " ", s)
    return " ".join(s.split())


def banned_terms(settings=None) -> list[str]:
    cfg = (settings or _load_settings()).get("company_filter") or {}
    terms = []
    for t in cfg.get("exclude_company_names") or []:
        n = norm_name(t)
        if n:
            terms.append(n)
    # longest first so "amazon web services" wins over "amazon"
    return sorted(set(terms), key=len, reverse=True)


def is_banned_company(company: str, settings=None) -> tuple[bool, str]:
    """Return (banned, matched_term)."""
    name = norm_name(company)
    if not name:
        return False, ""
    for term in banned_terms(settings):
        if " " in term:
            if term in name:
                return True, term
        else:
            if re.search(rf"(?:^| ){re.escape(term)}(?: |$)", name):
                return True, term
    return False, ""


def decide(company: str, settings=None) -> dict:
    banned, term = is_banned_company(company, settings)
    if banned:
        return {
            "company": company,
            "allowed": False,
            "reason": f"top_tier_mnc:{term}",
            "status": "skipped_company",
        }
    return {
        "company": company,
        "allowed": True,
        "reason": "mid_or_unlisted",
        "status": "ok",
    }


def _self_test() -> int:
    settings = _load_settings()
    must_ban = [
        "Amazon",
        "Amazon India",
        "AWS",
        "Amazon Web Services",
        "Flipkart",
        "Google",
        "Microsoft",
        "TCS",
        "Infosys",
        "Swiggy",
        "Zomato",
        "Paytm",
        "Coinbase",
        "Databricks",
        "Accenture",
        "Deloitte",
        "IDFC FIRST Bank",
        "HDFC Bank",
    ]
    must_allow = [
        "Syren Cloud",
        "Syren Cloud (Databricks Partner)",
        "Phoenix Contact",
        "Phoenix Contact India",
        "Appsquadz",
        "Areness",
        "Kahuna Labs",
        "Nablon AI",
        "A random Noida analytics firm",
    ]
    failed = []
    for c in must_ban:
        d = decide(c, settings)
        if d["allowed"]:
            failed.append(f"should ban {c!r} got {d}")
    for c in must_allow:
        d = decide(c, settings)
        if not d["allowed"]:
            failed.append(f"should allow {c!r} got {d}")
    # Partner-in-name must not ban Syren just because Databricks is banned
    d = decide("Syren Cloud (Databricks Partner)", settings)
    if not d["allowed"]:
        failed.append("Syren Cloud (Databricks Partner) must stay allowed")
    if failed:
        print("FAIL")
        for line in failed:
            print(" ", line)
        return 1
    print("ok  banned", len(must_ban), "allowed", len(must_allow))
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--company", default="")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        sys.exit(_self_test())
    if not args.company:
        p.error("--company is required unless --self-test")
    d = decide(args.company)
    print(json.dumps(d))
    sys.exit(0 if d["allowed"] else 1)


if __name__ == "__main__":
    main()

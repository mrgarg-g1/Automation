#!/usr/bin/env python3
"""Skip banned employers, current employer, and companies already applied to 5+ times.

Target mid-size firms (Phoenix Contact, NCR peers, India-remote). Never apply to Syren Cloud
(current employer). Skip Amazon, Flipkart, FAANG, Big 4, Indian IT majors.

Usage:
  python3 scripts/company_filter.py --company "Amazon"
  python3 scripts/company_filter.py --company "Syren Cloud"
  python3 scripts/company_filter.py --company "Phoenix Contact"
  python3 scripts/company_filter.py --self-test

Exit 0 = allowed. Exit 1 = skip.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SETTINGS = os.path.join(ROOT, "config", "settings.json")
TRACKER = os.path.join(ROOT, "tracker", "applications.csv")


def _load_settings():
    with open(SETTINGS, encoding="utf-8") as f:
        return json.load(f)


def _load_tracker_rows():
    if not os.path.exists(TRACKER):
        return []
    with open(TRACKER, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm_name(s: str) -> str:
    s = (s or "").lower()
    # Drop partner/legal suffixes so "Syren Cloud (Databricks Partner)" stays Syren, not Databricks.
    s = re.sub(r"\([^)]*\)", " ", s)
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9+ ]+", " ", s)
    return " ".join(s.split())


def _terms(raw) -> list[str]:
    terms = []
    for t in raw or []:
        n = norm_name(t)
        if n:
            terms.append(n)
    return sorted(set(terms), key=len, reverse=True)


def banned_terms(settings=None) -> list[str]:
    cfg = (settings or _load_settings()).get("company_filter") or {}
    return _terms(cfg.get("exclude_company_names"))


def current_employer_terms(settings=None) -> list[str]:
    cfg = (settings or _load_settings()).get("company_filter") or {}
    return _terms(cfg.get("current_employer_names"))


def _name_hits_term(name: str, term: str) -> bool:
    if not name or not term:
        return False
    if " " in term:
        return term in name
    return bool(re.search(rf"(?:^| ){re.escape(term)}(?: |$)", name))


def is_banned_company(company: str, settings=None) -> tuple[bool, str]:
    name = norm_name(company)
    if not name:
        return False, ""
    for term in banned_terms(settings):
        if _name_hits_term(name, term):
            return True, term
    return False, ""


def is_current_employer(company: str, settings=None) -> tuple[bool, str]:
    name = norm_name(company)
    if not name:
        return False, ""
    for term in current_employer_terms(settings):
        if _name_hits_term(name, term):
            return True, term
    return False, ""


def is_same_company(a: str, b: str) -> bool:
    na, nb = norm_name(a), norm_name(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    shorter, longer = (na, nb) if len(na) <= len(nb) else (nb, na)
    if shorter not in longer:
        return False
    # Avoid matching tiny tokens ("ai", "hive") against unrelated names.
    if " " in shorter or len(shorter) >= 6:
        return True
    return False


def applied_count_for_company(company: str, rows=None) -> int:
    rows = rows if rows is not None else _load_tracker_rows()
    n = 0
    for r in rows:
        if (r.get("status") or "").strip() != "applied":
            continue
        if is_same_company(company, r.get("company") or ""):
            n += 1
    return n


def max_applies_per_company(settings=None) -> int:
    cfg = (settings or _load_settings()).get("company_filter") or {}
    try:
        return int(cfg.get("max_applies_per_company") or 5)
    except (TypeError, ValueError):
        return 5


def decide(company: str, settings=None, rows=None) -> dict:
    settings = settings or _load_settings()
    banned, term = is_banned_company(company, settings)
    if banned:
        return {
            "company": company,
            "allowed": False,
            "reason": f"top_tier_mnc:{term}",
            "status": "skipped_company",
            "applied_count": applied_count_for_company(company, rows),
        }
    current, term = is_current_employer(company, settings)
    if current:
        return {
            "company": company,
            "allowed": False,
            "reason": f"current_employer:{term}",
            "status": "skipped_company",
            "applied_count": applied_count_for_company(company, rows),
        }
    cap = max_applies_per_company(settings)
    n = applied_count_for_company(company, rows)
    if n >= cap:
        return {
            "company": company,
            "allowed": False,
            "reason": f"max_applies_per_company:{n}>={cap}",
            "status": "skipped_company",
            "applied_count": n,
        }
    return {
        "company": company,
        "allowed": True,
        "reason": "mid_or_unlisted",
        "status": "ok",
        "applied_count": n,
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
        "Syren Cloud",
        "Syren Cloud (Databricks Partner)",
        "Syren",
    ]
    must_allow = [
        "Phoenix Contact",
        "Phoenix Contact India",
        "Appsquadz",
        "Areness",
        "Kahuna Labs",
        "Nablon AI",
        "A random Noida analytics firm",
        "LatentView",
        "Comviva",
        "SquadStack.ai",
    ]
    failed = []
    for c in must_ban:
        d = decide(c, settings, rows=[])
        if d["allowed"]:
            failed.append(f"should ban {c!r} got {d}")
    for c in must_allow:
        d = decide(c, settings, rows=[])
        if not d["allowed"]:
            failed.append(f"should allow {c!r} got {d}")
    # Partner-in-name must still skip Syren as current employer, not because Databricks is banned.
    d = decide("Syren Cloud (Databricks Partner)", settings, rows=[])
    if d["allowed"] or "current_employer" not in d["reason"]:
        failed.append("Syren Cloud (Databricks Partner) must skip as current_employer")
    # Cap: 5 applied rows to the same company
    cap_rows = [{"status": "applied", "company": "Phoenix Contact"} for _ in range(5)]
    d = decide("Phoenix Contact", settings, rows=cap_rows)
    if d["allowed"] or "max_applies_per_company" not in d["reason"]:
        failed.append("5 applied rows must skip Phoenix Contact")
    d = decide("Phoenix Contact", settings, rows=cap_rows[:4])
    if not d["allowed"]:
        failed.append("4 applied rows must still allow Phoenix Contact")
    if failed:
        print("FAIL")
        for line in failed:
            print(" ", line)
        return 1
    print("ok  banned", len(must_ban), "allowed", len(must_allow), "cap", max_applies_per_company(settings))
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

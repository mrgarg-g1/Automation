#!/usr/bin/env python3
"""Job application tracker CLI.

Usage:
  python scripts/tracker.py add --platform P --title T --company C --url U --status S [--score N] [--notes "..."]
  python scripts/tracker.py list [--status S] [--platform P] [--days N]
  python scripts/tracker.py stats
  python scripts/tracker.py check --url U            # duplicate check (exit 0 = new, 1 = seen)
  python scripts/tracker.py export --out tracker/export.csv
"""
import argparse
import csv
import os
import sys
from collections import Counter
from datetime import datetime, timedelta

TRACKER = os.path.join(os.path.dirname(__file__), "..", "tracker", "applications.csv")
FIELDS = ["date", "platform", "title", "company", "url", "status", "score", "notes"]
VALID_STATUSES = {
    "applied", "skipped_low_fit", "skipped_duplicate", "blocked",
    "failed", "signup_done", "needs_user_action",
}


def _ensure():
    os.makedirs(os.path.dirname(TRACKER), exist_ok=True)
    if not os.path.exists(TRACKER):
        with open(TRACKER, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(FIELDS)


def _rows():
    _ensure()
    with open(TRACKER, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def norm(s):
    return " ".join((s or "").lower().split())


def cmd_add(a):
    if a.status not in VALID_STATUSES:
        sys.exit(f"invalid status {a.status!r}; valid: {sorted(VALID_STATUSES)}")
    _ensure()
    with open(TRACKER, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow({
            "date": datetime.now().isoformat(timespec="seconds"),
            "platform": a.platform, "title": a.title, "company": a.company,
            "url": a.url, "status": a.status,
            "score": a.score if a.score is not None else "", "notes": a.notes,
        })
    print(f"logged: [{a.status}] {a.title} @ {a.company}")


def cmd_list(a):
    rows = _rows()
    if a.status:
        rows = [r for r in rows if r["status"] == a.status]
    if a.platform:
        rows = [r for r in rows if norm(r["platform"]) == norm(a.platform)]
    if a.days:
        cutoff = (datetime.now() - timedelta(days=a.days)).isoformat()
        rows = [r for r in rows if r["date"] >= cutoff]
    for r in rows:
        print(f"{r['date'][:10]}  {r['platform']:<14} {r['status']:<18} {r['title'][:45]:<45} {r['company'][:25]}")


def cmd_stats(_):
    rows = _rows()
    total = Counter(r["status"] for r in rows)
    per_platform = Counter((r["platform"], r["status"]) for r in rows)
    print(f"total rows: {len(rows)}")
    for s, n in total.most_common():
        print(f"  {s:<20} {n}")
    print("\nby platform:")
    for (p, s), n in sorted(per_platform.items()):
        print(f"  {p:<14} {s:<20} {n}")
    applied = [r for r in rows if r["status"] == "applied" and r["score"]]
    if applied:
        avg = sum(float(r["score"]) for r in applied) / len(applied)
        print(f"\navg fit score of applied: {avg:.1f}")


def cmd_check(a):
    rows = _rows()
    if any(norm(r["url"]) == norm(a.url) for r in rows if r["url"]):
        print("seen (url)")
        sys.exit(1)
    if a.title and a.company and any(
        norm(r["title"]) == norm(a.title) and norm(r["company"]) == norm(a.company)
        for r in rows
    ):
        print("seen (title+company)")
        sys.exit(1)
    print("new")
    sys.exit(0)


def cmd_export(a):
    _ensure()
    with open(TRACKER, encoding="utf-8") as src, open(a.out, "w", newline="", encoding="utf-8") as dst:
        dst.write(src.read())
    print(f"exported -> {a.out}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add")
    pa.add_argument("--platform", required=True)
    pa.add_argument("--title", required=True)
    pa.add_argument("--company", required=True)
    pa.add_argument("--url", default="")
    pa.add_argument("--status", required=True)
    pa.add_argument("--score", type=float)
    pa.add_argument("--notes", default="")
    pa.set_defaults(fn=cmd_add)

    pl = sub.add_parser("list")
    pl.add_argument("--status")
    pl.add_argument("--platform")
    pl.add_argument("--days", type=int)
    pl.set_defaults(fn=cmd_list)

    ps = sub.add_parser("stats")
    ps.set_defaults(fn=cmd_stats)

    pc = sub.add_parser("check")
    pc.add_argument("--url", default="")
    pc.add_argument("--title", default="")
    pc.add_argument("--company", default="")
    pc.set_defaults(fn=cmd_check)

    pe = sub.add_parser("export")
    pe.add_argument("--out", required=True)
    pe.set_defaults(fn=cmd_export)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

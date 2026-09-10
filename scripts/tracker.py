#!/usr/bin/env python3
"""Job application tracker CLI.

Usage:
  python scripts/tracker.py add --platform P --title T --company C --url U --status S [--score N] [--notes "..."]
  python scripts/tracker.py list [--status S] [--platform P] [--days N]
  python scripts/tracker.py stats
  python scripts/tracker.py health [--json]
  python scripts/tracker.py check --url U            # duplicate check (exit 0 = new, 1 = seen)
  python scripts/tracker.py export --out tracker/export.csv
"""
import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TRACKER = os.path.join(ROOT, "tracker", "applications.csv")
SETTINGS = os.path.join(ROOT, "config", "settings.json")
FIELDS = ["date", "platform", "title", "company", "url", "status", "score", "notes"]
VALID_STATUSES = {
    "applied", "skipped_low_fit", "skipped_duplicate", "blocked",
    "failed", "signup_done", "needs_user_action",
}
# Real apply attempts only. skipped_* / signup_done do not count toward failure %.
ATTEMPT_STATUSES = {"applied", "blocked", "failed", "needs_user_action"}
FAIL_STATUSES = {"blocked", "failed", "needs_user_action"}
DEFAULT_FAIL_PCT = 80
DEFAULT_MIN_ATTEMPTS = 5


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


def _load_settings():
    if not os.path.isfile(SETTINGS):
        return {}
    with open(SETTINGS, encoding="utf-8") as f:
        return json.load(f)


def platform_health(rows, fail_pct_threshold=DEFAULT_FAIL_PCT, min_attempts=DEFAULT_MIN_ATTEMPTS):
    """Return per-platform KEEP/SKIP from apply-attempt failure rate.

    attempts = applied + blocked + failed + needs_user_action
    fail = blocked + failed + needs_user_action
    SKIP when attempts >= min_attempts and fail/attempts * 100 > fail_pct_threshold.
    """
    counts = defaultdict(Counter)
    for r in rows:
        p = (r.get("platform") or "").strip()
        if p:
            counts[p][r.get("status") or ""] += 1
    out = []
    for platform in sorted(counts):
        c = counts[platform]
        applied = c["applied"]
        fail = sum(c[s] for s in FAIL_STATUSES)
        attempts = sum(c[s] for s in ATTEMPT_STATUSES)
        fail_pct = (100.0 * fail / attempts) if attempts else None
        skip = (
            attempts >= min_attempts
            and fail_pct is not None
            and fail_pct > fail_pct_threshold
        )
        out.append({
            "platform": platform,
            "applied": applied,
            "fail": fail,
            "attempts": attempts,
            "fail_pct": None if fail_pct is None else round(fail_pct, 1),
            "health": "SKIP" if skip else "KEEP",
        })
    return out


def cmd_health(a):
    settings = _load_settings()
    fail_pct = settings.get("skip_platform_if_failure_pct", DEFAULT_FAIL_PCT)
    min_attempts = settings.get("skip_platform_min_attempts", DEFAULT_MIN_ATTEMPTS)
    enabled = {
        p.get("name"): bool(p.get("enabled"))
        for p in settings.get("platforms") or []
        if p.get("name")
    }
    rows = platform_health(_rows(), fail_pct, min_attempts)
    for r in rows:
        r["settings"] = "enabled" if enabled.get(r["platform"]) else (
            "disabled" if r["platform"] in enabled else "unlisted"
        )
    skip = [r["platform"] for r in rows if r["health"] == "SKIP"]
    payload = {
        "skip_platform_if_failure_pct": fail_pct,
        "skip_platform_min_attempts": min_attempts,
        "platforms": rows,
        "skip": skip,
    }
    if a.as_json:
        print(json.dumps(payload, indent=2))
        return
    print(
        f"skip if failure > {fail_pct}% with at least {min_attempts} apply attempts "
        "(skipped_low_fit / skipped_duplicate / signup_done do not count)"
    )
    print(
        f"{'platform':<16} {'applied':>8} {'fail':>6} {'attempts':>9} {'fail%':>7}  "
        f"{'health':<6} {'settings'}"
    )
    for r in rows:
        pct = "—" if r["fail_pct"] is None else f"{r['fail_pct']:.0f}%"
        print(
            f"{r['platform']:<16} {r['applied']:>8} {r['fail']:>6} {r['attempts']:>9} "
            f"{pct:>7}  {r['health']:<6} {r['settings']}"
        )
    if skip:
        print(f"\nSKIP platforms (do not search or apply): {', '.join(skip)}")
        still_on = [p for p in skip if enabled.get(p)]
        if still_on:
            print(f"WARNING: still enabled in settings.json — treat as disabled: {', '.join(still_on)}")
    else:
        print("\nSKIP platforms (do not search or apply): (none)")


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

    ph = sub.add_parser("health")
    ph.add_argument("--json", dest="as_json", action="store_true")
    ph.set_defaults(fn=cmd_health)

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

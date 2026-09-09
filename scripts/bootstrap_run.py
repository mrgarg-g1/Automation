#!/usr/bin/env python3
"""Ensure this checkout is latest origin/main and the profile/resume are present.

Cursor cloud runs sometimes start on a stale environment snapshot from the
first commit (empty profile.json, resume/ gitignored). Pull before applying.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)


def run(args):
    p = subprocess.run(args, capture_output=True, text=True)
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    return p.returncode, out, err


def head():
    code, out, _ = run(["git", "rev-parse", "--short", "HEAD"])
    return out if code == 0 else "unknown"


def logline():
    code, out, _ = run(["git", "log", "-1", "--oneline"])
    return out if code == 0 else ""


def profile_name():
    path = os.path.join(ROOT, "config", "profile.json")
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return (data.get("full_name") or "").strip()


def resume_ok():
    return os.path.isfile(os.path.join(ROOT, "resume", "Resume.pdf"))


def pull_latest():
    run(["git", "remote", "-v"])
    code, out, err = run(["git", "fetch", "origin", "main"])
    print(f"git fetch origin main -> {code}")
    if out:
        print(out)
    if err:
        print(err)
    # Prefer tracking branch; fall back to detached origin/main
    code2, out2, err2 = run(["git", "checkout", "-B", "main", "origin/main"])
    print(f"git checkout -B main origin/main -> {code2}")
    if out2:
        print(out2)
    if err2:
        print(err2)
    return code == 0 and code2 == 0


def main():
    print(f"cwd={ROOT}")
    print(f"before: {logline() or head()}")
    name = profile_name()
    pdf = resume_ok()
    print(f"before: profile.full_name={name!r} resume_pdf={pdf}")

    stale = (not name) or (not pdf)
    if stale:
        print("Checkout looks stale or incomplete — pulling origin/main")
        if not pull_latest():
            print("ERROR: git fetch/checkout failed. In the Automations editor, set repository to mrgarg-g1/Automation, branch main, then update/rebuild the Cloud Agent environment.", file=sys.stderr)
            return 1

    print(f"after: {logline() or head()}")
    name = profile_name()
    pdf = resume_ok()
    print(f"after: profile.full_name={name!r} resume_pdf={pdf}")

    if not name:
        print("ERROR: config/profile.json still has no full_name after pull. This VM is not on latest main.", file=sys.stderr)
        return 1
    if not pdf:
        print("ERROR: resume/Resume.pdf missing after pull.", file=sys.stderr)
        return 1
    print(f"READY: {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

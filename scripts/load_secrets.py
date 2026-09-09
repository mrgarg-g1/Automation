#!/usr/bin/env python3
"""Materialize config/credentials.env from Cursor Cloud Agent secrets.

Cloud automations check out GitHub — they never get the gitignored credentials
file. Put the same keys in Cursor dashboard Secrets
(https://cursor.com/dashboard/cloud-agents). This script writes them locally
for the rest of the run.

Local runs: if credentials.env already exists, this is a no-op.
"""
import os
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
DEST = os.path.join(ROOT, "config", "credentials.env")

KEYS = [
    "MASTER_EMAIL",
    "MASTER_PASSWORD",
    "ZIPRECRUITER_EMAIL",
    "ZIPRECRUITER_PASSWORD",
    "INSTAHYRE_EMAIL",
    "INSTAHYRE_PASSWORD",
    "FLEXJOBS_EMAIL",
    "FLEXJOBS_PASSWORD",
]


def main():
    if os.path.exists(DEST):
        print("credentials.env already present (local file); leaving it as-is")
        return 0

    found = {k: os.environ.get(k, "").strip() for k in KEYS}
    if not found["MASTER_EMAIL"] or not found["MASTER_PASSWORD"]:
        print(
            "No credentials.env and MASTER_EMAIL / MASTER_PASSWORD are not set.\n"
            "Add them as Runtime Secrets at https://cursor.com/dashboard/cloud-agents\n"
            "or copy config/credentials.env.example -> config/credentials.env for local runs.",
            file=sys.stderr,
        )
        return 1

    lines = [
        "# Generated at run start from Cursor Cloud Agent secrets. Do not commit.",
        f"MASTER_EMAIL={found['MASTER_EMAIL']}",
        f"MASTER_PASSWORD={found['MASTER_PASSWORD']}",
        "",
    ]
    for k in KEYS[2:]:
        if found[k]:
            lines.append(f"{k}={found[k]}")
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote config/credentials.env from environment secrets (values not printed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

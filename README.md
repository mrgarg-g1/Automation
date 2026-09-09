# Job Application Automation (Cursor-native)

A robust, resume-driven job application system that runs on **Cursor's browser agent** — no Apify, no external bots. Hybrid mode: supervised local runs for signups/OAuth/captcha, plus a scheduled cloud Automation for daily applying once accounts exist.

## How it works

```
Resume.pdf ──► config/profile.json ──► RUNBOOK.md (master agent brain)
                                            │
                    ┌───────────────────────┼────────────────────────┐
                    ▼                       ▼                        ▼
            playbooks/*.md          config/settings.json      tracker/applications.csv
        (per-platform steps)      (caps, filters, prefs)      (every attempt logged)
```

Each run, the Cursor agent:
1. Loads your profile + settings.
2. Picks platforms in rotation, logs in (or signs up with email+password from `config/credentials.env`).
3. Searches with your role/location/remote filters, scores each job against your resume (fit rubric in `RUNBOOK.md`).
4. Applies only to jobs above the fit threshold, with human-like pacing and a daily cap.
5. Logs everything to the tracker and prints a run summary.

## Files

| Path | Purpose |
|------|---------|
| `RUNBOOK.md` | Master instructions the agent follows every run |
| `config/profile.json` | Your structured resume data (auto-built from Resume.pdf) |
| `config/settings.json` | Platforms, daily caps, search queries, fit threshold |
| `config/credentials.env` | Email/password per platform (local only — never commit) |
| `playbooks/` | Step-by-step application flows per platform |
| `tracker/applications.csv` | Every application attempt + status |
| `scripts/tracker.py` | CLI to add/query/export tracker rows |
| `automations/daily-apply.md` | Prompt draft for the scheduled Cursor cloud Automation |

## Quick start

1. Drop `Resume.pdf` into `resume/` and tell the agent — it builds `config/profile.json`.
2. Fill in `config/credentials.env` (one master email+password; reused per platform unless overridden).
3. Say **"run the job automation"** (or `run ziprecruiter only`, `dry run`, etc.).
4. Complete any captcha/email-verification prompts when the agent hands off to you.

## Safety rails (built in)

- Daily + per-platform caps with randomized 45–120s delays between applications.
- Never re-applies to a job already in the tracker (URL + title+company dedupe).
- Skips jobs below the resume-fit threshold — no spray-and-pray.
- Stops and asks you on: captcha, email/phone verification, payment walls (FlexJobs), ambiguous screening questions, or any ToS-sensitive prompt.

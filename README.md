# Job Application Automation (Cursor-native)

A robust, resume-driven job application system for **Cursor Automations**. Playbooks live in this GitHub repo. Job-site passwords live in Cursor Cloud Agent Secrets. Apify stays connected on the automation (not in git).

## How it works

```
resume/Resume.pdf ──► config/profile.json ──► RUNBOOK.md (master agent brain)
                                            │
                    ┌───────────────────────┼────────────────────────┐
                    ▼                       ▼                        ▼
            playbooks/*.md          config/settings.json      tracker/applications.csv
        (per-platform steps)      (caps, filters, prefs)      (every attempt logged)
```

Each run, the Cursor agent:
1. Loads your profile + settings.
2. Loads credentials (`scripts/load_secrets.py` from Cloud Agent secrets, or local `config/credentials.env`), then logs in or signs up.
3. Searches with your role/location/remote filters, scores each job against your resume (fit rubric in `RUNBOOK.md`).
4. Applies only to jobs above the fit threshold, with human-like pacing and a daily cap.
5. Logs everything to the tracker and prints a run summary.

## Files

| Path | Purpose |
|------|---------|
| `RUNBOOK.md` | Master instructions the agent follows every run |
| `resume/Resume.pdf` | Canonical PDF attached on applications |
| `config/profile.json` | Structured resume data used for forms and fit scoring |
| `config/settings.json` | Platforms, daily caps, search queries, fit threshold |
| `config/credentials.env` | Email/password (local only — gitignored, never commit) |
| `config/credentials.env.example` | Key names to copy into Cursor Cloud Agent Secrets |
| `playbooks/` | Step-by-step application flows per platform |
| `tracker/applications.csv` | Every application attempt + status |
| `scripts/load_secrets.py` | Writes credentials.env from Cloud Agent env vars |
| `scripts/tracker.py` | CLI to add/query/export tracker rows; `health` skips platforms over 80% apply-attempt failure |
| `automations/daily-apply.md` | Prompt + credential wiring for the scheduled Cursor Automation |

## Quick start

1. Resume lives at `resume/Resume.pdf`; `config/profile.json` is already filled from it.
2. Fill in `config/credentials.env` (one master email+password; reused per platform unless overridden).
3. Say **"run the job automation"** (or `run ziprecruiter only`, `dry run`, etc.).
4. Complete any captcha/email-verification prompts when the agent hands off to you.

## Safety rails (built in)

- Daily + per-platform caps with randomized 45–120s delays between applications.
- Never re-applies to a job already in the tracker (URL + title+company dedupe).
- Skips jobs below the resume-fit threshold — no spray-and-pray.
- Skips platforms whose apply-attempt failure rate is above 80% (`python3 scripts/tracker.py health`).
- Stops and asks you on: captcha, email/phone verification, payment walls (FlexJobs), ambiguous screening questions, or any ToS-sensitive prompt.

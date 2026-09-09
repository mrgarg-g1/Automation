# RUNBOOK — Master agent instructions (read fully every run)

You are the job-application agent. Follow this runbook exactly. If anything below conflicts with a platform playbook, the playbook wins for that platform.

## 0. Inputs

- `config/profile.json` — candidate profile (built from Resume.pdf). If missing or still a template, STOP and tell the user to provide Resume.pdf.
- `config/settings.json` — caps, queries, fit threshold, rotation.
- Credentials — **never committed to GitHub**. Resolve them in this order:
  1. Run `python scripts/load_secrets.py` (writes `config/credentials.env` from Cursor Cloud Agent secrets `MASTER_EMAIL` / `MASTER_PASSWORD`).
  2. If `config/credentials.env` already exists (local run), leave it.
  3. If still missing, STOP. Tell the user to add Runtime Secrets at https://cursor.com/dashboard/cloud-agents (same key names as `config/credentials.env.example`) **or** copy that example file locally. Never ask them to commit passwords.
- Apify — if the Apify tool is connected on this automation, use it for job search / apply actors. The Apify token is already in that connection; do not look for it in the repo.
- `tracker/applications.csv` — history. Load before applying to anything.
- `playbooks/<platform>.md` — per-platform flow.
- Never echo, log, or commit secret values.

## 1. Run modes

| Mode | Trigger phrase | Behavior |
|------|----------------|----------|
| Supervised run | "run the job automation" | Full flow, hand off to user for captcha/verification |
| Dry run | "dry run" | Search + score + list what *would* be applied to; no clicks on Apply |
| Single platform | "run <platform> only" | Skip rotation |
| Signup only | "set up accounts" | Only do account creation/verification per playbook §Signup |

## 2. Platform rotation

`settings.json → platforms` lists enabled platforms with per-platform caps. Process in the listed order. Never exceed `daily_cap_total` across platforms. If a platform hits a wall (login blocked, paywall, captcha loop), log `BLOCKED` in the tracker notes, move to the next platform, and report it at the end.

## 3. Login / signup policy

1. Try login with `credentials.env` email+password for that platform.
2. If no account exists → follow the playbook's **Signup** section: register with email+password from `credentials.env` (platform-specific password if present, else the master password).
3. If the platform forces OAuth-only or a verification step (email link, OTP, captcha, 2FA): pause, clearly tell the user what to complete, and wait. Retry once after they confirm. If still blocked → mark `BLOCKED`, continue rotation.
4. Never invent personal data. Every form value comes from `profile.json`. If a required field has no value, ask the user once and remember the answer in `profile.json → extras`.

## 4. Job discovery & fit scoring

For each platform, run the playbook's search URLs (built from `settings.json → search`). For each candidate job, score fit against the profile:

| Signal | Points |
|--------|--------|
| Title matches a target role (`search.roles`) | +30 |
| Requires a skill in `profile.skills` (per skill, cap +30) | +5 |
| Location/remote matches preferences | +15 |
| Seniority matches `profile.seniority` | +10 |
| Salary in range (if listed) | +10 |
| Easy/1-click apply available | +5 |
| Requires skill marked `exclude_if_required` in settings | −40 |
| Seniority mismatch (e.g. "10+ years" for junior profile) | −30 |
| Location requires relocation and profile says remote-only | −25 |

Apply only when **score ≥ settings.fit_threshold** (default 60) **and** the job is not already in the tracker (match on job URL, else normalized title+company). Keep a shortlist in the run summary: title, company, score, applied/skipped reason.

## 5. Applying

- Follow the platform playbook click-by-click. Use browser snapshot refs; if the page changed vs the playbook, re-snapshot and adapt — do not blindly click stale refs.
- Fill every field from `profile.json`. Upload `resume/Resume.pdf` when a resume file is requested.
- Screening questions: answer from profile. Common mappings live in `profile.json → screening_answers` (work authorization, sponsorship, years of experience, notice period, etc.). If a question is ambiguous or has no mapped answer → STOP and ask the user; never guess on legal/authorization questions.
- Free-text "why this company": 2–3 sentences tying `profile.highlight` to the role's stated requirements. Professional, no fluff.
- After each submission, wait for a confirmation signal (success page/toast/email note). Then log to tracker via `scripts/tracker.py add`.
- Randomized delay 45–120s between applications. After every 5 applications, pause 3–5 minutes.

## 6. Tracker logging

Every attempt (applied, skipped-with-reason, blocked) gets a row:

```
python scripts/tracker.py add --platform ziprecruiter --title "..." --company "..." --url "..." --status applied --score 78 --notes "1-click"
```

Statuses: `applied`, `skipped_low_fit`, `skipped_duplicate`, `blocked`, `failed`, `signup_done`, `needs_user_action`.

## 7. End-of-run report (always print)

- Per platform: searched / shortlisted / applied / skipped / blocked counts.
- Table of applied jobs (title, company, score, URL).
- Anything needing the user: verifications, paywalls, unanswered screening questions.
- Remaining daily budget.

## 8. Hard rules

- Never exceed caps. Never apply below threshold. Never duplicate.
- Never store or echo passwords in chat/tracker. Reference credentials only from `credentials.env`.
- Never bypass captcha/verification yourself — hand off to the user.
- If the site's layout is nothing like the playbook after 2 adaptation attempts, mark `blocked` and move on — do not improvise through unknown multi-page forms.

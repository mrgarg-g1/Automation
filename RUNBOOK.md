# RUNBOOK — Master agent instructions (read fully every run)

You are the job-application agent. Follow this runbook exactly. If anything below conflicts with a platform playbook, the playbook wins for that platform.

## 0. Inputs

**First command every run** (before judging the profile):

```
python scripts/bootstrap_run.py
python scripts/load_secrets.py
```

`bootstrap_run.py` prints the git SHA, pulls `origin/main` if `config/profile.json` is empty or `resume/Resume.pdf` is missing, then re-checks. If it still fails, STOP — the automation is pointed at the wrong repo/branch or a stale Cloud Agent snapshot. Report the SHA it printed.

- `config/profile.json` — candidate profile. Ready when `full_name` is `"Deepak Garg"`. Empty name/skills means a **stale checkout**, not a missing resume. Do not tell the user to "fill the template" if GitHub already has the profile; tell them to set repo `mrgarg-g1/Automation` branch `main` and update the Cloud Agent environment.
- `resume/Resume.pdf` — canonical PDF to attach. It is tracked in git (not ignored).
- `config/settings.json` — caps, queries, fit threshold, rotation.
- Credentials — **never committed to GitHub**. Resolve them in this order:
  1. `python scripts/load_secrets.py` (writes `config/credentials.env` from Cursor Cloud Agent secrets `MASTER_EMAIL` / `MASTER_PASSWORD`).
  2. If `config/credentials.env` already exists (local run), leave it.
  3. If still missing, STOP. Tell the user to add Runtime Secrets at https://cursor.com/dashboard/cloud-agents (same key names as `config/credentials.env.example`) **or** copy that example file locally. Never ask them to commit passwords.
- Apify — connected tool (`Tools → Apify`). Use for job search. Token is not in git.
- Gmail — connected tool (`Tools → Gmail`, read). Same wiring as Apify. Follow `playbooks/gmail-otp.md` for OTPs. Never commit mail.
- `AGENTS.md` — models, captcha/OTP, computerUse ban. Read first.
- `tracker/applications.csv` — history. Load before applying to anything.
- `tracker/open-actions.md` — captchas/OTPs still waiting. Keep highlighting until cleared.
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

`settings.json → platforms` lists enabled platforms with per-platform caps. Process in the listed order. Never exceed `daily_cap_total` across platforms.

Right after bootstrap, run:

```
python3 scripts/tracker.py health
```

If a platform's apply-attempt failure rate is **above** `skip_platform_if_failure_pct` (default 80) with at least `skip_platform_min_attempts` (default 5) attempts, `health` prints `SKIP`. **Do not search or apply on SKIP platforms** — even if `enabled` is still true. Attempts = `applied` + `blocked` + `failed` + `needs_user_action`. `skipped_low_fit` / `skipped_duplicate` / `signup_done` do not count.

If a platform hits a wall (login blocked, paywall, captcha loop), log `BLOCKED` in the tracker notes, move to the next platform, and report it at the end. Re-run `health` after logging; a platform that just crossed 80% is skipped for the rest of the run.

## 3. Login / signup policy

1. Try login with `credentials.env` email+password for that platform.
2. If no account exists → follow the playbook's **Signup** section: register with email+password from `credentials.env` (platform-specific password if present, else the master password).
3. **Email OTP / verification codes — do not wait for the user.** Gmail is connected. As soon as a site sends an OTP:
   1. Fetch it from the connected Gmail / Updates inbox (search recent mail from that site: ZipRecruiter, Greenhouse, Instahyre, Lever, etc.).
   2. Fill the code and continue the application.
   3. Never print the full OTP in chat, tracker notes, screenshots-as-text, or git. Say only `otp_from_gmail`.
   4. If Gmail/Updates is missing or the code is not in the inbox within ~2 minutes → log `needs_user_action` with note `otp_gmail_miss`, **notify immediately**, then continue other jobs (do not freeze the run).
4. **Captcha / picture puzzles — never sit and wait.** Do not try to solve captchas. Immediately:
   1. Post a user-visible **CAPTCHA — ACTION NEEDED NOW** alert (platform, job title, company, URL, what to click).
   2. Log `needs_user_action` with note `captcha_waiting`.
   3. Leave that tab/form as-is if possible, **continue other applications** (next platform / next job).
   4. **Keep highlighting** every open captcha in every later status message and in the §7 report until the user says they filled it or the listing expired. Do not bury captcha in a batch report at the end of the run.
5. Payment walls → `blocked`, continue. OAuth-only with no email path → `blocked`, continue.
6. Never invent personal data. Every form value comes from `profile.json`. If a required field has no value, ask the user once and remember the answer in `profile.json → extras`.

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

Location match means: **fully remote / WFH worldwide** (including outside India), or **hybrid/onsite in Gurugram, Noida, or Delhi (NCR) only**. Hybrid or onsite anywhere else (US office days, Bangalore, Hyderabad office, Chennai office, etc.) does **not** get location points and should be skipped unless the listing is also fully remote.

Apply only when **score ≥ settings.fit_threshold** (default 60) **and** the job is not already in the tracker (match on job URL, else normalized title+company). Keep a shortlist in the run summary: title, company, score, applied/skipped reason.

## 5. Applying

- Follow the platform playbook click-by-click. Use browser snapshot refs; if the page changed vs the playbook, re-snapshot and adapt — do not blindly click stale refs.
- Fill every field from `profile.json`. Upload `resume/Resume.pdf` when a resume file is requested.
- Screening questions: answer from profile. Common mappings live in `profile.json → screening_answers` (work authorization, sponsorship, years of experience, notice period, etc.). If a question is ambiguous or has no mapped answer → STOP and ask the user; never guess on legal/authorization questions.
- Free-text "why this company": 2–3 sentences tying `profile.highlight` to the role's stated requirements. Professional, no fluff.
- After each submission, wait for a confirmation signal (success page/toast/email note). Then log to tracker via `scripts/tracker.py add`.
- Randomized delay 45–120s between applications. After every 5 applications, pause 3–5 minutes.
- Open captcha items stay in a live queue. Re-state that queue after every subsequent apply (or skip) until cleared.

## 6. Tracker logging

Every attempt (applied, skipped-with-reason, blocked) gets a row:

```
python scripts/tracker.py add --platform ziprecruiter --title "..." --company "..." --url "..." --status applied --score 78 --notes "1-click"
```

Statuses: `applied`, `skipped_low_fit`, `skipped_duplicate`, `blocked`, `failed`, `signup_done`, `needs_user_action`.

## 7. End-of-run report (always print)

- Per platform: searched / shortlisted / applied / skipped / blocked counts.
- Table of applied jobs (title, company, score, URL).
- **Open captcha queue first** (still waiting): title, company, URL — keep listing until the user confirms they filled it.
- Anything else needing the user: OTP Gmail miss, paywalls, unanswered screening questions.
- Remaining daily budget.

## 8. Hard rules

- Never exceed caps. Never apply below threshold. Never duplicate.
- Never store or echo passwords in chat/tracker. Reference credentials only from `credentials.env`.
- Never solve captchas yourself. Notify immediately, continue other jobs, keep highlighting until the user fills them.
- Email OTP: read from Gmail/Updates and fill. Do not pause the whole run on OTP.
- Never launch Claude / GPT / Gemini / computerUse-on-Other-Models. If browser apply cannot stay on Cursor Grok, stop and report.
- If the site's layout is nothing like the playbook after 2 adaptation attempts, mark `blocked` and move on — do not improvise through unknown multi-page forms.

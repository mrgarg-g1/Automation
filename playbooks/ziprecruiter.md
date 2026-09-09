# Playbook — ZipRecruiter

Base: `https://www.ziprecruiter.com`

## Signup (only if login fails / no account)

1. Go to `https://www.ziprecruiter.com/register` (or click "Sign Up" → job seeker).
2. Choose **email registration** (not Google/LinkedIn buttons).
3. Fill: first/last name from `profile.full_name`, email + password from `credentials.env` (`ZIPRECRUITER_*` override else `MASTER_*`).
4. If it asks to upload a resume during onboarding → upload `resume/Resume.pdf`. ZipRecruiter auto-parses it; verify parsed name/title roughly match, fix if wildly wrong.
5. Email verification or captcha → hand off to user, wait for confirmation.
6. Log `signup_done` in tracker (title=`account`, company=`ziprecruiter`).

## Login

`https://www.ziprecruiter.com/login` → email + password. If "forgot password" loop or captcha repeats twice → `blocked`, move on.

## Search

Build URL from settings:

```
https://www.ziprecruiter.com/jobs-search?search=<ROLE>&location=<LOCATION_OR_Remote>&days=<POSTED_WITHIN_DAYS>
```

- One search per role in `search.roles` (stop that role's listing when its platform cap share is met).
- Sort by date when the sort control exists.
- Fully remote US/global listings are OK. Hybrid/onsite: only Gurugram, Noida, Delhi — skip US-city hybrid.
- Email OTP: pause and ask the user for the code (they will share it); do not abandon the platform on the first OTP.

## Qualify

Open each listing in the results list. Score per RUNBOOK §4. Prefer listings labeled **"1-Click Apply"** — deprioritize "Apply on company site" unless the ATS matches `playbooks/ats-direct.md` (Greenhouse/Lever/Ashby/Workable), in which case hand off to that playbook.

## Apply (1-Click Apply)

1. Click **1-Click Apply**.
2. Confirm the resume shown is ours (name matches profile). If it offers to replace → upload `resume/Resume.pdf`.
3. If screening questions appear → answer from `profile.screening_answers`; unknown/ambiguous → STOP and ask user.
4. Submit. Wait for the "Application submitted" confirmation.
5. Log `applied` with the job URL, title, company, score.

## Failure handling

- "Already applied" badge → log `skipped_duplicate` (also add to tracker so future runs dedupe on URL).
- Listing expired / filled → `failed` with note.
- Session expired mid-run → re-login once; second time → `blocked`.

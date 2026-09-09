# Playbook — ATS-direct (Greenhouse / Lever / Ashby / Workable / other)

The shared engine for applications that happen on a company's own applicant tracking system — reached from Remote.co, Protocol boards, FlexJobs "company site" links, etc.

## Identify the ATS from the URL

| URL pattern | ATS |
|---|---|
| `boards.greenhouse.io`, `job-boards.greenhouse.io` | Greenhouse |
| `jobs.lever.co` | Lever |
| `jobs.ashbyhq.com` | Ashby |
| `apply.workable.com` | Workable |
| `*.myworkdayjobs.com` | Workday (see special rules) |
| anything else | Generic — one careful attempt, else `blocked` |

## Greenhouse

Single long form. Map: first/last name, email, phone, location, LinkedIn (`profile.links.linkedin`), GitHub/portfolio. Resume upload → `resume/Resume.pdf`. Cover letter: only if **required** → RUNBOOK §5 free-text rule. Custom questions → `profile.screening_answers`; unknown → ask user. Submit → expect "Application submitted" page → log `applied`.

## Lever

`jobs.lever.co/<company>/<id>` → "Apply for this job" → form (name, email, phone, resume, LinkedIn/GitHub/Portfolio URLs, "additional information"). Fill from profile, upload resume, submit → confirmation page → log `applied`.

## Ashby

Two-step: form → review page. Fill basics + resume; on the review step verify parsed resume fields (Ashby re-parses the PDF — fix name/phone if mangled), then submit.

## Workable

`apply.workable.com` forms may ask to autofill from resume — allow it, then verify parsed fields. Some listings start a short "screening" chat-like flow; answer from profile only.

## Workday (special)

Workday almost always requires creating a per-company account (email + password) with email verification, and its forms are long, multi-step, and fragile.

1. Create the account with the platform email+password from `credentials.env` (reuse master password — one password per ATS keeps it memorable).
2. Email verification → hand off to user.
3. Multi-step form: use "autofill from resume" when offered, verify each step.
4. If the flow exceeds ~8 steps or hits repeated validation errors after 2 adaptation attempts → `blocked` with note "workday_complexity", continue rotation. Do not grind through broken Workday flows.

## Generic / unknown ATS

One careful attempt: fill obvious fields from profile, upload resume if asked. If the form is ambiguous, multi-page, or asks data we don't have → ask the user once; still unresolved → `blocked`.

## Hard rules for all ATS

- Every field value comes from `profile.json` / `credentials.env` — never invent.
- EEO/demographic voluntary questions: choose "Decline to self-identify" options when present; if forced, STOP and ask the user.
- Legal questions (authorization, sponsorship, non-compete): only from `profile.screening_answers`; unknown → STOP and ask.

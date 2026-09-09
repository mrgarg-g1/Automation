# Playbook — FlexJobs

Base: `https://www.flexjobs.com`

⚠️ **PAYWALL WARNING**: FlexJobs requires a paid subscription to see full listings and apply. If the user has not confirmed an active subscription, this platform stays `enabled: false` in settings. If we hit the paywall mid-run: log `blocked` with note "paywall", tell the user, and skip the platform.

## Signup (only with user's explicit go-ahead — involves payment)

1. `https://www.flexjobs.com/auth/signup` → email + password from `credentials.env`.
2. The subscription/payment step → **STOP. Always hand off to the user.** Never enter payment details.

## Login

`https://www.flexjobs.com/auth/login` → email + password.

## Search

```
https://www.flexjobs.com/search?search=<ROLE>&location=Remote&date=<DAYS>
```

Use the "100% Remote Work" filter when present.

## Qualify

Standard RUNBOOK §4 scoring. FlexJobs listings usually show salary + remote level — use both.

## Apply

Two listing types:

1. **Apply via FlexJobs** (internal form) → fill from profile, upload `resume/Resume.pdf` if asked, submit, log `applied`.
2. **Apply on company site** → hand off to `playbooks/ats-direct.md`.

## Notes

- FlexJobs saves resumes in the account ("Resume Profiles"). Keep exactly one, named after the profile, always current.

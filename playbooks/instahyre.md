# Playbook — Instahyre

Base: `https://www.instahyre.com`

India-focused platform; employers also post remote-global roles. Applications are typically 1-click once the profile is complete.

## Signup

1. `https://www.instahyre.com/signup/` → choose email registration.
2. Fill name/email/password from `credentials.env` (`INSTAHYRE_*` override else `MASTER_*`).
3. Complete the candidate profile wizard **from `profile.json`**: current title, years of experience, skills, expected salary (`profile.screening_answers.expected_salary`), notice period, location + "open to remote".
4. Upload `resume/Resume.pdf` when prompted.
5. Email OTP → RUNBOOK §3: read from Gmail/Updates and fill. Do not pause the run.
6. Log `signup_done`.

## Login

`https://www.instahyre.com/login/` → email + password.

## Search

```
https://www.instahyre.com/job-search/?q=<ROLE>&location=Remote
```

Also check the "Remote" filter chip. Sort by relevance/date if offered.

## Qualify

Standard RUNBOOK §4 scoring. Instahyre shows salary bands and "remote" tags on cards — use them. Skip roles requiring immediate joining if `profile.screening_answers.notice_period` is long.

## Apply

1. Open listing → **Apply** (usually 1-click with the completed profile).
2. If a short note to the recruiter is allowed → use the RUNBOOK §5 free-text rule.
3. Confirm submission toast/page → log `applied`.

## Notes

- Instahyre caps applications for incomplete profiles — if Apply is disabled, check profile completeness first and fill the missing section from `profile.json`.
- Recruiter messages may arrive later; not part of this automation (mention in the run report if seen).

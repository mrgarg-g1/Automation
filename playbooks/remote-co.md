# Playbook — Remote.co

Base: `https://remote.co`

Remote.co is an **aggregator**: most "Apply" buttons redirect to the company's own ATS (Greenhouse, Lever, Ashby, Workable, Workday…). The real application happens on that external page — use `playbooks/ats-direct.md` for those.

## Signup / login

No account needed to browse or apply (applications happen on the employer's site). Skip this section entirely.

## Search

- Remote roles index: `https://remote.co/remote-jobs`
- Category pages are useful, e.g. `https://remote.co/remote-jobs/data-science`, `https://remote.co/remote-jobs/developer` — pick categories matching `search.roles` (Data Scientist, AI Engineer, ML Engineer).
- Or use search: `https://remote.co/remote-jobs/search?search_keywords=<ROLE>`

## Qualify

1. Open listing, score per RUNBOOK §4.
2. Fully remote / "anywhere" is OK worldwide (including outside India). **Hybrid** listings are OK only for Gurugram, Noida, or Delhi. Skip US hybrid office-days (e.g. Texas/Arizona/Florida) and other non-NCR hybrid.
3. Skip listings marked as "anywhere in the world **with restrictions**" if they require US citizenship or exclude India. Time-zone overlap is OK.
4. Check the posting date on the listing page; skip anything older than `search.posted_within_days`.

## Apply

1. Click the listing's **Apply** button → lands on external ATS.
2. Identify the ATS from the URL (`boards.greenhouse.io`, `jobs.lever.co`, `ashbyhq.com`, `apply.workable.com`, `myworkdayjobs.com`, …).
3. Follow `playbooks/ats-direct.md` for that ATS.
4. If the ATS is unknown/multi-step-custom (e.g. Workday account creation): attempt once; if it requires creating a Workday-style account with email verification → hand off to user; if still blocked → `blocked`, continue.

## Notes

- Remote.co listings frequently expire before removal — a dead apply link = `failed` with note "expired", not an error in our flow.

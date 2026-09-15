# Playbook — Naukri (company-site apply only)

Base: `https://www.naukri.com`

The user already uses Naukri **Apply Now / Easy Apply** themselves. This agent must **never** click Naukri Apply Now, never post to `naukri.com/cloudgateway` apply endpoints, and never log an apply against a Naukri-hosted form.

Use Naukri only as a **discovery board**. Apply only when the listing redirects to the employer's own ATS / careers site.

## What counts as company-site apply

Apply if the listing has one of:

- `companyApplyJob: true`
- a non-empty `applyRedirectUrl` pointing off naukri.com
- a careers/ATS URL (Greenhouse, Lever, Ashby, Workable, Darwinbox, Workday, SmartRecruiters, company `/careers` page)

Skip (`skipped_duplicate` is wrong — use `blocked` with note `naukri_apply_now_only`) when:

- Apply is Naukri Apply Now / Easy Apply only
- `companyApplyJob` is false and there is no off-site redirect
- The URL stays on `naukri.com` after open

## Search

Build from `settings.json → search.roles` and locations. Prefer company-posted jobs, last 7 days.

```
https://www.naukri.com/<role>-jobs-in-gurgaon?k=<ROLE>&l=gurgaon&experience=4&jobAge=7&wfhType=0,2,3
https://www.naukri.com/<role>-jobs-in-noida?k=<ROLE>&l=noida&experience=4&jobAge=7
https://www.naukri.com/<role>-jobs-in-delhi?k=<ROLE>&l=delhi&experience=4&jobAge=7
https://www.naukri.com/<role>-jobs?k=<ROLE>&wfhType=2&jobAge=7
```

Remote (`wfhType=2`) is allowed worldwide. Hybrid/onsite: Gurugram / Noida / Delhi only.

Apify: `memo23/naukri-scraper` (has apply-redirect fields) or `valig/naukri-jobs-scraper`. Cap items; do not scrape thousands.

## Qualify

Standard RUNBOOK §4 scoring. Then:

1. `python3 scripts/company_filter.py --company NAME` — skip current employer (Syren Cloud), top-tier MNCs, and companies with 5+ `applied` rows.
2. Confirm the apply path is **company site**, not Naukri Apply Now.
3. Hand off to `playbooks/ats-direct.md` for Greenhouse / Lever / Ashby / Workable / Darwinbox / generic careers.

## Apply

Follow the destination ATS playbook. Confirmation must come from the **company site**, not Naukri's "application sent" toast.

## Hard rules

- Never Naukri Apply Now.
- Never invent CTC / notice / sponsorship.
- One blocked job on a board does **not** skip the rest of Naukri — log that job and continue to the next company-site listing.
- Daily cap: `settings.json → platforms.naukri.daily_cap`.

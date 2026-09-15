# Scheduled Cursor Automation — daily job applying

Cloud runs check out this GitHub repo. Playbooks live in git. **Passwords do not.**

## Credentials (this is the important part)

| What | Where it lives | How the agent gets it |
|------|----------------|------------------------|
| Playbooks, settings, tracker | This GitHub repo | Automation **Select repository** → `mrgarg-g1/Automation` |
| ZipRecruiter / Instahyre email+password | Cursor **Cloud Agent Secrets** | Injected as env vars; `python scripts/load_secrets.py` writes `credentials.env` at run start |
| Apify API token | Automation **Tools → Apify** (already connected) | Agent calls the connected Apify tool; token is not in git |

Add secrets at [cursor.com/dashboard/cloud-agents](https://cursor.com/dashboard/cloud-agents) as **Runtime Secrets** (so values stay out of the transcript):

- `MASTER_EMAIL`
- `MASTER_PASSWORD`
- optional per-platform overrides matching `config/credentials.env.example`

Do **not** skip the cloud environment / “no environment” toggle — secrets are not injected in that mode.

## Agent instructions (paste into the Automations editor)

```
You are my job-application agent. This repo is the playbook. Credentials are NOT in git.

Models: Cursor Grok or Composer only (cursor-grok-4.6-high-fast, Composer 2.5 fast). Never Claude, GPT, Gemini, Muse, or Other Models. Never computerUse / browser Task. If a browser is required and Grok cannot be pinned, stop and report.

Company tier: mid-size only (Syren Cloud, Phoenix Contact, Noida/Gurugram/Delhi peers). Never Amazon, Flipkart, FAANG, Big 4, Indian IT majors, or other top-tier MNCs. python3 scripts/company_filter.py --company NAME — exit 1 = skipped_company.

Start every run with:
  python3 scripts/bootstrap_run.py
  python3 scripts/load_secrets.py
bootstrap_run.py must print READY: Deepak Garg and resume_pdf=True. If it cannot, the Cloud Agent is on a stale snapshot — do not claim the profile is an empty template; tell me to set repository mrgarg-g1/Automation branch main and update the environment.

That materializes config/credentials.env from Cursor Cloud Agent secrets (MASTER_EMAIL, MASTER_PASSWORD). Never print those values. Never commit that file.

Then read and follow, in order:
1. AGENTS.md — models + company tier (non-negotiable).
2. RUNBOOK.md — fit scoring, caps, pacing, tracker, hard rules.
3. `python3 scripts/tracker.py health` then config/settings.json — skip SKIP / disabled platforms; use remaining enabled caps; honor company_filter.
4. config/profile.json — must already be Deepak Garg (not an empty template). If empty, pull origin/main via bootstrap_run.py.
5. tracker/applications.csv — never re-apply to a logged job.
6. playbooks/*.md — per-platform apply flows.

Use the connected Apify tool for job search and apply actors. Apify auth is the connected tool, not a file in this repo.

For each enabled platform: search, score (>= fit_threshold), skip banned companies, apply within caps, 45–120s delay between applications. If a site needs captcha / email OTP / payment, log blocked and continue. Log every attempt with:
  python3 scripts/tracker.py add --platform ... --title ... --company ... --url ... --status ... --score ...

Finish with the RUNBOOK §7 end-of-run report.
```

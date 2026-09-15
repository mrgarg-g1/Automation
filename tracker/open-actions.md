# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## CAPTCHA — ACTION NEEDED NOW (do not solve; keep highlighting)

User 2026-09-15: **do not stop the run on captcha.** Fill the form, leave the tab, keep applying. User will clear the whole captcha queue in one pass later.

Chrome was restarted earlier this run (`/tmp/chrome-job-apply`). Captcha tabs from before that restart are gone; re-open if still batching. **Currently open:** FourKites GH 8146530; Weekday Gurugram/Noida/Delhi (Submitting…). Instahyre login tabs still up.

| Job | Company | URL | What |
|---|---|---|---|
| Data Scientist | Weekday AI | https://jobs.workable.com/view/6dEwyfYzzMgJmDeXJpXaeQ/data-scientist-in-gurugram-at-weekday-ai | **tab open** — 8 LPA / 15 days / +91 / resume filled; Turnstile Submitting… |
| Data Scientist | Weekday AI | https://jobs.workable.com/view/dmgXbVFH59reFLC9vp8RCw/data-scientist-in-noida-at-weekday-ai | **tab open** — same CTC fill; Turnstile Submitting… |
| Data Scientist | Weekday AI | https://jobs.workable.com/view/1VoLPYmXTksaatQQdXbh7q/data-scientist-in-delhi-at-weekday-ai | **tab open** — same CTC fill; Turnstile Submitting… |
| Senior Data Scientist | FourKites | https://job-boards.greenhouse.io/fourkites/jobs/8146530 | **tab open** — CTC/notice/ML answers + resume; recaptcha + phone aria-invalid |
| AI & NLP Research Solutions Engineer | Acclaro | https://jobs.workable.com/view/uvQwufp3HmJyxRppCwvwwG/hybrid-ai-%26-nlp-research-solutions-engineer-in-noida-at-acclaro | Workable Turnstile (form filled earlier; tab may need re-open) |
| Research Data Scientist | Innodata Inc. | https://job-boards.greenhouse.io/innodatainc/jobs/4404732009 | Greenhouse recaptcha (re-open after Chrome restart) |
| Data Scientist | WorldQuant | https://job-boards.greenhouse.io/worldquant/jobs/4703128006 | Greenhouse recaptcha (re-open) |
| AI Software Engineer (Python) | Zimperium | https://jobs.lever.co/zimperium/5b35759a-d445-4fcb-b255-d719330af055/apply | Lever hCaptcha (re-open) |
| MLE IV Computer Vision | Jumio | https://job-boards.greenhouse.io/jumio/jobs/4713139005 | Greenhouse recaptcha; phone still flagged too long |
| Senior MLE - NLP (Noida) | Level AI | https://jobs.lever.co/levelai/cc04ab77-6ee3-4078-9cfd-110cda0b1438/apply | Lever location autocomplete empty from this VM + hCaptcha |
| Sr. MLE (Speech) - Noida | Level AI | https://jobs.lever.co/levelai/78ddcdbd-4bd8-4187-b7d0-38fcb39c8232/apply | same + hCaptcha |
| AI/ML Developer (India remote, 2–4 YOE) | Jobgether | https://jobs.lever.co/jobgether/e3f4d59d-0456-406b-ac35-a5e7b12a7d6f/apply | pick Hyderabad in location + hCaptcha |
| Data Scientist | ConveGenius | https://convegenius.keka.com/careers/applyjob/149252 | Keka image captcha; CTC now in profile (8 LPA / 15 LPA / 15 days) |

Two95 Gurugram GenAI/AI-ML is **applied**. i2e company-site DS is **applied** (`Application submitted successfully!`). Do not re-apply those.

## Screening answers (filled 2026-09-15 — do not ask the user again)

`config/profile.json`:

- `notice_period`: 15 days
- `current_ctc`: 8 LPA INR (`current_ctc_inr` 800000)
- `expected_salary`: 15 LPA INR (`expected_salary_inr` 1500000, `expected_salary_usd_month` 1800)
- `requires_sponsorship`: No = **India work auth only**, not US work auth. Still skip PathAI US sponsorship questions.

Source: logged-in Instahyre profile (Rs. 8 LPA, start 15 days after offer).

## CTC forms still to submit (answers are in profile now)

Fill from profile, then leave captcha tabs:

| Job | Company | URL |
|---|---|---|
| AI Engineer | NK Securities Research | https://job-boards.eu.greenhouse.io/nksecuritiesresearch/jobs/4811652101 |
| AI/ML Researcher | NK Securities Research | https://job-boards.eu.greenhouse.io/nksecuritiesresearch/jobs/4914411101 |
| Data Scientist | Insurity India | https://job-boards.greenhouse.io/insurityindia/jobs/4300524009 |
| Senior AI-Native Engineer | Payoneer | https://job-boards.greenhouse.io/payoneer/jobs/7431102 |
| Data Scientist | ConveGenius | https://convegenius.keka.com/careers/applyjob/149252 |
| Senior AI Engineer | FourKites | https://job-boards.greenhouse.io/fourkites/jobs/7981512 |
| Senior AI Engineer | Nacre Capital | https://jobs.workable.com/view/tqLo3KJY51BMJrg8fQd5x6/remote-senior-ai-engineer-in-india-at-nacre-capital |
| AI Engineer / AI Automation Specialist | Pavago | https://jobs.workable.com/view/6pTQSCLxyxucQPNBbqaGd5/remote-ai-engineer-%2F-ai-automation-specialist-in-india-at-pavago |
| AI Engineer - Agentic AI & Automation | LUXASIA | https://jobs.workable.com/view/wgKoBPh9bL82yV8MWVSLMF/hybrid-ai-engineer---agentic-ai-%26-automation-in-delhi-at-luxasia |
| Senior Data Scientist - Credit Risk | Funding Societies | https://jobs.workable.com/view/6LZNYpDuPXAuqsS5naTWkP/hybrid-senior-data-scientist---credit-risk-in-delhi-at-funding-societies-%7C-modalku-group |

NK Securities also asks JEE/Codeforces — **do not invent**. PathAI US work-auth: skip.

## Instahyre (logged in this run)

Password recovered via Gmail reset; `INSTAHYRE_*` is in local gitignored `config/credentials.env` (same as master). Profile: current role **Data Science / Machine Learning**; NCR + WFH + anywhere India/outside; 8 LPA; 15-day notice.

**Applied today (Application sent 2026-09-15):** M3AI DS, Bloom AI Senior AI, Shuru Sr Agentic AI, Zero to 1 AI Engineer, SquadStack.ai AI Product Engineer, Avaz AI/ML.

**Already sent 2026-09-09 (logged today so we do not retry):** Azisly, CIMET.

Instahyre daily_cap 8 is full for tracker-today. Next run can 1-click remaining: ConveGenius `job-435105`, VerbaFlo `job-439863`, Apeiro `job-436361`, i2e Instahyre `job-413191` (company-site already applied), Winmore `job-409751`. Skip VMock Instahyre (company-site applied). Skip Infosys/Accenture.

Skip already-applied Instahyre: SYDIAI, DataNimbus, Commotion, Telomere, FourKites, Nablon, Kahuna, Zynix, M3AI, Bloom, Shuru, Zero to 1, SquadStack, Avaz, Azisly, CIMET.

## Company policy

- Never apply to **Syren Cloud**.
- Skip a company after **5 `applied` rows**.
- Naukri = company-site / ATS only. Never Naukri Apply Now.
- Shortlist: `config/company_shortlist.json`. `python3 scripts/company_filter.py --company NAME`

## Models

Cursor Grok / Composer only. Never Claude, GPT, Gemini, Muse, or `computerUse`. Chrome CDP on `DISPLAY=:1`. Do not kill Chrome.

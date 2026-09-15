# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## CAPTCHA — ACTION NEEDED NOW (do not solve; keep highlighting)

User 2026-09-10: skip Jobgether/Binance Lever picture captchas and keep applying elsewhere. Workable Turnstile tabs should not be piled.

| Job | Company | URL | What |
|---|---|---|---|
| AI/ML Engineer | EUROPEAN DYNAMICS | https://jobs.workable.com/view/idz8Yi9JAb3NehqKnjPkgW/remote-ai%2Fml-engineer-in-athens-at-european-dynamics | Cloudflare Turnstile |
| AI Engineer | Youssef L | https://jobs.workable.com/view/oWbDXQHaTCsniQ9JzCGake/remote-ai-engineer-in-casablanca-settat-at-youssef-l | Turnstile / submit hang |
| AI Engineer | Portless | https://jobs.workable.com/view/boRuEDWWy88rZ2DjiiwZy1/remote-ai-engineer-in-united-states-at-portless | Turnstile / submit hang |

## Company tier (user 2026-09-15)

Mid-size only: Syren Cloud, Phoenix Contact, Noida/Gurugram/Delhi peers. Fully remote worldwide still allowed. Skip Amazon, Flipkart, FAANG, Big 4, Indian IT majors. `python3 scripts/company_filter.py --company NAME`.

## Unanswered screening (do not invent)

Set `profile.screening_answers.expected_salary`, `notice_period`. Until then skip CTC/notice forms:

| Job | Company | URL |
|---|---|---|
| AI Engineer | NK Securities Research | https://job-boards.eu.greenhouse.io/nksecuritiesresearch/jobs/4811652101 |
| AI/ML Researcher | NK Securities Research | https://job-boards.eu.greenhouse.io/nksecuritiesresearch/jobs/4914411101 |
| Data Scientist | Insurity India | https://job-boards.greenhouse.io/insurityindia/jobs/4300524009 |

## Next Instahyre (login failing)

Stored Instahyre password is still rejected. Update `INSTAHYRE_PASSWORD` in Cloud Agent secrets. Queued mid-size NCR/remote fits after login works:

| Job | Company | URL |
|---|---|---|
| Data Scientist | M3AI | https://www.instahyre.com/job-440216-data-scientist-at-m3ai-delhi-gurgaon-noida/ |
| AI / ML Engineer | Azisly | https://www.instahyre.com/job-442377-ai-ml-engineer-at-azisly-gurgaon/ |
| Machine Learning Engineer | ConveGenius | https://www.instahyre.com/job-435105-machine-learning-engineer-at-convegenius-noida/ |
| Senior AI Engineer | Bloom AI | https://www.instahyre.com/job-442873-senior-ai-engineer-at-bloom-ai-delhi/ |
| Senior AI Engineer | VerbaFlo | https://www.instahyre.com/job-439863-senior-ai-engineer-at-verbaflo-gurgaon/ |
| Sr. Agentic AI Engineer | Shuru Technologies | https://www.instahyre.com/job-440265-sr-agentic-ai-engineer-at-shuru-technologies-mumbai-work-from-home/ |
| AI Engineer | Zero to 1 | https://www.instahyre.com/job-390614-ai-engineer-at-zero-to-1-work-from-home/ |
| AI Product Engineer | SquadStack.ai | https://www.instahyre.com/job-441903-ai-product-engineer-at-squadstack-noida/ |
| AI / ML Engineer | Avaz | https://www.instahyre.com/job-439263-ai-ml-engineer-at-avaz-chennai-work-from-home/ |
| Senior ML Engineer | Proximity Labs | https://www.instahyre.com/job-416875-senior-ml-engineer-at-proximity-labs-work-from-home/ |

Dropped (top-tier): Infosys Gurgaon/Noida Data Engineer, Accenture LLM/ML/AI roles, Adobe Noida MLE.

Skip already-applied Instahyre: SYDIAI, DataNimbus, Commotion, Telomere, FourKites, Nablon, Kahuna, Zynix.

## Greenhouse HTTP

Most boards return **400 recaptcha enterprise** (Innodata Research DS `4404732009` this run). OTP boards (Coinbase / NewRocket / EnCharge) are either already applied, company-filter banned, or not DS/ML. Phoenix Contact US board still has no India DS/ML (Pennsylvania intern only).

## Models

Cursor Grok / Composer only. Never Claude, GPT, Gemini, Muse, or `computerUse`.

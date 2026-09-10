# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## Skip (user 2026-09-10)

- **Naukri and LinkedIn** — already applied; do not apply there (also skip Hirist leftovers).
- **Jobgether Lever MLE** `d5ccb68f` and **Binance Lever Finance AI DS** `3c553d93` — user said skip the open captchas. Logged `blocked` / `captcha_skipped_by_user`. Do not wait on those tabs. Prefer Greenhouse HTTP (no picture captcha).
- **ZipRecruiter** — `enabled: false`. 14/14 attempts failed (100% > 80% skip rule). Email OTP + computerUse banned. Do not search, login, or apply.
- **protocol_jobs** — `enabled: false`. 7/7 attempts failed (100% > 80% skip rule). Lever captcha / empty boards. Do not search or apply.

Run `python3 scripts/tracker.py health` every run. SKIP platforms get no search and no apply.

## Email OTP — next run: fill from Gmail read tool (`playbooks/gmail-otp.md`)

No open email-OTP items. ZipRecruiter login OTP is skipped with the platform (see Skip above). Greenhouse OTP boards still use Gmail during HTTP apply.

## Unanswered screening (do not guess)

Set `profile.screening_answers.requires_sponsorship` (Yes/No). Until then skip **US/EU** jobs that ask visa sponsorship, including:

| Job | Company | URL |
|---|---|---|
| Machine Learning Engineer | Twilio | https://job-boards.greenhouse.io/twilio/jobs/7702644 |
| Machine Learning Engineer II | PathAI | https://job-boards.greenhouse.io/pathai/jobs/8696752002 |

India-located roles: answer from `work_authorization` = authorized in India.

## Next Instahyre (cap currently 8/8 — apply after reset)

| Job | Company | URL | YOE / loc |
|---|---|---|---|
| AL / ML Engineer | DISCO | https://www.instahyre.com/job-423265-al-ml-engineer-at-disco-work-from-home/ | 4-8 WFH |
| AI Engineer (Backend) | Tekion | https://www.instahyre.com/job-441127-ai-engineer-backend-at-tekion-work-from-home/ | 5-9 WFH Agentic/LLM |
| AI / ML Engineer | Azisly | https://www.instahyre.com/job-442377-ai-ml-engineer-at-azisly-gurgaon/ | 4-8 Gurgaon |
| Senior Data Scientist | Eucloid Data Solutions | https://www.instahyre.com/job-442185-senior-data-scientist-at-eucloid-data-solutions-chennai-gurgaon/ | 3-5 Gurgaon (+Chennai) |
| AI Product Engineer | DISCO | https://www.instahyre.com/job-421516-ai-product-engineer-at-disco-work-from-home/ | 3-7 WFH |

Skip already-applied Instahyre: SYDIAI, DataNimbus, Commotion, Telomere, FourKites, Nablon, Kahuna, Zynix.

## Next ATS (Greenhouse HTTP — no Lever captcha)

Greenhouse embed POST returns **428 + Gmail security code** only on a small set of boards (Coinbase, NewRocket/`highmetric`, EnCharge `enchargeai36`, Gusto, PlanetScale, Neuralink, Akoya). ~95% of other Greenhouse boards return **400** (reCAPTCHA enterprise) — skip those; do not solve captchas.

Live leftover on OTP boards that still fail fit/visa/location: Coinbase Senior MLE India `7739592` (Senior vs 4 YOE); highmetric ServiceNow AI Engineer `6177423004` (no ServiceNow skill); highmetric US/UK/NL Anthropic FDE roles (visa or Senior/Lead); EnCharge AI Compiler Engineer India `4008053009` (compiler/MLIR, not DS/ML). GitLab AI Engineer `8556658002` still recaptcha. BJAK Ashby Applied AI Engineer India `416c3505-bc04-4b6e-8c60-fae0ea8b947e` is a next HTTP target if an Ashby apply path is found. Instahyre remains 8/8 until reset.

## Cleared this run

- NewRocket AI/ML Developer `6148059004` — applied.
- NewRocket Senior AI/ML FDE `6161076004` — already applied.
- Databricks AI Engineer FDE `8099751002` — already applied.
- Moniepoint DS Fraud `4921127101` — already applied.
- Coinbase Machine Learning Engineer `7985187` Remote India — applied (confirmation email).
- Jobgether MLE + Binance Finance AI DS — skipped by user (captcha).
- EnCharge AI Research Engineer, AI Models `4252539009` India remote-friendly — applied (Greenhouse HTTP 200 + Gmail OTP).

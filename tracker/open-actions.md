# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## Skip (user 2026-09-10)

- **Naukri and LinkedIn** — already applied; do not apply there (also skip Hirist leftovers).
- **Jobgether Lever MLE** `d5ccb68f` and **Binance Lever Finance AI DS** `3c553d93` — user said skip the open captchas. Logged `blocked` / `captcha_skipped_by_user`. Do not wait on those tabs. Prefer Greenhouse HTTP (no picture captcha).
- **ZipRecruiter** — `enabled: false`. 14/14 attempts failed (100% > 80% skip rule). Email OTP + computerUse banned. Do not search, login, or apply.
- **protocol_jobs** — `enabled: false`. 7/7 attempts failed (100% > 80% skip rule). Lever captcha / empty boards. Do not search or apply.

- **Ashby** — `enabled: false`. 5/5 attempts failed (100% > 80% skip). BJAK/Tolken/AHL/Sarvam submissions from this VM were flagged as spam. Do not retry from this environment.

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

## Next Instahyre (site login currently failing)

Stored Instahyre password is rejected (`Password you entered is incorrect`). 8/8 already applied today on this account earlier. Queued jobs below stay for after login works:

| Job | Company | URL | YOE / loc |
|---|---|---|---|
| AL / ML Engineer | DISCO | https://www.instahyre.com/job-423265-al-ml-engineer-at-disco-work-from-home/ | 4-8 WFH |
| AI Engineer (Backend) | Tekion | https://www.instahyre.com/job-441127-ai-engineer-backend-at-tekion-work-from-home/ | 5-9 WFH Agentic/LLM |
| AI / ML Engineer | Azisly | https://www.instahyre.com/job-442377-ai-ml-engineer-at-azisly-gurgaon/ | 4-8 Gurgaon |
| Senior Data Scientist | Eucloid Data Solutions | https://www.instahyre.com/job-442185-senior-data-scientist-at-eucloid-data-solutions-chennai-gurgaon/ | 3-5 Gurgaon (+Chennai) |
| AI Product Engineer | DISCO | https://www.instahyre.com/job-421516-ai-product-engineer-at-disco-work-from-home/ | 3-7 WFH |
| Senior ML Engineer | Amazon | https://www.instahyre.com/job-420139/ | 3-7 NCR |
| Data Scientist | Arintra | https://www.instahyre.com/job-436220/ | 4-8 Noida |
| AI Engineer | IDFC FIRST Bank | https://www.instahyre.com/job-398232/ | 3-7 Gurgaon |
| Computer Vision Engineer | Goldcast | https://www.instahyre.com/job-435862/ | 1-5 Noida |

Skip already-applied Instahyre: SYDIAI, DataNimbus, Commotion, Telomere, FourKites, Nablon, Kahuna, Zynix.

## Next ATS (Greenhouse HTTP — no Lever captcha)

Greenhouse embed POST returns **428 + Gmail security code** only on a small set of boards (Coinbase, NewRocket/`highmetric`, EnCharge `enchargeai36`, Gusto, PlanetScale, Neuralink, Akoya). ~95% of other Greenhouse boards return **400** (reCAPTCHA enterprise) — skip those; do not solve captchas.

Live leftover on OTP boards that still fail fit/visa/location: Coinbase Senior MLE India `7739592` (Senior vs 4 YOE); highmetric ServiceNow AI Engineer `6177423004` (no ServiceNow skill); highmetric US/UK/NL Anthropic FDE roles (visa or Senior/Lead); EnCharge AI Compiler Engineer India `4008053009` (compiler/MLIR, not DS/ML). GitLab AI Engineer `8556658002` still recaptcha. Do not retry Ashby from this VM.

Workable (new, 2026-09-10): **applied** RealAdvisor Data Scientist (remote, HTTP 201 in live Chrome). Many India listings ask CTC/notice (Funding Societies Delhi hybrid, Innovaccer Noida, Irth MLOps India) — unanswered, skip until `profile.screening_answers` has those. Cutshort job list is login-walled.

User 2026-09-10: **no screenshots / no videos**. Watch the Cloud Agent live desktop (Chrome on DISPLAY=:1). Do not attach ss.

## Cleared this run

- NewRocket AI/ML Developer `6148059004` — applied.
- NewRocket Senior AI/ML FDE `6161076004` — already applied.
- Databricks AI Engineer FDE `8099751002` — already applied.
- Moniepoint DS Fraud `4921127101` — already applied.
- Coinbase Machine Learning Engineer `7985187` Remote India — applied (confirmation email).
- Jobgether MLE + Binance Finance AI DS — skipped by user (captcha).
- EnCharge AI Research Engineer, AI Models `4252539009` India remote-friendly — applied (Greenhouse HTTP 200 + Gmail OTP).

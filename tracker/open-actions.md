# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## Captcha — ACTION NEEDED NOW (do not solve; forms are already filled)

User will solve captcha only — not job forms. Chrome is on `DISPLAY=:1` with both Lever applies filled + resume attached.

| Job | Company | URL | What |
|---|---|---|---|
| Machine Learning Engineer | Jobgether | https://jobs.lever.co/jobgether/d5ccb68f-a15c-43d7-a381-05cfced69df3/apply | hCaptcha picture puzzle; name/email/phone/location/company + Resume.pdf filled |
| Finance AI Data Scientist | Binance | https://jobs.lever.co/binance/3c553d93-1746-4e78-b6eb-b82bff5cc801/apply | hCaptcha picture puzzle; form + LinkedIn URL + Resume.pdf filled |

After captcha: expect Lever confirmation page, then `tracker.py add --status applied`.

## Skip (user 2026-09-10): Naukri and LinkedIn

Do **not** apply on Naukri or LinkedIn — user already applied there. Same for Hirist/Naukri easy-apply tabs left over from discovery. Use Greenhouse / Lever / Ashby / Instahyre / other ATS instead.

## Email OTP — next run: fill from Gmail read tool (`playbooks/gmail-otp.md`)

| Job | Company | URL | What |
|---|---|---|---|
| account login | ZipRecruiter | https://www.ziprecruiter.com/login | 6-digit email OTP; computerUse banned so login cannot be completed in this agent |

## Unanswered screening (do not guess)

Set `profile.screening_answers.requires_sponsorship` (Yes/No). Until then skip **US/EU** jobs that ask visa sponsorship, including:

| Job | Company | URL |
|---|---|---|
| Machine Learning Engineer | Twilio | https://job-boards.greenhouse.io/twilio/jobs/7702644 |
| Machine Learning Engineer II | PathAI | https://job-boards.greenhouse.io/pathai/jobs/8696752002 |

India-located roles (e.g. Coinbase Remote India): answer from `work_authorization` = authorized in India; do not treat as the empty US-sponsorship field.

## Next Instahyre (cap currently 8/8 — apply after reset)

| Job | Company | URL | YOE / loc |
|---|---|---|---|
| AL / ML Engineer | DISCO | https://www.instahyre.com/job-423265-al-ml-engineer-at-disco-work-from-home/ | 4-8 WFH |
| AI Engineer (Backend) | Tekion | https://www.instahyre.com/job-441127-ai-engineer-backend-at-tekion-work-from-home/ | 5-9 WFH Agentic/LLM |
| AI / ML Engineer | Azisly | https://www.instahyre.com/job-442377-ai-ml-engineer-at-azisly-gurgaon/ | 4-8 Gurgaon |
| Senior Data Scientist | Eucloid Data Solutions | https://www.instahyre.com/job-442185-senior-data-scientist-at-eucloid-data-solutions-chennai-gurgaon/ | 3-5 Gurgaon (+Chennai) |
| AI Product Engineer | DISCO | https://www.instahyre.com/job-421516-ai-product-engineer-at-disco-work-from-home/ | 3-7 WFH |

Skip already-applied Instahyre: SYDIAI, DataNimbus, Commotion, Telomere, FourKites, Nablon, Kahuna, Zynix.

## Cleared this run

- NewRocket AI/ML Developer `6148059004` — applied (Greenhouse confirmation page; otp_from_gmail).
- NewRocket Senior AI/ML FDE `6161076004` — already applied (thank-you email 2026-09-09).
- Databricks AI Engineer FDE `8099751002` — already applied (thank-you email 2026-09-10).
- Moniepoint DS Fraud `4921127101` — already applied (thank-you email).
- Coinbase Machine Learning Engineer `7985187` Remote India — applied 2026-09-10 (Greenhouse HTTP + otp_from_gmail; confirmation email).

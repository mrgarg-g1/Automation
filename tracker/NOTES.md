# Durable run notes (not secrets)

Location: fully remote worldwide OK. Hybrid/onsite only Gurugram / Noida / Delhi.

Company tier: mid-size only (Phoenix Contact, NCR peers, India-remote). Never Syren Cloud (current employer). Skip a company after 5 applied rows. Skip Amazon, Flipkart, FAANG, Big 4, Indian IT majors. Naukri = company-site only, never Apply Now. `python3 scripts/company_filter.py --company NAME`.

2026-09-15 follow-up: 62-company shortlist in `config/company_shortlist.json`. Keka (ConveGenius Noida DS) and Lever (Level AI Noida ML) are live company-site applies that need CTC/notice and/or captcha — do not skip the rest of those ATS boards. Instahyre login 403 from this VM. Apify balance too low for Naukri scraper.

2026-09-15 apply: Greenhouse S3 resume presign + JSON POST to `boards.greenhouse.io/embed/{board}/jobs/{id}` with empty `g-recaptcha-enterprise-token` returns 428 JSON. OTP only when body includes `security_code_recipient` (NewRocket/EnCharge path). Jumio + Moniepoint Credit are recaptcha-only. Workable apply POST 412 Turnstile. Applied today still 0 until Instahyre password, CTC/notice, or a new OTP-board India DS role.

Models: Cursor Grok / Composer only. Never `computerUse` (it billed Claude Sonnet 4.5 on 2026-09-10 even with `inherit`). Never Claude / GPT / Gemini / Muse.

Apify scrapers that worked 2026-09-10: `crawlerbros/ziprecruiter-scraper-pro` (1-click URLs), `getascraper/instahyre-jobs-scraper`, `unfenced-group/remote-co-scraper` (details still login-walled), `getascraper/web3career-jobs-scraper`. Remote.co keyword search via web-fetch ignored the query. `web3.career/data-jobs` 404 — use `data-science-jobs`. Protocol Labs `directory.plnetwork.io/jobs` is empty.

Stale listings: OpenZeppelin Greenhouse `7826440003` is Technical Sales Lead, not AI Ops. Zscaler Agentic AI MLE `5142576007` is hybrid Bangalore (skip). MoonPay Staff MLE is London hybrid.

Instahyre next queue after cap reset: DISCO, Timepay.ai, Meraki Labs (Jumio skipped — seniority).

# Open actions (next run must keep highlighting these)

Clear a row only after the user confirms they completed it **or** a later run submits successfully and logs `applied`.

## CAPTCHA — ACTION NEEDED NOW

**Mrsool Data Scientist II** — no confirmation email. Tab still open. If the checkbox is visible, click it.

| Job | Company | URL |
|---|---|---|
| Data Scientist II | Mrsool | https://jobs.workable.com/view/mRbyeQVTnqBXQ9chnKP9te/remote-data-scientist-ii-in-india-at-mrsool |

Gmail confirmed the rest of the captcha batch (ProcDNA, Funding Societies, Nacre ×2, Weekday Agentic AI, Blue Machines, D2B, Acclaro). Those tabs were closed.

## Daily cap

**32/30 applied today** (captcha backlog counted after Gmail confirm). No more new applies until tomorrow.

## Apify quota / alternative

Still `Monthly usage hard limit exceeded`. Do **not** paste a token in chat.

**Easiest:** raise the monthly spend cap in [Apify Console billing](https://console.apify.com/billing) (same connected account).

**Or connect one MCP** on this automation (Tools →, same place as Apify/Gmail):

1. **Firecrawl** — fetch listing pages (closest to `apify/web-fetch`)
2. **Bright Data** — residential scrape for Naukri / ZipRecruiter / Remote.co
3. **Browserbase** — hosted browser for Cloudflare/Akamai listing pages

Until then, discovery uses Greenhouse public API + Chrome + WebSearch (`playbooks/discovery.md`). ZipRecruiter search results did load in Chrome this pass; 1-click still needs login/OTP. Daily cap is full today.

## Screening (do not ask again)

`profile.json`: notice 15 days; current 8 LPA INR; expected 15 LPA INR / USD 1800 per month; `requires_sponsorship` No = **India work auth only**. Skip PathAI US. Skip NK Securities until JEE/Codeforces answers exist.

## Instahyre

Logged in. Daily tracker cap 8 is full today.

## Company policy

Never Syren Cloud. Skip after 5 `applied` rows (FourKites 3, Weekday AI 4 including Agentic). Naukri = company-site only. Chrome CDP `DISPLAY=:1` — do not kill Chrome.

## Models

Cursor Grok / Composer only. Never Claude, GPT, Gemini, Muse, or `computerUse`.

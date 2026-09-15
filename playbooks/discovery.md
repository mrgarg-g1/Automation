# Playbook — Job discovery without Apify

Apify is the default search tool (`Tools → Apify`). If it returns **monthly usage hard limit exceeded**, do **not** freeze the run. Use this fallback. Never ask the user to paste an API token in chat.

## Already available (no new access)

| Source | What it covers | How |
|---|---|---|
| Greenhouse public API | Company ATS boards | `GET https://boards-api.greenhouse.io/v1/boards/{board}/jobs` then `.../jobs/{id}?questions=true` |
| Chrome CDP (`DISPLAY=:1`) | Instahyre, ZipRecruiter (when Cloudflare passes), Workable, company sites | Open search URLs from each platform playbook |
| Cursor WebSearch | Recent Greenhouse/Lever/JazzHR/Keka URLs | Query `site:job-boards.greenhouse.io` + role + India/Remote |
| Lever / Ashby URLs | Direct apply pages | Open in Chrome; Ashby from this VM is often spam-flagged — one try, then skip |

This is enough for **ats_direct** (the path that actually submitted today: WPP, Dscout, Orcrist, FourKites, Payoneer, Insurity).

## What Apify was uniquely good at

Residential-proxy scrapers for boards that block this datacenter:

- Naukri company-site redirects (`memo23/naukri-scraper`)
- ZipRecruiter 1-click URLs (`crawlerbros/ziprecruiter-scraper-pro`)
- Remote.co listings (`unfenced-group/remote-co-scraper`)

Without that, Naukri/Remote.co/ZR scrape from this VM often hit Cloudflare or Akamai.

## If you want a replacement MCP (connect like Apify)

Connect on the **same automation**: Cursor **Tools →** add the MCP. Do not put the key in git or in chat.

Pick **one**:

1. **Firecrawl** — closest drop-in for `apify/web-fetch` (fetch a URL → markdown). Best first add.
2. **Bright Data** — residential proxy; closest to Apify actors for Naukri / ZipRecruiter / Remote.co.
3. **Browserbase** — hosted Chrome for blocked listing pages (not `computerUse`; not Claude).

Raising the **existing Apify monthly spend cap** in [Apify Console billing](https://console.apify.com/billing) is still cheaper than wiring a second scraper if the account already has actors we know.

## Run order when Apify is dead

1. Greenhouse/Lever boards from `config/company_shortlist.json` + WebSearch.
2. Chrome: Instahyre (until daily 8), ZipRecruiter login + Gmail OTP, Workable India remote/NCR.
3. Naukri: Chrome search only; apply **company ATS only**.
4. If Firecrawl/Bright Data is connected, use it for Naukri redirects and Remote.co before giving up on those boards.

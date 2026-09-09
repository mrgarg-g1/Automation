# Scheduled Cursor Automation — daily job applying (hybrid mode)

**When to create this:** only after a supervised local run has (a) created + verified accounts on the target platforms and (b) completed at least one successful application. Cloud agents cannot do first-time OAuth/captcha/email-verification — those must be done locally first.

## How to create

Ask in the Agents Window: *"Create a Cursor Automation from automations/daily-apply.md"*. The automate skill will walk you through a draft table, then open the Automations editor.

## Draft

| Field | Value |
|-------|-------|
| Name | Daily job application run |
| Description | Searches enabled job platforms, scores listings against my resume, applies to good fits within daily caps, and logs everything to the tracker. |
| Trigger | On a schedule — every day at 09:00 (`cron: 0 9 * * *`; adjust timezone in the editor) |
| Tools | None required beyond default shell/browser-free environment |
| Instructions | See prompt below |

## Prompt (paste into the automation's instructions)

```
You are my job-application agent. This repo contains the full system — read these files first and follow them exactly:

1. RUNBOOK.md — master rules: run modes, fit scoring, pacing, caps, tracker logging, hard rules.
2. config/settings.json — enabled platforms, caps, search roles, fit threshold.
3. config/profile.json — my candidate profile.
4. config/credentials.env — login email/passwords (never echo these anywhere).
5. tracker/applications.csv — history; never re-apply to anything already logged.
6. playbooks/*.md — per-platform application flows.

Then perform a standard daily run in dry-safe order:
- For each enabled platform in settings order, search per its playbook, score jobs per RUNBOOK §4, and apply only to jobs scoring >= the fit threshold, respecting per-platform and total daily caps and the 45–120s randomized pacing delay.
- If a platform demands login interaction you cannot complete non-interactively (captcha, OTP, email verification), mark it blocked in the tracker and continue with the next platform.
- Log every attempt with: python scripts/tracker.py add ...
- Finish with the RUNBOOK §7 end-of-run report as your final message.
```

## Deferred to the editor

- Final schedule/timezone confirmation.
- Cloud compute size (default is fine).
- **Caveat:** credentials.env must be present in the repo/branch the automation checks out, or the run will stop at login. If you'd rather not commit credentials, keep the automation disabled and run locally instead — local runs read the file from your working tree.

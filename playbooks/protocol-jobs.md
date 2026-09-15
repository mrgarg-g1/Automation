# Playbook — Protocol / Web3 boards

**DISABLED** in `config/settings.json` (2026-09-10): 7/7 apply attempts failed (100% > 80% skip rule). Lever captcha / empty Protocol Labs boards. Do not search or apply here until a working HTTP apply path exists and the user re-enables the platform.

Base candidates (verify at runtime; pick the one the user means — default to the first):

- `https://protocol.ai/join/` (Protocol Labs careers — Greenhouse-hosted)
- If the user meant "web3/crypto protocol jobs" generally, treat `https://web3.career` or `https://cryptojobslist.com` as the board.

These are mostly **ATS redirectors**: listings land on Greenhouse/Lever/Ashby. Use `playbooks/ats-direct.md` for the actual application.

## Signup / login

Protocol Labs careers and web3.career need no account to apply. CryptoJobsList offers optional accounts — skip unless the user asks.

## Search

- Protocol Labs: open `https://protocol.ai/join/`, filter departments matching `search.roles` (e.g. Engineering), location "Remote".
- web3.career: `https://web3.career/<role-slug>-jobs` or search box; filter Remote.

## Qualify

Standard RUNBOOK §4 scoring, plus: many web3 roles require smart-contract/Solidity experience — if that's required and not in `profile.skills`, the exclude rule applies automatically via scoring (− and skip).

## Apply

Hand off to `playbooks/ats-direct.md` once on the employer's ATS page. Log with platform=`protocol_jobs` and the final ATS URL.

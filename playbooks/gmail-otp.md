# Playbook — Gmail OTP (read-only)

Gmail is connected on this automation the **same way as Apify**: Cursor **Tools → Gmail** (read). There is no token in git.

## Discover the tool (every run)

MCP namespaces change names. Do **not** hard-code a stale tool id.

1. List dynamic tools (catalog or search `gmail|mail|google`).
2. Pick the namespace that is Gmail / Google Mail and **ready** (not `needsAuth`).
3. Inspect that namespace’s schemas (`GetDynamicTools` with the namespace, then the specific tool).
4. Use **read/search/list message** tools only. Do not send, delete, or forward mail.

If the Gmail namespace is missing or `needsAuth`: log `otp_gmail_miss`, notify immediately, continue other jobs. Tell the user to attach Gmail on the automation (same place as Apify).

## When a site asks for OTP / email verification code

1. Note the sender/site (ZipRecruiter, Instahyre, Greenhouse, NewRocket, Lever, Databricks, etc.).
2. Search the inbox for mail from the last ~10–15 minutes matching that site. Prefer unread.
3. Read the matching message. Extract the code (usually 4–8 digits or an 8-character alphanumeric Greenhouse code).
4. Fill it on the site and continue the application.
5. Tracker notes: `otp_from_gmail` only. **Never** write the code, full email body, or message id into git, tracker, or chat.

## Safety

- Read-only. Do not click unknown links from mail in a way that submits the application from the email itself unless the playbook says so.
- If several codes exist, use the **newest** matching that site.
- If no code arrives in ~2 minutes → `needs_user_action` / `otp_gmail_miss`, keep applying elsewhere.

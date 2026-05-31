# Provider Options

This skill does not assume a sending provider is configured.

## Draft-Only Mode

Use when no email sending tool is available.

Output a send-ready draft with:

- To
- Cc / Bcc
- Subject
- Body
- Attachments
- Notes

## Gmail / Google Workspace

Use only if a Gmail connector, browser session, automation, or API integration is explicitly available.

Do not ask for raw passwords or OAuth tokens.

## SMTP

Use only if SMTP credentials and a safe script/tool are already configured outside the chat.

Do not store credentials in the repo or Jarvis notes.

## Browser Sending

If the user asks to use a logged-in webmail session, use a browser tool only when available and appropriate.

Still require final confirmation before clicking send.

## Automation

If email automation is connected for external recipients, confirm:

- From account
- Recipient list
- Subject
- Body
- Attachments
- Scheduled time, if any

Do not create recurring or delayed email automation unless explicitly requested.

## Self-Email Automation

For owner/self email automation, a per-message confirmation is not required when:

- The user has requested self-email automation.
- The configured provider/tool is available.
- The recipient list contains only allowlisted owner/self addresses.
- Validation passes.

Recommended allowlist examples:

```text
OWNER_EMAIL
SELF_EMAIL_ALLOWLIST
```

Do not infer owner email addresses from random project files. Use explicit configuration or a user-provided self address.

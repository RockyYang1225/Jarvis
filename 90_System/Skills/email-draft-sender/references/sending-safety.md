# Sending Safety

Email is external communication. Treat external sending as a confirmed action. Self-email automation can skip per-message confirmation only under the allowlist rules below.

## Self-Email Automation

Automatic sending is allowed when all conditions are true:

- The sending provider/tool is configured and available.
- Every `To`, `Cc`, and `Bcc` recipient is an allowlisted owner/self email address.
- No external recipient is present.
- The payload has a subject and body.
- Attachments are either absent or explicitly part of the current generated artifact.
- No secret-like text, private keys, tokens, passwords, or unrelated private notes are detected.
- The provider/tool can verify delivery success.

If any condition fails, stop and use explicit confirmation mode.

For self-email automation, report after sending:

- Provider/tool
- Recipient(s)
- Subject
- Sent timestamp or message id, if available
- Any warnings

## Must Confirm Before Sending

Show the final message and ask for explicit confirmation before sending.

Confirmation must include clear intent, such as:

- "确认发送"
- "send it"
- "yes, send"
- "可以发送"

Ambiguous phrases like "looks good" are not enough if recipients or attachments are high-risk.

This confirmation section does not apply to self-email automation when all allowlist conditions pass.

## Stop If

- No recipient is provided.
- Subject is empty.
- Body is empty.
- Attachments are referenced but missing.
- The email contains secrets, tokens, passwords, private keys, or unrelated private notes.
- The user asks to send from an unconfigured account.
- The tool cannot verify success.

## External Recipients

For external recipients, restate:

- To / Cc / Bcc
- Subject
- Attachments
- Any links

Ask for confirmation after showing the final draft.

## Attachments

Do not attach files automatically.

Before attaching, verify:

- File exists.
- File is intended for the recipient.
- File does not contain secrets or private notes.
- User confirmed attachment list.

## After Sending

Only claim success when the provider/tool confirms success.

Report:

- Provider/tool
- Recipient(s)
- Subject
- Sent timestamp or message id, if available
- Any failed recipients

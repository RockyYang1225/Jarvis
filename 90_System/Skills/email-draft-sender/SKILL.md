---
name: email-draft-sender
description: Draft, review, localize, and safely send emails with configured email delivery tools, including automatic self-email mode for allowlisted owner addresses. Use when the user asks to write an email, generate an email draft, send an email, 发送邮件, 发邮件, 自动发邮件给自己, 生成发送邮箱, prepare follow-up mail, send release notes, send acceptance mail, or produce subject/body/recipients/attachments for an email.
---

# Email Draft Sender

Use this skill to draft, review, and safely send email.

## Core Rule

Default mode is draft first. Send only when one of these modes applies:

1. Confirmed send: a real email delivery capability is configured, and the user has reviewed the final message and explicitly confirmed sending.
2. Self-email automation: a real email delivery capability is configured, all recipients are allowlisted owner email addresses, no external Cc/Bcc is present, and the payload passes validation.

If neither condition applies, produce a send-ready draft and explain what manual action remains.

## Quick Start

1. Identify intent:
   - Draft only
   - Review or polish an existing email
   - Translate or localize email
   - Generate a send-ready payload
   - Send email after confirmation
   - Automatically send email to the owner / self address
2. Collect required fields:
   - To
   - Cc / Bcc, if needed
   - Subject
   - Body
   - Attachments, if any
   - Tone and language
3. Read references as needed:
   - For writing style, read [references/email-writing.md](references/email-writing.md).
   - For templates, read [references/templates.md](references/templates.md).
   - For sending safety, read [references/sending-safety.md](references/sending-safety.md).
   - For provider options, read [references/provider-options.md](references/provider-options.md).
4. Validate the payload before sending or handoff:

```bash
rtk python3 <jarvis-root>/90_System/Skills/email-draft-sender/scripts/validate_email_payload.py <payload.json>
```

5. If using self-email automation, validate that all recipients are allowlisted owner addresses.
6. If not self-email automation, show the final email to the user and wait for explicit confirmation such as "确认发送".
7. If sending is configured and the selected mode is allowed, send and verify. Otherwise, leave a draft.

## Required Safety Boundaries

- Do not silently send email to external recipients.
- Automatic self-email is allowed only for configured owner email allowlists.
- Do not invent recipients.
- Do not add attachments without user confirmation.
- Do not send to external recipients unless the user confirms final content and recipients.
- Do not expose secrets, tokens, private notes, or unrelated project context in the email.
- Do not claim an email was sent unless a configured sending tool returned success.
- If no sending tool is available, say that only a draft was prepared.
- If self-email automation conditions fail, fall back to confirmed-send mode.

## Output Format

For drafts:

```text
To:
Cc:
Bcc:
Subject:

Body:
...

Attachments:
- ...

Notes:
- ...
```

For sent mail:

```text
Sent: yes
Provider/tool:
To:
Subject:
Evidence:
```

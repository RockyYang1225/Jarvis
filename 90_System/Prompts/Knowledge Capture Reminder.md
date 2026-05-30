# Knowledge Capture Reminder Prompt

Use this prompt near the end of a project coding session.

```text
Review this project session and decide whether it is worth reminding me about knowledge capture.

Inspect:
- git status
- git diff --stat
- recent changed files
- docs/project-home.md if present
- tasks/active.md and tasks/done.md if present
- decisions/ if present
- knowledge/ if present

Only remind me if the session produced one of:
- meaningful code or docs change
- architecture or product decision
- debugging lesson
- reusable command or workflow
- project status change
- career/portfolio-worthy progress

If it is worth capturing, ask exactly in Chinese:

"本次会话可能产生了值得沉淀的知识，要我准备一份知识沉淀草稿吗？"

If I say yes, draft:
1. repo-local updates
2. Jarvis project retro
3. reusable knowledge candidates
4. project card updates

Do not write long-term Jarvis knowledge without my confirmation.
```

# agency-agents

来源：`https://github.com/msitarzewski/agency-agents`

用途：第三方专业 agent 定义库。Jarvis 中的 `agency-*` skills 会引用这里的原始 agent prompt。

## Jarvis 托管路径

```text
<jarvis-root>/90_System/Tools/External Tools/agency-agents/repo
```

## 已安装 Skill

已安装的 `agency-*` skills 位于 `~/.codex/skills/agency-*`。

旧入口 `~/agency-agents` 已删除，不再作为兼容路径保留。

## 更新

```bash
git -C "<jarvis-root>/90_System/Tools/External Tools/agency-agents/repo" pull --ff-only
```

## 验证

```bash
test -d "<jarvis-root>/90_System/Tools/External Tools/agency-agents/repo/.git"
git -C "<jarvis-root>/90_System/Tools/External Tools/agency-agents/repo" status --short
```

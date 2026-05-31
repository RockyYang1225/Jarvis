# production-readiness

来源：`https://github.com/RockyYang1225/production-readiness`

用途：检查 demo app、API、Web app、全栈项目或通用项目是否具备生产上线准备度。

## Jarvis 托管路径

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo
```

## 主 Skill

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/SKILL.md
```

`~/.agents/skills/production-readiness` 指向上面的 Jarvis skill 目录。

旧入口 `~/.production-readiness/repo` 和 `~/plugins/production-readiness` 已删除，不再作为兼容路径保留。

## 本地检查脚本

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/scripts/inspect_project.py
```

## 更新

```bash
git -C "<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo" pull --ff-only
```

## 验证

```bash
readlink ~/.agents/skills/production-readiness
python3 "<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/scripts/inspect_project.py" /path/to/project
```

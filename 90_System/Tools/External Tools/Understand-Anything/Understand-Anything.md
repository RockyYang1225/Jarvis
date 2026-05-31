# Understand-Anything

来源：`https://github.com/Lum1104/Understand-Anything`

用途：把代码库、知识库或文档分析成可探索、可搜索、可提问的交互式知识图谱。

## Jarvis 托管路径

```text
<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo
```

## Codex 发现入口

```text
~/.agents/skills/understand
~/.agents/skills/understand-chat
~/.agents/skills/understand-dashboard
~/.agents/skills/understand-diff
~/.agents/skills/understand-domain
~/.agents/skills/understand-explain
~/.agents/skills/understand-knowledge
~/.agents/skills/understand-onboard
```

这些入口都应指向：

```text
<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo/understand-anything-plugin/skills/
```

通用插件入口：

```text
~/.understand-anything-plugin
```

应指向：

```text
<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo/understand-anything-plugin
```

## 常用命令

在 Codex / agent 会话里使用：

```text
/understand
/understand --language zh
/understand-dashboard
/understand-chat How does this codebase work?
/understand-diff
/understand-onboard
```

## 更新

由于安装路径改为 Jarvis 托管路径，更新时使用：

```bash
UA_DIR="<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo" \
  bash -c 'curl -fsSL https://raw.githubusercontent.com/Lum1104/Understand-Anything/main/install.sh | UA_DIR="$UA_DIR" bash -s --update'
```

或直接：

```bash
git -C "<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo" pull --ff-only
pnpm -C "<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo" install --frozen-lockfile
pnpm -C "<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo" build
```

## 验证

```bash
test -L ~/.agents/skills/understand
readlink ~/.agents/skills/understand
pnpm -C "<jarvis-root>/90_System/Tools/External Tools/Understand-Anything/repo" build
```

## 备注

曾按官方默认路径安装过一份：

```text
~/.understand-anything/repo
```

旧默认安装路径已删除。实际 Codex skill 和通用插件入口已经切到 Jarvis 托管路径。

# planning-with-files

来源：`https://github.com/OthmanAdi/planning-with-files`

用途：文件型规划工作流项目。

## Jarvis 托管位置

`planning-with-files` 是从 GitHub 下载的外部工具 repo，真实仓库现在托管在 Jarvis：

```text
<jarvis-root>/90_System/Tools/External Tools/planning-with-files/repo
```

旧入口 `~/planning-with-files` 和 `~/Workspace/planning-with-files` 已删除，不再作为兼容路径保留。

## 注意

当前 repo 有本地改动和未跟踪项目文档。不要在整理路径时清理、重置或覆盖这些改动。

## 验证

```bash
test -d "<jarvis-root>/90_System/Tools/External Tools/planning-with-files/repo/.git"
git -C "<jarvis-root>/90_System/Tools/External Tools/planning-with-files/repo" status --short
```

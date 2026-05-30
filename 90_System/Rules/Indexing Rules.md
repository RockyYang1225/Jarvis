# 索引规则

Jarvis 的每一层都必须有清晰入口。

## 基本规则

- 每个顶层区域必须有入口索引。
- 每个二级目录必须有目录内索引，或在 [[../Indexes/Layer Index|层级索引]] 中明确指定入口。
- 新增目录时，不能只创建空文件夹；必须同步创建或指定索引文件。
- 父级索引必须链接到子级索引。
- 重要索引要能从 [[../../00_Home/Dashboard|Dashboard]] 或 [[../Indexes/Jarvis Session Index|Jarvis 会话索引]] 找到。

## 命名习惯

- 目录内索引优先使用目录同名文件。
- 如果已有更自然的入口名，可以在 [[../Indexes/Layer Index|层级索引]] 中指定，例如 Home 使用 `Dashboard.md`。
- 给用户看的索引标题写中文。
- 路径和文件名可以保留英文，保持链接稳定。

## 新增目录检查清单

新增目录后检查：

- 是否有索引文件
- 父级索引是否链接到它
- [[../Indexes/Layer Index|层级索引]] 是否需要更新
- Codex 是否需要从 `AGENTS.md` 读到它
- 是否需要模板、workflow 或 agent registry 支持

## 边界

索引负责导航，不负责承载大量正文。

如果一个索引开始记录大量过程细节，应该拆到：

- 项目卡片
- 复盘
- 知识笔记
- workflow
- template

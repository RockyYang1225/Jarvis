# 知识沉淀提醒流程

## 目的

提醒我判断一次项目会话是否值得沉淀成知识。

自动化只负责提醒；只有我确认后，才准备草稿。不要静默写入长期知识。

## 触发条件

当满足以下任意条件时，可以提醒是否沉淀：

- 代码或文档有实质变化
- 做出了设计或架构决策
- 调试了 bug，且原因可复用
- 发现了新的流程或命令
- 项目范围、状态或下一步发生变化
- 本次会话产生了可写入简历/作品集的进展

以下情况不需要提醒：

- 只是读取文件
- 只是回答问题
- 只有格式调整
- 失败尝试且没有可复用经验

## 固定提醒语

```text
本次会话可能产生了值得沉淀的知识，要我准备一份知识沉淀草稿吗？
```

## 如果我确认

准备一份草稿，包含：

1. 项目变化
2. 已做决策
3. 可复用知识
4. 任务变化
5. 建议写入 repo 的内容
6. 建议写入 Jarvis 的内容

写入跨项目 Jarvis 知识前，再次请求确认。

## 如果我拒绝

不要写知识沉淀文件。

只有在我要求时，才更新项目任务状态。

## 写入目标

Repo 内：

- `docs/project-home.md`
- `tasks/active.md`
- `tasks/done.md`
- `decisions/ADR-xxx.md`
- `knowledge/YYYY-MM-DD-session-notes.md`
- `reviews/project-retros.md`

Jarvis 内：

- `50_Reviews/Project Retros/<project>-YYYY-MM-DD.md`
- `40_Knowledge/Patterns/<topic>.md`
- `90_System/Rules/<rule>.md`
- `10_Workspace/Active Projects/<project>.md`

## 边界

Repo 内更新可以更直接，因为它们仍在项目上下文里。

Jarvis 更新属于长期记忆，需要明确确认。

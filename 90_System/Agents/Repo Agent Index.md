# Repo Agent Index

这个文件索引所有项目 repo 里的本地 agents。

全局 agent 负责跨项目通用能力；repo local agents 负责项目特有规则、领域知识、测试方式、发布方式和验收方式。

## 规则

- 每个 repo 可以有自己的 `agents/` 目录。
- 每个 repo 的 `AGENTS.md` 负责告诉 Codex 本项目有哪些本地 agent。
- Jarvis 通过这个文件维护上层索引。
- 新增 repo local agent 时，同步更新本文件。
- 项目开发验收统一走 [[../Workflows/Project Development Acceptance|项目开发验收]]，repo local agents 只补充项目特有规则。

## Repo Agents

| Project | Repo | Local Agents File | 状态 |
|---|---|---|---|
| 示例项目 | `~/Workspace/example-project` | `~/Workspace/example-project/agents/README.md` | 示例 |

## 本地 Agent 最小集合

每个 repo 默认预留这些本地 agent 槽位：

- Project Developer Agent：项目开发执行规则
- Project Test Agent：项目测试和验证规则
- Project Acceptance Agent：项目内验收规则
- Project Knowledge Agent：项目知识沉淀规则

不是每个项目都必须立即填满细节；但入口先统一。

## 新增本地 Agent 清单模板

```markdown
# <Project> Local Agents

Jarvis Index: `90_System/Agents/Repo Agent Index.md`
Repo:

## Agents

### Project Developer Agent

职责：
输入：
输出：
可用技能：
边界：

### Project Test Agent

职责：
输入：
输出：
测试命令：
边界：

### Project Acceptance Agent

职责：
输入：
输出：
验收标准：
边界：

### Project Knowledge Agent

职责：
输入：
输出：
沉淀目标：
边界：
```

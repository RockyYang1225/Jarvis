# Jarvis Guide

这个文件是 Jarvis 的顶层使用说明。

以后如果在 Jarvis 根目录打开 Codex 会话，先看这里，就能知道每一层做什么、有哪些工具、有哪些 workflow、项目代码应该去哪里。

## 一句话定位

Jarvis 是我的个人工作系统，不是代码仓库本体。

- Jarvis 管思考、索引、知识、复盘、agent、workflow。
- `~/Workspace` 管真实项目代码。

## 每一层做什么

| 层级 | 作用 | 路径 |
|---|---|---|
| Home | 控制台、当前重点、使用说明 | `00_Home/` |
| Workspace | 项目索引和项目卡片 | `10_Workspace/` |
| Career | 简历、面试、作品集素材 | `20_Career/` |
| Ideas | 想法、idea、孵化中的项目 | `30_Ideas/` |
| Knowledge | 稳定、可复用的知识 | `40_Knowledge/` |
| Reviews | 日、周、项目、面试复盘 | `50_Reviews/` |
| System | Jarvis 自身规则、模板、agent、workflow、prompt | `90_System/` |
| Code Repos | 真实代码项目 | `~/Workspace/` |

## 顶层入口

- [[Dashboard|Jarvis 控制台]]
- [[Current Focus|当前重点]]
- [[../90_System/Indexes/Layer Index|层级索引]]
- [[../90_System/Indexes/Jarvis Session Index|Jarvis 会话索引]]
- [[../90_System/System|系统]]
- [[../90_System/Tools/Tools|工具索引]]
- [[../90_System/Agents/Agent Registry|Agent 管理]]
- [[../90_System/Agents/Workflow Registry|Workflow 管理]]
- [[../90_System/Agents/Repo Agent Index|Repo 本地 Agent 索引]]

## 常见任务怎么走

### 我要开发项目

1. 先到 [[../10_Workspace/Projects|项目工作区]] 找项目卡片。
2. 再进入真实 repo：`~/Workspace/<项目名>`。
3. 在 repo 里读 `AGENTS.md`、`agents/README.md`、`docs/project-home.md`。
4. 开发完成后走 [[../90_System/Workflows/Project Development Acceptance|项目开发验收]]。

### 我有一个新想法

1. 先放进 `30_Ideas/Inbox/`。
2. 先走 [[../90_System/Workflows/Classify New Idea|新想法分类]]，判断它是代码、音乐、内容、学习、职业、生活、商业还是 Jarvis 系统想法。
3. 如果准备整理或执行，走 [[../90_System/Workflows/Idea Documentation and Capability Discovery|想法文档化与能力检索]]：先生成对应文档，再盘点现有能力并检索工具。
4. 需要整理时使用 [[../90_System/Templates/Idea Brief|想法简报模板]]。
5. 只有适合持续执行和交付的想法，才走 [[../90_System/Workflows/Idea to Project|想法到项目]]。

### 我要沉淀知识

1. 先生成草稿。
2. 判断是项目内知识、复盘，还是长期知识。
3. 长期知识进入 [[../40_Knowledge/Knowledge|Knowledge]] 前需要确认。

### 我要维护 agent 或 workflow

1. Agent 先登记到 [[../90_System/Agents/Agent Registry|Agent Registry]]。
2. Workflow 先登记到 [[../90_System/Agents/Workflow Registry|Workflow Registry]]。
3. Repo 本地 agent 同步到 [[../90_System/Agents/Repo Agent Index|Repo Agent Index]]。
4. 必要时新增 prompt、模板、自动化脚本。

## 工具怎么查

工具分四类：

- Jarvis 内部工具：agent、workflow、prompt、template。
- Codex / Superpowers 技能：用于开发、计划、调试、验证。
- agency-agent 技能：用于架构、前端、后端、原型、验收、代码审查。
- Repo 本地工具：每个项目自己的 `AGENTS.md`、`agents/README.md`、项目文档和测试命令。

详细索引见 [[../90_System/Tools/Tools|工具索引]]。

## Codex 开会话时的默认读法

如果会话开在 Jarvis 层：

1. 读 `AGENTS.md`。
2. 读本文件。
3. 读 [[../90_System/Indexes/Layer Index|层级索引]]，确认每一层的入口。
4. 根据用户任务选择对应层级。
5. 如果涉及项目代码，进入 `~/Workspace/<repo>` 后再读 repo 入口。
6. 如果产生可复用知识，先问是否准备沉淀草稿。

如果会话开在用户主目录层，也默认按 Jarvis 知识体系会话处理；只有明确要改项目代码时，才进入 `~/Workspace/<repo>`。

## 固定提醒

项目会话结束时，如果产生了决策、调试经验、可复用流程、项目状态变化或作品集素材，使用这句话：

```text
本次会话可能产生了值得沉淀的知识，要我准备一份知识沉淀草稿吗？
```

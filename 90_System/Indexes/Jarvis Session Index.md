# Jarvis 会话索引

这个索引用来帮助在 Jarvis 顶层开启的 Codex 会话快速定位上下文。

## 必读入口

- [[../../00_Home/Jarvis Guide|Jarvis Guide]]
- [[../../00_Home/Dashboard|Jarvis 控制台]]
- [[../System|系统]]
- [[Layer Index|层级索引]]
- [[../Tools/Tools|工具索引]]
- [[../Agents/Agent Registry|Agent Registry]]
- [[../Agents/Workflow Registry|Workflow Registry]]
- [[../Agents/Repo Agent Index|Repo Agent Index]]

## 按任务路由

| 任务 | 先读 | 再读 |
|---|---|---|
| 看当前重点 | [[../../00_Home/Current Focus|当前重点]] | [[../../00_Home/Dashboard|控制台]] |
| 找项目 | [[../../10_Workspace/Projects|项目工作区]] | [[../Agents/Repo Agent Index|Repo Agent Index]] |
| 捕获新想法 | [[../Workflows/Classify New Idea|新想法分类]] | [[../../30_Ideas/Categories/Categories|想法分类]] |
| 想法准备执行 | [[../Workflows/Idea Documentation and Capability Discovery|想法文档化与能力检索]] | [[../Tools/Tools|工具索引]] |
| 修改代码 | 项目卡片 | `~/Workspace/<repo>/AGENTS.md` |
| 创建项目 | [[../Workflows/Idea to Project|想法到项目]] | [[../Templates/Project Charter|项目启动说明模板]] |
| 持续开发验收 | [[../Workflows/Project Development Acceptance|项目开发验收]] | [[../Templates/Acceptance Report|验收报告模板]] |
| 沉淀知识 | [[../Workflows/Knowledge Capture Reminder|知识沉淀提醒]] | [[../../40_Knowledge/Knowledge|Knowledge]] |
| 做复盘 | [[../Workflows/Weekly Review|每周复盘]] | [[../../50_Reviews/Reviews|Reviews]] |
| 维护 agent | [[../Agents/Agent Registry|Agent Registry]] | [[../Prompts/Prompts|Prompts]] |
| 维护 workflow | [[../Agents/Workflow Registry|Workflow Registry]] | [[../Workflows/Workflows|Workflows]] |
| 维护 skill | [[../Skills/Skills|Skills]] | [[../Tools/Tools|工具索引]] |
| 查工具 | [[../Tools/Tools|工具索引]] | 当前 Codex 会话的实际工具列表 |

## 项目入口

- [[../../10_Workspace/Active Projects/Active Projects|活跃项目索引]]

## 重要边界

- Jarvis 只放索引、知识、复盘、系统规则。
- 真实代码在 `~/Workspace`。
- 长期知识写入前需要确认。
- 大版本邮件默认只生成草稿，不自动发送。

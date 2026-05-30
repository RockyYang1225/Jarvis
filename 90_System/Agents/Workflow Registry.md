# Workflow Registry

这个文件维护 Jarvis 里的 workflow 体系。

后续新增 workflow 时，先在这里登记，再决定是否需要：

- 单独 workflow 文档
- agent prompt
- 模板
- repo `AGENTS.md` 规则
- 自动化脚本
- 邮件或提醒机制

## 设计原则

- 如果从 Jarvis 顶层开会话，先读 `AGENTS.md` 和 [[../Indexes/Jarvis Session Index|Jarvis Session Index]]。
- Workflow 描述一条可重复执行的工作路径。
- 每条 workflow 要明确触发条件、参与 agent、输入、输出和人工确认点。
- 小改动可以自动触发验收；长期记忆、版本发布、邮件通知需要明确规则。
- 大版本必须生成版本文档。
- Workflow 负责串联多个 agent，而不是让单个 agent 自己隐式调用其他 agent。
- Workflow 可以同时使用 global agents 和 repo local agents。
- Repo local agents 的上层索引见 [[Repo Agent Index]]。

## 编排层级

```text
Jarvis Workflow
  -> Global Agent
  -> Repo Local Agent
  -> Evidence / Report / Docs
  -> Human confirmation when required
```

## Workflow 必须说明

- 使用哪些 global agents
- 使用哪些 repo local agents
- 每个 agent 的输入和输出
- agent 之间的交接物
- 哪一步需要我确认
- 哪些文档必须生成

## 当前 Workflows

| Workflow | 状态 | 参与 Agent | 触发条件 | 输出 |
|---|---|---|---|---|
| 新想法分类 | 已启用 | Knowledge Capture Reminder 可参与 | 捕获任何新 idea | 生命周期位置、主分类、最小下一步 |
| 想法文档化与能力检索 | 已启用 | Knowledge Capture Reminder、Development Agent、Repo Local Agents、github-capability-finder 可参与 | 用户提出想法、点子或准备实行方案 | 对应想法文档、能力盘点、工具检索建议、执行方案 |
| 想法到项目 | 已启用 | Development Agent 可参与 | 想法准备进入执行 | Project Charter、Project Card、repo KB |
| 每周复盘 | 已启用 | AI Weekly Review | 每周复盘 | Weekly Review 草稿、知识提炼建议 |
| 知识沉淀提醒 | 已启用 | Knowledge Capture Reminder | 项目会话产生可沉淀内容 | 知识沉淀草稿提醒 |
| 项目开发验收 | 已启用：手动触发 | Development Agent、Product Acceptance Agent、Repo Local Agents | 每次小改动或版本完成 | 验收报告、版本文档、邮件草稿 |
| 生产上线准备度评审 | 已启用：手动触发 | Development Agent、Product Acceptance Agent、Repo Local Agents | 项目、demo app、API、Web app 或全栈项目准备上线、发布或部署前 | 上线准备度结论、阻塞项、风险项、验证证据、发布 checklist |

## 想法文档化与能力检索 Workflow

主文档：[[../Workflows/Idea Documentation and Capability Discovery|想法文档化与能力检索]]

### 目标

当用户提出想法、点子或初步方案时，先生成对应文档，再判断是否执行；进入执行前，先查看现有能力，并在有缺口时检索对应工具。

### 参与 Agent

- Knowledge Capture Reminder：提醒是否需要长期沉淀。
- Development Agent：当想法进入项目执行时参与。
- Repo Local Agents：当想法属于已有项目时补充项目规则。
- github-capability-finder：当需要查找 skill、plugin、MCP、CLI、agent、workflow template 或开发工具时参与。

### 输出

- 想法收集条目、想法简报、项目启动说明、研究笔记或系统改进草稿。
- 已有能力盘点。
- 工具检索候选和建议。
- 可执行方案和确认点。

### 人工确认点

- 长期知识写入。
- 修改 Jarvis 长期规则、agent、workflow 或 registry。
- 安装外部工具。
- 创建真实项目 repo。

## 项目开发验收 Workflow

主文档：[[../Workflows/Project Development Acceptance|项目开发验收]]

### 目标

让项目持续开发时，每次小改动都由独立验收 agent 做产品验收和测试验收；当产出大版本时，生成版本文档和邮件草稿，提醒我人工验收。

### 参与 Agent

- Development Agent：负责实现。
- Product Acceptance Agent：负责独立验收。
- Repo Local Agents：补充项目特有开发、测试、验收和知识规则。
- Human Owner：我，负责大版本最终验收。

### Development Agent 可用能力

- superpowers skills，例如 brainstorming、writing-plans、test-driven-development、verification-before-completion
- agency-agent skills，例如 agency-frontend-developer、agency-backend-architect、agency-software-architect、agency-rapid-prototyper
- 当前 repo 的 `AGENTS.md`

### Product Acceptance Agent 读取范围

验收 agent 不读取开发会话全过程，只读取：

- 初始产品方案
- 初始技术方案
- 当前版本文档
- 变更摘要
- 测试证据
- 截图 / 日志 / 命令输出

### 小改动验收

每个小改动完成后，生成验收报告：

```text
结论：通过 / 需要修改 / 阻塞
产品验收：
测试验收：
证据：
缺口：
下一步：
```

### 大版本验收

大版本完成时必须生成版本文档和邮件草稿，并提醒我人工验收。

邮件收件人：

```text
<owner-email@example.com>
```

真实自动发送能力单独接入；在未接入前，不自动发邮件。

### 大版本触发条件

- 一个 milestone 完成
- 新增主要用户流程
- UI/交互有明显变化
- API/数据结构有破坏性变化
- 准备发布/部署
- 多个小改动累计成一个可验收版本

## 新增 Workflow 登记模板

```markdown
## Workflow Name

状态：规划中 | 已启用 | 暂停 | 废弃
参与 Global Agents：
参与 Repo Local Agents：
主文档：
关联 Prompt：
关联模板：

### 目标

### 触发条件

### 输入

### 输出

### Agent 编排顺序

### 人工确认点

### 自动化边界
```

# Agent Registry

这个文件维护 Jarvis 的全局 agent 体系。

后续新增 agent 时，先在这里登记，再决定是否需要单独 prompt、模板、workflow、repo 本地 agent 或自动化脚本。

## 三层模型

顶层会话入口：

- `AGENTS.md`
- [[../../00_Home/Jarvis Guide|Jarvis Guide]]
- [[../Indexes/Jarvis Session Index|Jarvis Session Index]]

### 1. Global Agents

全局 agent 由 Jarvis 管理，适合跨项目复用。

位置：

```text
Jarvis/90_System/Agents/Agent Registry.md
Jarvis/90_System/Prompts/
Jarvis/90_System/Templates/
```

### 2. Workflow Orchestration

Workflow 负责编排多个 agent，决定 agent 的顺序、输入、输出和人工确认点。

位置：

```text
Jarvis/90_System/Agents/Workflow Registry.md
Jarvis/90_System/Workflows/
```

### 3. Repo Local Agents

每个 repo 可以有自己的本地 agent，用于处理该项目特有的开发、测试、发布、验收或知识沉淀规则。

位置：

```text
<repo>/agents/
<repo>/AGENTS.md
```

全局索引见 [[Repo Agent Index]]。

## 设计原则

- Agent 是职责单元，不是随便起的角色名。
- 每个 agent 都要说明输入、输出、触发时机和权限边界。
- 给我看的说明写中文。
- 给 Codex / agent 执行的 prompt 可以保留英文。
- 不要让多个 agent 对同一件事都有最终决定权。
- 长期写入 Jarvis 的内容需要我确认。
- Repo 本地 agent 优先处理项目特有规则；全局 agent 处理跨项目通用规则。
- Workflow 才负责串联 agent；agent 自己不应该偷偷调用一串其他 agent。

## Agent 分类

### 开发类 Agent

负责实现、修复、重构、生成文档、运行测试。

可使用：

- superpowers skills
- agency-agent skills
- repo 内 `AGENTS.md`
- 项目内 `docs/`、`tasks/`、`decisions/`、`knowledge/`

### 验收类 Agent

负责独立验收产品和测试结果。

默认候选：

- `agency-reality-checker`
- `agency-code-reviewer` 作为补充，不作为主验收角色

### 复盘类 Agent

负责识别是否值得沉淀知识、生成复盘草稿、提出知识提炼建议。

默认候选：

- Knowledge Capture Reminder
- AI Weekly Review

### 系统维护类 Agent

负责维护 Jarvis 自身的规则、模板、索引、agent/workflow registry。

该类 agent 只能提出修改建议；结构性修改需要我确认。

## 当前 Agent

| Agent | 类型 | 主要职责 | 主文档 / Prompt | 状态 |
|---|---|---|---|---|
| Development Agent | 开发 | 依据产品方案和技术方案实现小版本改动 | [[Development Agent]] / [[../Prompts/Development Agent|Prompt]] | 已启用：手动触发 |
| Product Acceptance Agent | 验收 | 只基于初始产品方案、技术方案和变更证据做产品验收 + 测试验收 | [[Product Acceptance Agent]] / [[../Prompts/Product Acceptance Agent|Prompt]] | 已启用：手动触发 |
| Knowledge Capture Reminder | 复盘 | 在项目会话结束后提醒是否沉淀知识 | [[../Prompts/Knowledge Capture Reminder|Knowledge Capture Reminder]] | 已启用 |
| AI Weekly Review | 复盘 | 生成每周复盘草稿和系统更新建议 | [[../Prompts/AI Weekly Review|AI Weekly Review]] | 已启用 |

## Repo Local Agent 索引

每个 repo 的本地 agent 由 [[Repo Agent Index]] 统一索引。

本地 agent 命名建议：

```text
<project>-developer
<project>-tester
<project>-release-agent
<project>-acceptance-agent
<project>-knowledge-agent
```

本地 agent 文档建议放在：

```text
<repo>/agents/<agent-name>.md
```

## 新增 Agent 登记模板

```markdown
## Agent Name

类型：
作用域：Global | Repo Local
状态：规划中 | 已启用 | 暂停 | 废弃
主 Prompt：
关联 Workflow：
关联模板：
所属 repo：

### 职责

### 输入

### 输出

### 触发时机

### 权限边界

### 不允许做什么
```

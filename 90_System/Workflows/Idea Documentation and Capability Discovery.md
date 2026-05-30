# 想法文档化与能力检索流程

这个 workflow 用来处理用户提出的想法、点子、灵感或初步方案。

核心原则：先把想法变成对应文档，再决定是否执行；进入执行前，先查看 Jarvis 和当前会话已有能力，再检索可能需要的新工具。

## 目标

- 避免想法只停留在聊天里。
- 根据想法类型生成合适文档，而不是默认都变成代码项目。
- 执行方案前先盘点现有 agent、workflow、skill、plugin、repo local agent 和工具。
- 现有能力不足时，再检索对应工具、技能、插件、MCP、CLI、模板或参考项目。

## 触发条件

当用户表达以下意图时触发：

- “我有个想法 / 点子 / idea”
- “帮我记一下这个想法”
- “这个能不能做”
- “帮我把这个方案落地”
- “开始做这个想法”
- “找找有没有工具能做这件事”

如果用户明确只是临时闲聊，不触发长期文档写入；可以先生成草稿并询问是否保存。

## 输入

- 用户原始想法
- 当前动机
- 想法来源
- 期望输出
- 是否准备马上执行
- 已知约束：时间、成本、技术栈、目标用户、交付形式

## 输出

根据想法类型至少生成一个对应文档草稿：

| 想法类型 | 首选文档 | 位置 |
|---|---|---|
| 原始想法 | 想法收集条目 | `30_Ideas/Inbox/` |
| 可行动想法 | 想法简报 | `30_Ideas/Idea Briefs/` |
| 准备进入项目 | 项目启动说明 | `30_Ideas/Promoted/` 或项目卡片 |
| 项目执行方案 | 任务计划 / 技术方案 | 项目 repo 的 `docs/`、`tasks/` 或 `decisions/` |
| Jarvis 系统改进 | workflow / rule / agent 文档草稿 | `90_System/` 对应目录 |
| 学习研究 | 研究笔记草稿 | `40_Knowledge/Notes/` 或 `30_Ideas/Incubation/` |
| 内容 / 音乐 / 职业资产 | 对应 brief 或素材草稿 | 对应层级目录 |

长期写入 Jarvis 知识或系统规则前，需要用户确认。普通想法收集和用户明确要求创建的文档可以直接创建。

## 流程

```text
用户提出想法
  -> 新想法分类
  -> 生成对应文档草稿
  -> 判断是否进入执行
  -> 盘点现有能力
  -> 检索补充工具
  -> 判断是否应新开公共项目会话
  -> 形成执行方案
  -> 按对应 workflow 执行
```

## 阶段规则

### 1. 先分类

先走 [[Classify New Idea|新想法分类流程]]，判断想法属于：

- 应用 / 产品
- 音乐创作
- 内容创作
- 学习 / 研究
- 职业 / 作品集
- 生活 / 个人系统
- 商业 / 变现
- Jarvis 系统

不要默认把想法变成项目。只有适合持续执行和交付时，才升级到 [[Idea to Project|想法到项目流程]]。

### 2. 先生成对应文档

在执行前，先生成能承载该想法的文档。

文档至少包含：

- 原始想法
- 分类
- 为什么重要
- 当前形态
- 最可能输出
- 最小验证动作
- 风险 / 未知
- 下一步

如果用户只是想快速捕获，创建简短 Inbox 条目即可。如果用户已经要求落地，优先创建想法简报或项目启动说明。

### 3. 执行前盘点现有能力

开始实行方案前，先查看：

- [[../Tools/Tools|工具索引]]
- 当前会话实际可用工具列表
- [[../Agents/Agent Registry|Agent Registry]]
- [[../Agents/Workflow Registry|Workflow Registry]]
- [[../Agents/Repo Agent Index|Repo Agent Index]]
- [[../Skills/Skills|Skills]]
- 如果涉及项目代码，进入真实 repo 后读取 repo `AGENTS.md`、`agents/README.md`、`docs/project-home.md`

输出一份简短能力盘点：

```text
已有可用能力：
缺口：
是否需要外部工具：
```

### 4. 再检索对应工具

如果已有能力不足，按顺序检索：

1. Jarvis 内部工具、workflow、templates、prompts。
2. 当前 Codex 会话的 skills、plugins、MCP、browser、automation 等实际能力。
3. Rocky 自定义 skill，尤其是 `github-capability-finder`。
4. 本地 `github-daily-report` 能力归档。
5. GitHub、官方文档或可信来源。

工具检索的目标包括：

- skill
- plugin
- MCP server
- agent / agent framework
- CLI
- workflow template
- prompt pack
- testing / browser / automation / deployment / documentation 工具
- 与项目技术栈匹配的库或框架

检索结果需要给出：

```text
候选工具：
适配场景：
风险：
是否建议安装 / 试用：
下一步：
```

不要自动安装新工具、插件或 skill，除非用户明确确认。

### 5. 判断是否应新开公共项目会话

如果正在新增 skill、workflow、agent、plugin 或工具，并发现它不只服务当前 Jarvis，而是适合给别人复用、发布到 GitHub、提供安装说明或作为独立 repo 长期维护，不要在当前会话继续完整实现。

当前会话只完成：

- 为什么它适合做成公共项目
- 建议形态：skill、plugin、workflow、MCP、CLI 或 repo 项目
- 建议 repo 名和路径
- 第一版范围
- 目录结构
- 本地 Jarvis 接入方式
- 新会话启动 prompt

然后建议用户新开会话独立推进。

### 6. 形成执行方案

执行方案必须引用前面生成的文档，并说明：

- 使用哪些已有能力
- 新检索到哪些工具
- 选用 / 不选用的理由
- 第一阶段如何验证
- 需要用户确认的节点

如果是代码项目，继续走 [[Idea to Project|想法到项目流程]] 或 [[Project Development Acceptance|项目开发验收]]。

## Agent 编排顺序

```text
Jarvis Session
  -> 新想法分类
  -> 文档生成
  -> 能力盘点
  -> 工具检索
  -> 公共项目边界判断
  -> 对应执行 workflow
```

可参与：

- Knowledge Capture Reminder：提醒是否沉淀长期知识。
- Development Agent：当想法进入项目执行时参与。
- Repo Local Agents：当想法对应已有项目 repo 时参与。
- github-capability-finder：当需要检索外部能力时参与。

## 人工确认点

以下动作需要用户确认：

- 长期写入 `40_Knowledge/` 的稳定知识。
- 修改 Jarvis 长期系统规则、agent、workflow、registry。
- 安装新 skill、plugin、MCP、CLI 或其他外部工具。
- 创建或迁移真实项目 repo。
- 将内部能力升级为公共 GitHub 项目。
- 对外发送邮件、发布内容或部署服务。

## 自动化边界

- 可以自动生成用户明确要求的想法文档草稿。
- 可以自动更新必要索引，但不得静默归档、删除、重命名长期文件。
- 可以检索工具和提出建议，但不得自动安装。
- 可以进入项目执行，但真实代码必须在 `~/Workspace/<repo>/`，不放在 Jarvis。
- 如果能力应作为公共项目维护，当前会话只做设计和新会话启动 prompt，不继续实现完整公共项目。

## 固定提示

当用户提出想法并想执行时，先说清楚：

```text
我会先把这个想法整理成对应文档，再检查现有能力和可用工具；如果发现缺口，我会先检索候选工具并给你确认，不会直接安装。
```

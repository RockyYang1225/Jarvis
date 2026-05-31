# 项目开发验收

这个 workflow 用来管理项目的持续开发、独立验收、版本文档和大版本人工验收通知。

核心原则：

- 开发 agent 负责实现和交接。
- 开发 agent 必须先完成自测、自修和证据整理，不能把基础测试失败交给验收 agent 发现。
- 验收 agent 负责产品验收和测试验收。
- 验收 agent 是独立复核，不替代开发自测，也不负责修代码。
- Workflow 负责串联 agent。
- 大版本必须生成版本文档。
- 邮件通知先生成标准邮件内容；真实发送能力单独接入。

## 适用范围

适用于 `~/Workspace` 下的项目 repo。

每个 repo 应该具备：

- `AGENTS.md`
- `agents/README.md`
- `docs/project-home.md`
- `docs/architecture.md`
- `tasks/active.md`
- `tasks/done.md`
- `reviews/project-retros.md`

## 参与角色

### Global Agents

- [[../Agents/Development Agent|Development Agent]]
- [[../Agents/Product Acceptance Agent|Product Acceptance Agent]]

### Repo Local Agents

每个 repo 可按需使用：

- Project Developer Agent
- Project Test Agent
- Project Acceptance Agent
- Project Knowledge Agent

上层索引见 [[../Agents/Repo Agent Index|Repo Agent Index]]。

### Human Owner

你负责：

- 大版本最终验收
- 是否写入长期 Jarvis 知识
- 是否发送版本验收邮件
- 产品方向和优先级取舍

## 输入

开发开始前需要尽量明确：

- 产品方案：用户目标、核心流程、验收标准
- 技术方案：架构、数据、接口、风险
- 当前任务：本次要改什么，不改什么
- 版本边界：小改动还是大版本

如果项目还没有正式产品方案或技术方案，Development Agent 需要先补一份最小版本。

## 标准流程

1. 选择任务
2. Development Agent 读取产品方案、技术方案、repo 规则和当前任务
3. Development Agent 实现改动
4. Development Agent 自测：运行项目要求的构建、单元测试、集成测试和必要的 UI / 模拟器路径验证
5. 如果自测失败，Development Agent 必须先定位原因、修改代码或测试、重新验证；不能进入交接
6. Development Agent 更新必要文档并生成变更交接摘要
7. Product Acceptance Agent 只读取允许的交接材料
8. Product Acceptance Agent 独立复跑或抽查关键验证，生成验收报告
9. Workflow 根据结论决定下一步

## 开发自测 Gate

Development Agent 在交接前必须完成自测 gate。缺少证据时，默认不能交接。

必须根据项目类型选择并记录：

- Xcode / iOS 项目：运行 XcodeGen、全量 XCTest、受影响单测；涉及 UI / 交互时，至少做模拟器 smoke test 或截图 / 录屏证据。
- 前端项目：运行 build、lint、单元测试；涉及界面时，用浏览器打开本地页面做关键路径验证并保存截图或文字证据。
- 后端项目：运行单元测试、集成测试或 API smoke test；依赖环境缺失时，Development Agent 应先尝试用 repo 文档或隔离临时环境补齐。
- 全栈项目：分别验证前端、后端和关键联调路径。
- 数据迁移 / 存储模型变化：补充迁移验证方案；如果无法自动验证，必须列为发布前人工验收重点。

自测失败时：

- 先按系统化调试流程定位根因。
- 由 Development Agent 修改代码、测试或本地验证环境。
- 重新运行失败项和相关回归测试。
- 只有自测通过或存在明确不可消除的外部阻塞时，才允许生成交接。

如果存在外部阻塞，交接必须写清楚：

- 哪条命令失败。
- 失败原因和原始错误。
- 已尝试的修复或替代验证。
- 为什么该阻塞不能在当前开发流程内解决。

## 开发交接摘要

开发完成后，Development Agent 必须交接：

- 本次目标
- 实际变更
- 影响范围
- 验证命令和结果
- 自测失败后的修复记录，如果发生过
- 截图、日志或关键证据
- 已更新文档
- 已知风险
- 建议验收重点

## 验收读取边界

Product Acceptance Agent 不读取完整开发会话。

允许读取：

- 初始产品方案
- 初始技术方案
- 当前版本文档
- 变更交接摘要
- 测试证据
- 截图 / 日志 / 命令输出
- repo 内明确的验收标准

不应该依赖：

- 开发过程中的口头解释
- 开发 agent 的主观保证
- 未记录在交接物里的背景信息

## 小改动验收

每次小改动完成后，生成 [[../Templates/Acceptance Report|验收报告]]。

结论只能是：

- 通过
- 需要修改
- 阻塞

如果结论是“需要修改”或“阻塞”，Development Agent 根据验收报告修复，再重新交接。

验收发现开发自测本该发现的问题时，Workflow 必须回到 Development Agent 阶段，并在交接里补写：

- 为什么开发自测漏掉。
- 已新增或修正的自测步骤。
- 复跑结果。

## 大版本验收

触发大版本时，必须生成：

- [[../Templates/Version Acceptance Document|版本验收文档]]
- [[../Templates/Acceptance Report|验收报告]]
- [[../Templates/Version Acceptance Email|版本验收邮件]]

邮件收件人：

```text
<owner-email@example.com>
```

当前规则是先生成邮件正文并提醒你确认；后续接入邮件自动化后，再由自动化负责发送。

## 大版本触发条件

满足任一条件即可视为大版本：

- 一个 milestone 完成
- 新增主要用户流程
- UI / 交互有明显变化
- API / 数据结构有破坏性变化
- 准备发布或部署
- 多个小改动累计成一个可验收版本

## 必须更新的文档

每次小改动至少考虑更新：

- `tasks/active.md`
- `tasks/done.md`
- `docs/project-home.md`
- `knowledge/implementation-notes.md`

涉及架构时更新：

- `docs/architecture.md`
- `decisions/`

形成版本时更新：

- `docs/roadmap.md`
- `reviews/project-retros.md`
- 版本验收文档

## 知识沉淀提醒

验收完成后，如果本次产生了可沉淀内容，沿用固定提醒语：

```text
本次会话可能产生了值得沉淀的知识，要我准备一份知识沉淀草稿吗？
```

写入长期 Jarvis 知识前必须由你确认。

## 相关文件

- [[../Agents/Agent Registry|Agent Registry]]
- [[../Agents/Workflow Registry|Workflow Registry]]
- [[../Agents/Repo Agent Index|Repo Agent Index]]
- [[../Prompts/Development Agent|Development Agent Prompt]]
- [[../Prompts/Product Acceptance Agent|Product Acceptance Agent Prompt]]
- [[../Templates/Acceptance Report|验收报告模板]]
- [[../Templates/Version Acceptance Document|版本验收文档模板]]
- [[../Templates/Version Acceptance Email|版本验收邮件模板]]

# 工具索引

这个文件说明 Jarvis 可以调度哪些工具和能力。

注意：Codex 每次会话可用的工具可能不同。这里是 Jarvis 的能力索引；执行前仍要看当前会话实际可用工具。

## Jarvis 内部工具

| 工具 | 用途 | 入口 |
|---|---|---|
| Agent Registry | 管理全局 agent | [[../Agents/Agent Registry|Agent Registry]] |
| Workflow Registry | 管理 workflow 编排 | [[../Agents/Workflow Registry|Workflow Registry]] |
| Repo Agent Index | 管理 repo local agents | [[../Agents/Repo Agent Index|Repo Agent Index]] |
| Skills | Jarvis 自定义 skills | [[../Skills/Skills|Skills]] |
| Prompts | 给 Codex / agent 执行的提示词 | [[../Prompts/Prompts|Prompts]] |
| Templates | 常用文档模板 | [[../Templates/Templates|Templates]] |
| Rules | Jarvis 系统规则 | [[../Rules/Rules|Rules]] |
| Automation | 自动化配置入口 | [[../Automation/Automation|Automation]] |

## 主要 Workflows

| Workflow | 什么时候用 | 入口 |
|---|---|---|
| 新想法分类 | 捕获任何新想法，判断它属于代码、音乐、内容、学习等哪一类 | [[../Workflows/Classify New Idea|新想法分类]] |
| 想法文档化与能力检索 | 用户提出想法后，先生成对应文档；准备执行时盘点现有能力并检索工具 | [[../Workflows/Idea Documentation and Capability Discovery|想法文档化与能力检索]] |
| 想法到项目 | idea 准备变成可执行项目 | [[../Workflows/Idea to Project|想法到项目]] |
| 项目开发验收 | 项目持续开发、小改动验收、大版本验收 | [[../Workflows/Project Development Acceptance|项目开发验收]] |
| 项目生命周期 | 管理项目从启动到复盘 | [[../Workflows/Project Lifecycle|项目生命周期]] |
| 知识沉淀提醒 | 会话结束后判断是否沉淀知识 | [[../Workflows/Knowledge Capture Reminder|知识沉淀提醒]] |
| 每周复盘 | 周期性回顾和系统更新 | [[../Workflows/Weekly Review|每周复盘]] |

## Superpowers 技能

用于规范开发过程。

常用技能：

- brainstorming：把模糊想法变成方案
- writing-plans：把方案拆成实施计划
- executing-plans：按计划执行
- test-driven-development：先测后改
- systematic-debugging：系统化排查问题
- verification-before-completion：完成前必须验证
- requesting-code-review：请求代码审查
- receiving-code-review：处理代码审查反馈

常见位置：

```text
~/.agents/skills/
/Users/rockyyang/.codex/plugins/cache/openai-curated/superpowers/
```

## Jarvis 自定义 Skills

| Skill | 用途 | 位置 |
|---|---|---|
| github-capability-finder | 先查本地 github-daily-report，再去 GitHub 找插件、skill、agent、MCP、CLI、workflow、开发者工具 | `90_System/Skills/github-capability-finder` |
| github-project-publisher | 将本地项目或已有仓库安全发布到 GitHub / 远程 git 仓库，支持创建/连接 repo、push、Release、GitHub Pages 和发布前安全检查 | `90_System/Skills/github-project-publisher` |
| project-readme-builder | 生成或刷新项目全局 README，支持多语言、内部/外部链接、使用说明、SVG 和生成图片等视觉资产 | `90_System/Skills/project-readme-builder` |

发现入口：

```text
~/.agents/skills/github-capability-finder -> <jarvis-root>/90_System/Skills/github-capability-finder
~/.agents/skills/github-project-publisher -> <jarvis-root>/90_System/Skills/github-project-publisher
~/.agents/skills/project-readme-builder -> <jarvis-root>/90_System/Skills/project-readme-builder
```

## Agency-Agent 技能

用于补充专业角色能力。

当前已安装：

- `agency-software-architect`
- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-rapid-prototyper`
- `agency-code-reviewer`
- `agency-reality-checker`

位置：

```text
~/.codex/skills/agency-*
```

使用方式：

- 开发 agent 可以参考 architecture / frontend / backend / prototype 相关技能。
- 验收 agent 主要参考 `agency-reality-checker`。
- 代码审查使用 `agency-code-reviewer`，但它不替代产品验收。

## Repo 本地工具

每个项目 repo 可以有自己的本地规则和工具。

标准入口：

```text
~/Workspace/<repo>/AGENTS.md
~/Workspace/<repo>/agents/README.md
~/Workspace/<repo>/docs/project-home.md
```

常见项目内文档：

- `docs/`
- `tasks/`
- `decisions/`
- `knowledge/`
- `reviews/`

## App / 系统工具

当前会话可能提供这些能力，使用前以实际工具列表为准：

- Browser：操作 Codex 内置浏览器
- Chrome：操作用户 Chrome
- Computer Use：操作本机 App
- Documents：处理 Word / docx
- Spreadsheets：处理表格
- Presentations：处理 PPT
- Web：查最新信息
- Image generation：生成或编辑图片
- Automations：创建提醒或周期任务

## 工具选择规则

- 代码改动：优先读 repo `AGENTS.md`，再按项目技术栈选技能。
- 想法执行：先走 [[../Workflows/Idea Documentation and Capability Discovery|想法文档化与能力检索]]，生成对应文档，再查看现有能力并检索工具。
- UI / 浏览器验证：优先用 Browser 或 Chrome 做真实页面验证。
- 高风险完成声明：必须使用 verification-before-completion 的思路验证。
- 产品验收：走 [[../Workflows/Project Development Acceptance|项目开发验收]]。
- 知识沉淀：先生成草稿，长期写入前确认。

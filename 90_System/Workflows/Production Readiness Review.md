# 生产上线准备度评审

这个 workflow 用于在项目、demo app、Web app、API 或全栈项目被认为可以上线、发布、部署或公开使用之前，做一次证据优先的上线准备度评审。

## 适用范围

- demo app 准备从展示进入真实用户使用
- API 准备被外部或生产系统调用
- Web app 准备公开发布
- 全栈项目准备部署到 staging 或 production
- 通用项目需要判断是否具备发布条件

## 使用工具

主项目：

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo
```

主 skill：

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/SKILL.md
```

本地检查脚本：

```text
<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/scripts/inspect_project.py
```

## 输入

评审开始前尽量明确：

- 项目路径
- 项目类型：API、Web app、全栈项目、通用项目
- 目标部署环境：本地演示、内部试点、staging、public production
- 发布范围：demo、内部使用、灰度、公开发布
- 风险容忍度：尤其是认证、数据、支付、隐私、对外 API
- 已有证据：测试输出、截图、日志、部署记录、监控记录、文档

## 标准流程

1. 读取目标项目入口规则，例如 `AGENTS.md`、`agents/README.md`、`docs/project-home.md`。
2. 使用 production-readiness skill 判断评审范围。
3. 如果能访问本地文件，运行：

```bash
python3 "<jarvis-root>/90_System/Tools/External Tools/plugins/production-readiness/repo/skills/production-readiness/scripts/inspect_project.py" /path/to/project
```

4. 根据项目类型读取对应检查域 reference。
5. 收集证据：源码、配置、文档、测试、日志、截图、命令输出。
6. 输出上线准备度报告。
7. 如果结论为“需要修改”或“不适合上线”，回到开发 workflow 修复后再评审。

## 输出

评审报告必须包含：

```text
Production Readiness Review

Conclusion: Ready | Conditionally Ready | Not Ready
Scope:
Project Type:
Evidence Reviewed:

Must Fix Before Production:

High-Risk Gaps:

Recommended Improvements:

Domain Findings:

Commands / Checks Run:

Unverified Assumptions:

Release Checklist:
```

## 结论规则

- `Ready`：没有已知上线阻塞项，关键生产控制有证据，剩余问题风险低。
- `Conditionally Ready`：可以在明确限制下内部发布、试点、灰度或 demo 发布。
- `Not Ready`：缺少关键安全、可靠性、部署、数据或验证证据。

## 人工确认点

这些动作必须由 Human Owner 确认：

- 真实生产部署
- 公开发布
- 对外发通知或邮件
- 写入长期 Jarvis 知识
- 删除、归档、重命名长期项目资产

## 自动化边界

评审 agent 可以读取文件、运行检查命令、生成报告和建议。

评审 agent 不可以：

- 静默部署
- 静默修改目标项目
- 静默发送外部通知
- 静默写入长期 Jarvis 知识
- 把未验证内容说成事实

## 相关文件

- [[../Agents/Workflow Registry|Workflow Registry]]
- [[Project Development Acceptance|项目开发验收]]
- [[../Tools/External Tools/plugins/production-readiness/production-readiness|production-readiness]]

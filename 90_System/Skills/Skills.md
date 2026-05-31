# Skills

这里索引 Rocky 自定义 skills。

真实 skill 文件优先放在 Jarvis 里。  
如果 Codex 需要从 `.agents/skills` 自动发现，则在 `.agents/skills` 保留软链接。

## 当前 Skills

| Skill | 用途 | Jarvis 位置 | 发现入口 |
|---|---|---|---|
| email-draft-sender | 写邮件、生成邮件草稿、校验收件人/正文/附件，并在邮件能力已配置且用户明确确认后安全发送 | [[email-draft-sender/SKILL|email-draft-sender]] | `~/.agents/skills/email-draft-sender` |
| github-capability-finder | 先查本地 github-daily-report，再去 GitHub 找插件、skill、agent、MCP、CLI、workflow、开发者工具 | [[github-capability-finder/SKILL|github-capability-finder]] | `~/.agents/skills/github-capability-finder` |
| github-project-publisher | 将本地项目或已有仓库安全发布到 GitHub / 远程 git 仓库，支持创建/连接 repo、push、Release、GitHub Pages 和发布前安全检查 | [[github-project-publisher/SKILL|github-project-publisher]] | `~/.agents/skills/github-project-publisher` |
| project-readme-builder | 为项目生成或刷新全局 README，支持项目介绍、使用方式、多语言、超链接、SVG 或生成图片等视觉资产 | [[project-readme-builder/SKILL|project-readme-builder]] | `~/.agents/skills/project-readme-builder` |

## 规则

- 新增自定义 skill 时，真实目录放在 `90_System/Skills/<skill-name>`。
- 如需被 Codex 自动发现，在 `~/.agents/skills/<skill-name>` 创建软链接。
- 更新 skill 时，同步更新本索引和 [[../Tools/Tools|工具索引]]。
- Skill 的用户说明可以中文；执行 prompt 和机器规则可以英文。

## 相关

- [[../Tools/Tools|工具索引]]
- [[../Agents/Agent Registry|Agent Registry]]
- [[../Workflows/Workflows|Workflows]]

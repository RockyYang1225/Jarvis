# Jarvis

Jarvis 是一个基于 Markdown 的个人工作操作系统，用来配合 Codex 管理项目路由、想法捕获、workflow、agent、模板、skill、知识沉淀和复盘循环。

它适合想让 AI 辅助工作拥有记忆、边界和可重复流程的人：Jarvis 管工作系统，真实代码留在独立项目仓库里。

![Jarvis system map](../docs/assets/jarvis-system-map.svg)

Languages: [English](../README.md) | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../LICENSE)
[![Quick Start](https://img.shields.io/badge/Quick%20Start-install-blue.svg)](#快速开始)
[![Codex Ready](https://img.shields.io/badge/Codex-ready-111827.svg)](#配合-codex-使用)

## 目录

- [为什么需要 Jarvis](#为什么需要-jarvis)
- [你会得到什么](#你会得到什么)
- [快速开始](#快速开始)
- [配合 Codex 使用](#配合-codex-使用)
- [项目结构](#项目结构)
- [公开与本地边界](#公开与本地边界)
- [Skills、Workflows 和 Agents](#skillsworkflows-和-agents)
- [常用命令](#常用命令)
- [发布前检查](#发布前检查)
- [许可证](#许可证)

## 为什么需要 Jarvis

AI 编程会话如果从错误的位置开始，很容易把项目代码、规划笔记、可复用知识、私人记录和临时想法混在一起。Jarvis 的作用是给这些工作一张稳定地图。

核心原则很简单：个人工作系统放在 Jarvis，真实源码放在独立项目仓库；`AGENTS.md` 和 `90_System/` 层负责把每次会话路由到正确的 workflow。

## 你会得到什么

### 可复用的工作系统骨架

Jarvis 内置 Home、Workspace、Ideas、Knowledge、Reviews、Career、System 等标准层级，用来承载控制台、项目索引、想法、知识、复盘、职业资产和系统规则。

### Codex 会话路由

顶层 `AGENTS.md` 会告诉 Codex 先读哪些文件、什么时候进入真实项目 repo、什么时候分类想法，以及什么时候需要先确认再写入长期知识。

### Workflow 和 Agent 注册表

`90_System/` 存放可复用 workflow、agent registry、prompt、template、rule 和 tool，让系统能力可以持续演化，而不是散落在随机笔记里。

### 跟随 repo 的 Skills

自定义 skill 放在 `90_System/Skills/` 下，安装脚本会把它们链接到 `~/.agents/skills`。

### 默认保护隐私

这个 repo 设计成发布可复用系统骨架，同时默认不提交真实项目卡片、个人复盘、简历、面试记录、缓存和本地运行文件。

## 快速开始

### 1. 克隆

```bash
git clone https://github.com/RockyYang1225/Jarvis.git Jarvis
cd Jarvis
```

### 2. 安装本地支持

```bash
./scripts/install.sh
```

安装脚本可以重复运行。它会创建标准目录、保留已有本地文件、补 `.gitkeep` 占位文件，并把 repo 内置 skill 链接到 `~/.agents/skills`。

### 3. 验证

```bash
./scripts/public-readiness-scan.sh
```

之后从 Jarvis 根目录打开 Codex，让顶层 `AGENTS.md` 先被加载。

## 配合 Codex 使用

从 Jarvis 根目录启动 Codex。顶层 `AGENTS.md` 会告诉 Codex 如何路由工作：

- 项目代码放在 `~/Workspace/<repo>`
- Jarvis 存放思考、索引、可复用知识、workflow、prompt、template 和 skill
- 长期知识写入前需要确认
- 面向用户的 Jarvis 笔记默认使用中文
- agent prompt 和执行规则可以在更清晰时使用英文

如果要改项目代码，进入真实项目 repo，并先读该 repo 的 `AGENTS.md`、`agents/README.md` 和 `docs/project-home.md`。

## 项目结构

```text
00_Home/        控制台、当前重点、使用说明
10_Workspace/   项目索引和项目卡片，不放源码
20_Career/      简历、面试、作品集资产
30_Ideas/       想法收集箱、简报、分类、孵化
40_Knowledge/   稳定可复用知识索引和笔记
50_Reviews/     日、周、月、项目、面试复盘
90_System/      Jarvis 规则、模板、agent、workflow、prompt、skill
docs/           设计文档、实施计划、项目说明
scripts/        安装器、检查脚本、维护工具
```

真实应用源码通常放在 Jarvis 之外：

```text
~/Workspace/<repo>
```

## 公开与本地边界

适合提交到 Git：

- `AGENTS.md`
- `README.md`
- `00_Home/` 通用操作入口
- `30_Ideas/` 分类和 workflow 索引
- `90_System/` agents、workflows、templates、prompts、rules、tools、skills
- 顶层索引文件
- 脱敏后的示例和模板

默认留在本地：

- 真实活跃项目卡片
- 简历和面试记录
- 私人知识笔记
- 日、周、月、项目复盘
- secrets、tokens、本地自动化状态、导出文件、缓存、日志

`.gitignore` 会偏保守地保护本地内容。如果某个私人区域需要公开示例，优先新增脱敏示例或模板，而不是提交真实笔记。

## Skills、Workflows 和 Agents

### 添加 Skill

把 repo 自带 skill 放在：

```text
90_System/Skills/<skill-name>/SKILL.md
```

然后运行：

```bash
./scripts/install.sh
```

安装器会把 skill 链接到：

```text
~/.agents/skills/<skill-name>
```

### 添加 Workflow、Agent 或模板

使用这些系统目录：

- `90_System/Workflows/`
- `90_System/Agents/`
- `90_System/Templates/`
- `90_System/Prompts/`
- `90_System/Rules/`
- `90_System/Tools/`

新增可复用能力时，同步更新对应 registry 或 index。

## 常用命令

| 任务 | 命令 |
|---|---|
| 安装或刷新本地 skill 链接 | `./scripts/install.sh` |
| 发布前扫描公开文件 | `./scripts/public-readiness-scan.sh` |
| 检查 README 链接 | `rtk python3 90_System/Skills/project-readme-builder/scripts/check_readme_links.py . READMEs/README.zh-CN.md` |
| 查看 Git 状态 | `git status --short` |

## 发布前检查

公开发布前运行：

```bash
./scripts/public-readiness-scan.sh
git status --short
```

检查变更和跟踪文件列表。不要把私人项目卡片、简历、面试记录、secret 或个人复盘发布出去，除非它们已经被明确脱敏。

## 项目状态

Jarvis 是一个持续演化中的个人工作系统模板。它现在可以作为 Markdown/Codex 工作区使用，但每个使用者都应该按自己的工作方式调整 workflow、template、prompt 和隐私规则。

## 许可证

MIT License。见 [LICENSE](../LICENSE)。

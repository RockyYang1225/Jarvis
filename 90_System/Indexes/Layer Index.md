# 层级索引

这个文件维护 Jarvis 每一层的入口索引。

原则：每个层级都要有一个稳定入口。新建目录时，同时创建或指定该目录的索引文件，并从上层索引链过去。

## 顶层入口

| 层级 | 职责 | 索引 |
|---|---|---|
| Jarvis | 顶层系统入口 | [[../../00_Home/Dashboard|Dashboard]] / `AGENTS.md` |
| Home | 控制台、当前重点、使用说明 | [[../../00_Home/Dashboard|Dashboard]] |
| Workspace | 项目索引和项目状态 | [[../../10_Workspace/Projects|Projects]] |
| Career | 简历、面试、作品集 | [[../../20_Career/Career|Career]] |
| Ideas | 想法收集和孵化 | [[../../30_Ideas/Ideas|Ideas]] |
| Knowledge | 长期可复用知识 | [[../../40_Knowledge/Knowledge|Knowledge]] |
| Reviews | 日、周、项目、面试复盘 | [[../../50_Reviews/Reviews|Reviews]] |
| System | Jarvis 规则、模板、agent、workflow | [[../System|System]] |

## Workspace 子层

| 层级 | 索引 |
|---|---|
| Active Projects | [[../../10_Workspace/Active Projects/Active Projects|Active Projects]] |
| Incubating Projects | [[../../10_Workspace/Incubating Projects/Incubating Projects|Incubating Projects]] |
| Paused Projects | [[../../10_Workspace/Paused Projects/Paused Projects|Paused Projects]] |
| Archived Projects | [[../../10_Workspace/Archived Projects/Archived Projects|Archived Projects]] |

## Career 子层

| 层级 | 索引 |
|---|---|
| Resume | [[../../20_Career/Resume/Resume|Resume]] |
| Interviews | [[../../20_Career/Interviews/Interviews|Interviews]] |
| Portfolio | [[../../20_Career/Portfolio/Portfolio|Portfolio]] |
| Job Market | [[../../20_Career/Job Market/Job Market|Job Market]] |
| Stories | [[../../20_Career/Stories/Stories|Stories]] |

## Ideas 子层

| 层级 | 索引 |
|---|---|
| Inbox | [[../../30_Ideas/Inbox/Inbox|Inbox]] |
| Categories | [[../../30_Ideas/Categories/Categories|Categories]] |
| Idea Briefs | [[../../30_Ideas/Idea Briefs/Idea Briefs|Idea Briefs]] |
| Incubation | [[../../30_Ideas/Incubation/Incubation|Incubation]] |
| Parked | [[../../30_Ideas/Parked/Parked|Parked]] |
| Promoted | [[../../30_Ideas/Promoted/Promoted|Promoted]] |

## Knowledge 子层

| 层级 | 索引 |
|---|---|
| Topics | [[../../40_Knowledge/Topics/Topics|Topics]] |
| Notes | [[../../40_Knowledge/Notes/Notes|Notes]] |
| Sources | [[../../40_Knowledge/Sources/Sources|Sources]] |
| Patterns | [[../../40_Knowledge/Patterns/Patterns|Patterns]] |
| Glossary | [[../../40_Knowledge/Glossary/Glossary|Glossary]] |

## Reviews 子层

| 层级 | 索引 |
|---|---|
| Daily | [[../../50_Reviews/Daily/Daily|Daily]] |
| Weekly | [[../../50_Reviews/Weekly/Weekly|Weekly]] |
| Monthly | [[../../50_Reviews/Monthly/Monthly|Monthly]] |
| Project Retros | [[../../50_Reviews/Project Retros/Project Retros|Project Retros]] |
| Interview Retros | [[../../50_Reviews/Interview Retros/Interview Retros|Interview Retros]] |

## System 子层

| 层级 | 索引 |
|---|---|
| Agents | [[../Agents/Agent Registry|Agent Registry]] |
| Skills | [[../Skills/Skills|Skills]] |
| Workflows | [[../Workflows/Workflows|Workflows]] |
| Templates | [[../Templates/Templates|Templates]] |
| Prompts | [[../Prompts/Prompts|Prompts]] |
| Rules | [[../Rules/Rules|Rules]] |
| Indexes | [[Indexes|Indexes]] |
| Tools | [[../Tools/Tools|Tools]] |
| Automation | [[../Automation/Automation|Automation]] |

## 新建层级规则

新建目录时同步处理：

1. 创建目录内索引文件。
2. 从父级索引链接过去。
3. 如属于顶层或二级层，更新本文件。
4. 如果会被 Codex 使用，更新 `AGENTS.md` 或相关 workflow。

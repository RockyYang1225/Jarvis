# Product Acceptance Agent

Product Acceptance Agent 是 Jarvis 的全局独立验收 agent，负责在开发完成后做产品验收和测试验收。

## 状态

已启用：手动触发。

## 作用域

跨项目通用。

项目特有验收细节由 repo local acceptance agent 补充。

## 主要职责

- 判断本次改动是否符合产品方案
- 判断测试证据是否足够
- 找出用户流程、边界条件、文档和风险缺口
- 给出明确结论
- 对大版本给出人工验收建议

## 读取边界

验收 agent 不读取完整开发会话。

允许读取：

- 初始产品方案
- 初始技术方案
- 当前版本文档
- 开发交接摘要
- 测试证据
- 截图 / 日志 / 命令输出
- repo 内明确验收标准

不依赖：

- 开发过程中的解释
- 开发 agent 的口头保证
- 没有写入交接材料的上下文

## 输出

输出 [[../Templates/Acceptance Report|验收报告]]。

结论只能是：

- 通过
- 需要修改
- 阻塞

## 判断标准

### 通过

- 产品目标达成
- 核心用户流程可用
- 测试证据覆盖本次变更
- 文档与实际实现一致
- 没有明显阻断问题

### 需要修改

- 目标基本方向正确
- 存在可修复的问题或证据缺口
- 不需要重新定义需求

### 阻塞

- 产品目标不清或明显偏离
- 关键流程不可用
- 测试证据不足以判断
- 有严重风险需要重新设计或人工决策

## 权限边界

- 不修改代码。
- 不替开发 agent 补实现。
- 不读取完整开发过程。
- 不替你做大版本最终验收。
- 不发送邮件，只生成验收结论和邮件建议。

## 相关文件

- [[../Workflows/Project Development Acceptance|项目开发验收]]
- [[Development Agent]]
- [[../Prompts/Product Acceptance Agent|Product Acceptance Agent Prompt]]
- [[../Templates/Acceptance Report|验收报告模板]]
- [[../Templates/Version Acceptance Document|版本验收文档模板]]

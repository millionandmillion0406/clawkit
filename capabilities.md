# 能力详解：OpenClaw vs Claude Code/Codex/Gemini CLI

---

## 什么是 Claude Code / Codex / Gemini CLI

它们本质上是同一个东西的不同实现：**一个能操作终端、读写文件、执行命令的 AI Agent**。

- **Claude Code**：Anthropic 出品，运行在终端里，用 Claude 模型
- **OpenAI Codex CLI**：OpenAI 出品，终端 Agent（2025），用 GPT-4。注意：旧的 Codex 模型（2021）已停用，现在的产品是 Codex CLI
- **Gemini CLI**：Google 出品，终端 Agent，用 Gemini
- **ZCode**：智谱出品，终端 Agent + 桌面 IDE 集成，用 GLM-5.2

它们共同的能力：
1. 递归探索代码库（rg / grep / tree）
2. 编辑文件（diff / apply_patch 或直接覆写）
3. 执行终端命令（bash / python）
4. Git 操作（diff / commit / branch）
5. 自主工作流（读 → 改 → 验证 → 循环）

## OpenClaw 的对等能力

OpenClaw 默认就有的：
- `read` — 读取任意文件
- `write` — 创建/覆写文件
- `exec` — 执行终端命令
- 多模型 — GLM-5-Turbo / DeepSeek / GLM-5V / Qwen，按需切换

OpenClaw 独有的：
- **24/7 自主运行** — crontab + systemd 守护
- **多通道** — 微信/邮箱/QQ 触发
- **跨会话记忆** — MEMORY.md + 知识管家（注意：敏感凭证不放 MEMORY.md，用环境变量）
- **全链路闭环** — 开发 → 部署 → 监控 → 告警 → 修复

## 差距：不是能力，是工具

OpenClaw 不缺能力，缺的是**等价工具**：

| Codex 做的 | OpenClaw 缺的 | 补法 |
|-----------|-------------|------|
| 项目结构一览 | tree_cmd.py | 本 repo 有 |
| 持续终端 | tmux 会话 | 配一下 |
| Git 可视化 | GitHub API | MEMORY.md 里有 Token |

补完这三样后，OpenClaw 在**写代码**层面跟它们对等，在**运维+自主性**层面远超它们。

## 为什么 OpenClaw 更适合生产环境

Claude Code / Codex 属于"开发态 Agent"——打开电脑、开始写代码、写完关掉。适合原型开发。

OpenClaw 属于"运维态 Agent"——代码写完只是开始。部署、监控、定时任务、异常告警、根据反馈迭代。适合生产服务。

**结论**：不是替代关系，是互补关系。开发阶段用 Codex/Claude Code，生产阶段用 OpenClaw。如果你只能选一个，选 OpenClaw——因为它能覆盖全生命周期。

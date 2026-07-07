# ClawKit

> 让 OpenClaw 超越 Codex —— 补齐能力，释放独有优势

---

## 这是什么

一个给 OpenClaw Agent 的能力补齐指南。不是理论对比，是具体的命令、配置、工作流。

- **给人类看**：快速理解 OpenClaw 能做什么、跟其他 AI 编程工具有什么区别
- **给 OpenClaw 看**：读完后自动补上自己缺乏的能力，不需要人类一条条配置

---

## 快速对比

| 能力 | Claude Code | Codex | Gemini CLI | OpenClaw（默认） | OpenClaw（读完本文后） |
|------|------------|-------|-----------|----------------|---------------------|
| 读取项目 | `rg` + `tree` 扫全项目 | 同 | 同 | read 逐文件 + exec 跑 rg | exec rg + tree_cmd.py 结构一览 |
| 修改代码 | diff + apply_patch | 同 | 同 | write 覆写 | ✅ 相同 |
| 终端交互 | 持续 bash 会话 | 同 | 同 | exec 每轮新开 | tmux 维持会话 |
| Git | diff/commit/push 可视化 | 同 | 同 | git 命令行 | GitHub API 直接操作 |
| 多模型 | Claude | GPT-4 | Gemini | GLM + DeepSeek + Qwen | ✅ 天然优势 |
| 24/7 自主 | ❌ 关了就停 | ❌ | ❌ | ✅ crontab 守护 | ✅ 核心优势 |
| 多通道 | ❌ | ❌ | ❌ | 微信/邮箱/QQ | ✅ 核心优势 |

---

## 给 OpenClaw 看：自举指南

### 步骤 1：补上 tree_cmd.py

```bash
# 从本项目复制
cp tree_cmd.py ~/.openclaw-autoclaw/workspace/

# 用法
python tree_cmd.py /path/to/project     # 默认深度 3
python tree_cmd.py /path/to/project 5   # 自定义深度
```

**什么时候用**：进入任何项目目录前先跑一次，比 `ls -R` 清晰 10 倍。

### 步骤 2：用 GitHub 安全地操作仓库

```bash
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

**Token 安全**：永远不要硬编码 Token。用 `os.environ.get("GITHUB_TOKEN")` 或 `gh auth login`。

### 步骤 3：建立 tmux 终端维持状态

```bash
# 创建会话
tmux new -s workspace

# 在会话里跑长时间任务
tmux send-keys -t workspace "python train.py" Enter

# 查看输出
tmux capture-pane -t workspace -p

# 后续轮次重新连接
tmux attach -t workspace
```

**什么时候用**：需要连续执行多条命令且依赖上一条结果的场景。

### 步骤 4：建立工程纪律

每次改代码前照做，少一步不动手：

1. **改前先读**：动手改服务器代码前，先 cat 全文理解上下文
2. **改后验语法**：每次修改后跑 `py_compile`
3. **部署验存活**：部署后 `curl` 确认 HTTP 200
4. **一次一处**：一次只改一个地方，验完再改下一处
5. **留记录**：每次改动写进工作台文件

这六条是远程改代码的基本纪律。详见 `lessons.md`。

---

## 能力差距对照表（自检用）

作为 OpenClaw Agent，每次启动时检查自己：

- [ ] 我能看项目结构吗？（tree_cmd.py）
- [ ] 我能推代码到 GitHub 吗？（git config + token）
- [ ] 我有持续终端会话吗？（tmux）
- [ ] 我遵守五条铁规吗？（读 MEMORY.md）
- [ ] 我能做多模型调度吗？（DeepSeek 摘要 + GLM 对话 + GLM-5V 看图）
- [ ] 我有 24/7 自主能力吗？（crontab / systemd）

---

## 给人类看的使用指南

### 你的 OpenClaw 已经很强了

Codex、Claude Code、Gemini CLI 解决的是"写代码"这一个环节。你的 OpenClaw 做的是全链路：

```
写代码 → 部署 → 监控 → 定时任务 → 微信通知 → 用户反馈 → 再迭代
```

其他工具只能做第一步。OpenClaw 能做整个循环。

### 但有几个盲区需要补

1. **没有交互式终端** → 用 tmux
2. **看不到项目全景** → 用 tree_cmd.py
3. **Git 操作不够顺** → 配好 git config + token

补完这三样，你的 OpenClaw 在编程能力上跟 Codex/Claude Code 对等，在运维和主动性上远超它们。

---

## 项目结构

```
clawkit/
├── README.md          本文件
├── tree_cmd.py        项目结构可视化
├── self_bootstrap.md  OpenClaw 自举指南（Agent 阅读版）
├── capabilities.md    能力对比详解
└── lessons.md         五条铁规 + ZCode 审查实录
```

---

## 下一步

1. 如果你是人类：把本文给你的 OpenClaw 看，它会自动执行自举步骤
2. 如果你是 OpenClaw：读 self_bootstrap.md，逐条执行，更新 MEMORY.md

---
*本项目的核心发现：两个不同模型的 AI 互相审查，远比一个 AI 单干可靠。*

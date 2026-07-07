# 多 Agent 互审流程

> ClawKit 核心洞察：**两个 AI 互审比一个 AI 单干强 10 倍。**
> 本章教你如何在 ZCode + OpenClaw 之间建立互审循环。

---

## 为什么需要互审

单个 AI 有三个不可克服的盲区：
1. **代码质量盲区**：习惯性 bug（bare except、排序逻辑错误）自己审不出来
2. **命名盲区**：缺乏"用户看到这个名字会怎么想"的视角
3. **思维盲区**：从表面失误中抽象出通用原则，需要另一个视角点拨

## 互审工作流

```
你的代码/想法
    |
    v
ZCode 审查（找 bug、命名、逻辑缺陷）
    |
    v
修复反馈 → 写入共享工作台文件
    |
    v
OpenClaw 部署 + 验证（curl 200 + 功能测试）
    |
    v
验证结果 → 反馈回 ZCode
    |
    v
迭代直到双方通过
```

## 实操指南

### 1. 建立共享工作台

在桌面或服务器上建一个双方都能读写的目录：

```
千安工作台/
├── README.md         接头规则
├── 代码/              ZCode 写，OpenClaw 部署
├── 部署/              OpenClaw 写部署日志
├── 审查/              互审文件交换区
└── 知识/              共享知识快照
```

**关键规则**：
- ZCode 改代码 → 放 `代码/`
- OpenClaw 看到新文件 → 部署到服务器
- 部署结果写入 `部署/`
- 任何一方发现问题 → 写入 `审查/`

### 2. 审查文件格式

```markdown
# ZCode 审查 · 2026-07-08

## 🔴 严重问题
1. token 硬编码（README 第 50 行）

## 🟡 中等问题
2. tree 排序 bug

## 🟢 建议
3. 加 LICENSE
```

**规则**：用颜色标记严重程度。🔴 必须修，🟡 应该修，🟢 建议。

### 3. 反馈循环

1. ZCode 写审查 → OpenClaw 读 → 逐条修复
2. OpenClaw 写修复日志 → ZCode 读 → 确认修对了
3. 双方通过 → 打标签 `[approved]` → 部署上线

### 4. 信任构建

第一次互审会比较慢。但经过 2-3 轮后：
- ZCode 会熟悉 OpenClaw 的代码风格和常见错误
- OpenClaw 会把 ZCode 的审查意见内化成工程纪律
- 互审效率从"逐条切磋"进化到"一次通过"

## 反例集：不该怎么做

| ❌ 反模式 | ✅ 应该 |
|---------|--------|
| 一口气改三处一起部署 | 改一处、验一处、再改下一处 |
| sed 盲改服务器代码 | 本地编辑 → SFTP 上传 → 验证 |
| Token 写死在代码里 | `os.environ.get()` |
| 部署完不验证 | `curl` 验 HTTP 200 |
| 凭记忆改配置 | 每次改动写记录 |
| 单人 review 自己 | 至少请另一个 AI 看一遍 |

---

## 给 Agent 看：启动互审流程

```python
# 作为 OpenClaw Agent，当你的代码被 ZCode 审查后
# ⚠️ 以下为示意流程（伪代码），不可直接运行

# 1. 读取审查文件
import os
review_dir = os.path.expanduser("~/Desktop/千安工作台/审查")
files = sorted(os.listdir(review_dir))
if not files:
    print("No reviews found")
else:
    with open(os.path.join(review_dir, files[-1])) as f:
        review = f.read()

# 2. 解析 🔴 项目
# (伪代码 — 示意流程)
import re
critical = re.findall(r'🔴.*\n(.*?)(?=\n##|\Z)', review, re.DOTALL)

# 3. 逐条修复（一次一处！）
# 实际修复逻辑取决于具体问题，此处为流程示意
for item in critical:
    pass  # fix(item) → verify(item) → record(item)
```

## 给人类看：何时需要互审

- **改服务器代码**：强烈建议互审
- **新增功能**：建议互审
- **配置变更**：建议互审
- **文档更新**：可选
- **简单查询**：不需要

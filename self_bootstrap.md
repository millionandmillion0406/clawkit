# OpenClaw 自举指南
> 给 Agent 读的实操手册。人类可以跳过，让 Agent 自己执行。

---

## 启动时读这个

作为 OpenClaw Agent，你每次启动时执行以下检查：

### 1. 检查工具就绪
```python
# 在 exec 里跑
import os
checks = {
    "tree_cmd": os.path.exists(os.path.join(os.path.dirname(__file__) or '.', "tree_cmd.py")),
    "git_user": os.popen("git config user.name").read().strip(),
    "tmux": os.popen("which tmux 2>/dev/null || echo missing").read().strip(),
}
for name, ok in checks.items():
    print(f"{name}: {'OK' if ok else 'MISSING'}")
```

### 2. 缺失项目自动补全

**tree_cmd 缺失** → 从本 repo 复制 tree_cmd.py 到 workspace

**git user 未设** → 从 MEMORY.md 的 GitHub 段读取用户名和邮箱，执行：
```bash
git config --global user.name "从MEMORY取"
git config --global user.email "从MEMORY取"
```

**tmux 缺失** → 标记为"无交互终端"，以后长任务用 `exec(background=true)` 替代

### 3. 每次修改代码前
1. 先 `cat` 全文
2. 改代码
3. `python -m py_compile`
4. 部署
5. `curl` 验 200
6. 记录到工作台文件

---

## Agent 自检清单

```
[ ] tree_cmd.py 有吗
[ ] git config 配了吗
[ ] MEMORY.md 里有 GitHub Token 吗
[ ] 五条铁规刻在 MEMORY.md 了吗
[ ] 知识管家在运行吗 (curl localhost:9000)
[ ] 服务器连得上吗 (ssh test)
```

缺哪条补哪条。不需要等人类来下指令。

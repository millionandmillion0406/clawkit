#!/bin/bash
# ClawKit bootstrap.sh - One command to set up all tools
# Usage: bash bootstrap.sh [workspace_dir]

WORKSPACE="${1:-$(pwd)}"
echo "=== ClawKit Bootstrap ==="
echo "Workspace: $WORKSPACE"

# 1. Install tree_cmd
if [ ! -f "$WORKSPACE/tree_cmd.py" ]; then
    echo "[1/4] Installing tree_cmd..."
    cp "$(dirname "$0")/tree_cmd.py" "$WORKSPACE/"
    echo "  tree_cmd.py -> $WORKSPACE/"
else
    echo "[1/4] tree_cmd already installed"
fi

# 2. Configure Git
if [ -z "$(git config user.name 2>/dev/null)" ]; then
    echo "[2/4] Configure Git..."
    if [ -n "$GIT_USER" ] && [ -n "$GIT_EMAIL" ]; then
        # Non-interactive mode (for Agent automation)
        git config --global user.name "$GIT_USER"
        git config --global user.email "$GIT_EMAIL"
    else
        read -p "  GitHub username: " gh_user
        read -p "  GitHub email: " gh_email
        git config --global user.name "$gh_user"
        git config --global user.email "$gh_email"
    fi
else
    echo "[2/4] Git configured: $(git config user.name)"
fi

# 3. Check GitHub Token
if [ -z "$GITHUB_TOKEN" ] && [ -z "$GH_TOKEN" ]; then
    echo "[3/4] GitHub Token not set"
    echo "  Create at: https://github.com/settings/tokens"
    echo "  Choose 'Classic', check 'repo' scope"
    echo "  Then: export GITHUB_TOKEN=ghp_xxx"
else
    echo "[3/4] GitHub Token: OK"
fi

# 4. Check tmux
if command -v tmux &> /dev/null; then
    echo "[4/4] tmux: OK"
else
    echo "[4/4] tmux not installed - interactive terminal unavailable"
    echo "  Install: apt install tmux / brew install tmux"
fi

echo "=== Bootstrap Complete ==="
echo ""
echo "Self-check:"
echo "  tree_cmd: $([ -f "$WORKSPACE/tree_cmd.py" ] && echo OK || echo MISSING)"
echo "  git user: $(git config user.name 2>/dev/null || echo NOT SET)"
echo "  GH_TOKEN: $([ -n "$GITHUB_TOKEN$GH_TOKEN" ] && echo SET || echo NOT SET)"
echo "  tmux: $(command -v tmux &>/dev/null && echo OK || echo MISSING)"

#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required to install Rulesync" >&2
  exit 1
fi

npm install -g rulesync
rulesync install
rulesync generate
rulesync doctor

if command -v uv >/dev/null 2>&1; then
  uv tool install -p 3.13 serena-agent || uv tool upgrade serena-agent
  serena setup claude-code
  serena setup codex
else
  echo "uv not found; skipped Serena installation. Install uv, then run: uv tool install -p 3.13 serena-agent" >&2
fi

echo "Agent stack bootstrap complete. Verify Serena in Claude/Codex with /mcp."

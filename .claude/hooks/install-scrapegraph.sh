#!/bin/bash
# Installs ScrapeGraphAI into ~/.venvs/scrapegraph in Claude Code cloud sessions.
set -euo pipefail
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

VENV="$HOME/.venvs/scrapegraph"
if "$VENV/bin/python" -c "import scrapegraphai" 2>/dev/null; then exit 0; fi

uv venv "$VENV" -q
uv pip install -q -p "$VENV/bin/python" scrapegraphai
# Downgrade after install so scrapegraphai stays latest: playwright 1.56.0
# matches the Chromium preinstalled in /opt/pw-browsers
uv pip install -q -p "$VENV/bin/python" "playwright==1.56.0"

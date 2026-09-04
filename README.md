# roman-claude-context

Shared context and agent configuration for Roman's Claude Code and Codex workflows.

## Current stack

- **Rulesync** — source of truth for shared agent rules.
- **Ponytail** — minimal-diff / reuse-first coding discipline.
- **Planning with Files** — durable task state for long multi-step work.
- **Serena** — optional machine-level semantic code tools via MCP.
- **Spec Kit** — optional spec-driven workflow for product repositories.
- **GitHub Agentic Workflows** — intentionally opt-in; not enabled automatically.

## Repository layout

- `.rulesync/rules/overview.md` — canonical shared policy.
- `rulesync.jsonc` — Rulesync targets and portable skill sources.
- `CLAUDE.md` — Claude rule surface.
- `AGENTS.md` — Codex rule surface.
- `.claude/settings.json` — Claude project plugin configuration.
- `docs/agent-stack.md` — installation and operating details.
- `scripts/bootstrap-agent-stack.sh` — bootstrap Rulesync and Serena on a development machine.

## Claude Code

The repository registers and enables these project plugins through `.claude/settings.json`:

- `ponytail@ponytail`
- `planning-with-files@planning-with-files`

## Codex

Rulesync generates the shared `AGENTS.md` policy and portable skills from:

- `DietrichGebert/ponytail`
- `OthmanAdi/planning-with-files`

Refresh the generated configuration with:

```bash
npm install -g rulesync
rulesync install
rulesync generate
rulesync doctor
```

## Full local bootstrap

From a checkout of this repository:

```bash
bash scripts/bootstrap-agent-stack.sh
```

The script installs/refreshes Rulesync, generates Claude/Codex configuration, and installs/configures Serena when `uv` is available.

See `docs/agent-stack.md` for Serena, Spec Kit, and GitHub Agentic Workflows details.

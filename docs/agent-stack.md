# Claude + Codex agent stack

## Repository-level state

This repository uses Rulesync as the source of truth for shared coding-agent rules.

- Source policy: `.rulesync/rules/overview.md`
- Rulesync manifest: `rulesync.jsonc`
- Claude generated rule surface: `CLAUDE.md`
- Codex generated rule surface: `AGENTS.md`
- Claude project plugins: `.claude/settings.json`

The Rulesync manifest declares portable Codex skills from:

- `DietrichGebert/ponytail`
- `OthmanAdi/planning-with-files`

Claude Code uses the native project plugins for those two projects instead of duplicate generated skills.

## Refresh Rulesync outputs

```bash
npm install -g rulesync
rulesync install
rulesync generate
rulesync doctor
```

`rulesync install` resolves the declared external skills and records their pinned source revisions in the Rulesync lockfile. `rulesync generate` emits the configured Claude/Codex surfaces from `.rulesync`.

## Serena semantic code tools

Serena is intentionally a machine-level integration because it runs an MCP server and needs language-server tooling on the machine where Claude/Codex executes.

Install:

```bash
uv tool install -p 3.13 serena-agent
```

Configure Claude Code:

```bash
serena setup claude-code
```

Configure Codex CLI/App:

```bash
serena setup codex
```

Verify in each client with `/mcp`.

The shared agent policy instructs agents to prefer Serena's symbol-aware navigation/refactoring tools when Serena is connected, while retaining built-in tools for trivial edits and non-code work.

## Spec Kit

Spec Kit is for application/project repositories, not for this context repository itself. Install the CLI once:

```bash
uv tool install specify-cli
```

Initialize it inside a product repository with the integration used for that project, for example:

```bash
specify init --here --force --non-interactive --integration claude
```

Codex is also a supported Spec Kit integration. Use Spec Kit for substantial new features where a durable specification, implementation plan, task breakdown, and convergence check are valuable.

## GitHub Agentic Workflows

`github/gh-aw` is not enabled automatically here. It can run Claude Code or Codex inside GitHub Actions for reasoning-heavy repository automation such as PR review, issue triage, CI-failure investigation, and documentation maintenance.

It is deliberately opt-in because enabling an agentic workflow can consume GitHub Actions/AI quotas and requires reviewing engine authentication, permissions, network access, and safe-output configuration.

## Operating model

1. Rulesync keeps shared agent rules portable.
2. Ponytail minimizes unnecessary implementation while preserving correctness/safety.
3. Planning with Files persists complex-task state outside the context window.
4. Serena supplies semantic code retrieval/refactoring when installed locally.
5. Spec Kit is used in product repos when a full spec-driven workflow is justified.
6. Agentic Workflows are added only for explicit GitHub automation use cases.

# roman-claude-context

Shared context and agent configuration for Roman's Claude/Codex workflows.

## Ponytail integration

### Claude Code

Project settings register and enable `DietrichGebert/ponytail` through `.claude/settings.json`.

### Codex

`AGENTS.md` provides the Ponytail-style minimal-diff rules automatically at repository level, including reuse-first implementation, native/stdlib preference, root-cause fixes, and explicit safety guardrails.

For the full Ponytail Codex plugin (commands, modes, and lifecycle hooks), install it in the Codex environment:

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Then start Codex, review/trust the plugin hooks via `/hooks`, and start a new thread. The same installation is picked up by the Codex desktop app after restart.

Source: https://github.com/DietrichGebert/ponytail

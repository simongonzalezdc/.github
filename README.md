# simongonzalezdc `.github`

Shared defaults for repositories under [simongonzalezdc](https://github.com/simongonzalezdc).

## What’s in this repo

| Path | Job |
| --- | --- |
| [`profile/README.md`](profile/README.md) | Public GitHub profile |
| `.github/workflows/` | Agent-law and health checks |
| `.github/pull_request_template.md` | PR template |
| `docs/agent-law/` | Shared agent workflow rules |
| `scripts/provision-agent-law.py` | Provision those rules into target repos |

Product README and install docs stay in each product repo.

<!-- EMPOWER_ORCHESTRATOR:START -->
## Agent-law contribution rule

This repository follows the Empower Orchestrator law in `docs/agent-law/empower-orchestrator.md`.

If a change exposes a repeated task or repeated agent failure, contributors and agents should either ship the smallest durable prevention artifact or explain why this PR is intentionally one-off.

Automation and durable system changes require the scale/severity/reversibility/predictability blast-radius check before dispatch.
<!-- EMPOWER_ORCHESTRATOR:END -->

## License

See [LICENSE](LICENSE).

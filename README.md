# Simon Gonzalez De Cruz GitHub Defaults

This repository holds shared public GitHub defaults for repositories owned by Simon Gonzalez De Cruz.

## What Lives Here

- `profile/README.md` is the public GitHub organization/profile README content.
- `.github/workflows/` contains reusable repository-health and agent-law checks.
- `.github/pull_request_template.md` gives pull requests a consistent review shape.
- `docs/agent-law/` documents the shared agent workflow rules used across repos.
- `scripts/provision-agent-law.py` helps copy the shared guidance into target repositories.

## How To Use It

Use this repo as the source of truth for public repository defaults and agent-facing workflow guidance. Product-specific README content should stay in each product repository; this repo only defines reusable defaults, templates, and shared doctrine.

## Maintenance Notes

- Keep shared guidance generic enough to apply across repos.
- Put product-specific instructions in the target repo instead of here.
- Update this README when a new default file, workflow, or provisioning script becomes part of the shared surface.

## License

See [LICENSE](LICENSE).

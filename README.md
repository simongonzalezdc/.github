# Simon Gonzalez De Cruz GitHub Defaults

This repository provides the shared public GitHub configuration, reusable workflows, and agent-facing guidance for repositories owned by Simon Gonzalez De Cruz.

## Features

- **Agent Workflow Doctrine**: A standardized set of rules (`docs/agent-law/`) and provisioning scripts (`scripts/provision-agent-law.py`) to ensure consistent AI-assisted development across all repositories.
- **Automated CI & Health Checks**: Pre-configured GitHub Actions workflows for repository health checks, OCR-based code review, and dependency management (Renovate).
- **Public Profile Management**: Houses the organization's public GitHub profile README (`profile/README.md`).
- **Standardized Templates**: Includes a pull request template (`.github/pull_request_template.md`) to ensure consistent and thorough PR descriptions.
- **Dependency Management**: Automated dependency updates configured via `renovate.json`.

## Installation

This is a configuration repository. To use these defaults, you can clone or reference them in your own projects.

```bash
# Clone the repository to access defaults and provisioning scripts
git clone https://github.com/simon/.github.git
cd .github
```

## Quick Start

1. **Provision Agent-Law**: To apply the shared agent workflow doctrine to a target repository, run the provisioning script:
    ```bash
    # Navigate to the target repository's root directory
    cd /path/to/your/target-repo
    python /path/to/simon/.github/scripts/provision-agent-law.py
    ```
2. **Use as a Template Repository**: In your GitHub organization settings, you can designate this repository or a repository created from it as a template to standardize new project initialization.

## Usage

### As a Source of Truth

Refer to this repository for the canonical definitions of:
- **Agent Law**: Understand the rules governing AI agent contributions by reading `docs/agent-law/`.
- **Repository Defaults**: Find shared configuration files, templates, and workflows in the root and `.github/` directory structure.

### For CI/CD and Workflows

The workflows defined in `.github/workflows/` are designed for this repository itself. To apply similar CI patterns to your own repositories:
- Copy or adapt the workflow YAML files.
- Use the `actions/checkout` and `actions/upload-artifact` versions specified here as a reference for maintaining consistent action versions.

### Key Files and Directories

- `profile/README.md`: The public organization profile.
- `docs/agent-law/`: Shared doctrine for AI agent workflows.
- `scripts/provision-agent-law.py`: Script to copy agent-law guidance into a target repo.
- `.github/workflows/`: Reusable workflows for CI and code review.
- `.github/pull_request_template.md`: Standard PR template.
- `AGENTS.md`, `CLAUDE.md`: Top-level guidance files for specific AI agents.
- `CONTRIBUTING.md`: Guidelines for contributing to this repository.
- `renovate.json`: Configuration for automated dependency updates.

## FAQ

**Q: Who is this repository for?**
A: It's primarily for Simon Gonzalez De Cruz and collaborators maintaining multiple repositories under this account, ensuring consistency and automation.

**Q: What is "agent-law"?**
A: It's a documented set of rules and guidelines that govern how AI coding assistants (agents) should behave when contributing to projects, ensuring their work aligns with project standards.

**Q: Can I use these workflows in my own repository?**
A: Yes. The workflows are examples. You should review, adapt, and test them for your specific needs before adding them to your `.github/workflows/` directory.

**Q: How do I update the agent-law rules for a specific project?**
A: Run the provisioning script (`scripts/provision-agent-law.py`) in your project. Then, review the generated files (like `AGENTS.md`) and customize them for your project's specific context.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
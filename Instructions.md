# MiniScale-LM Development Instructions

## Project objective

Build a small, reproducible decoder-only Transformer pre-training framework
in PyTorch.

The project should demonstrate:

- Mathematical correctness
- Reproducible experiments
- Clear and maintainable Python
- Strong automated testing
- Training-performance measurement
- Honest documentation

## Development rules

- Never work directly on the main branch.
- Do not modify unrelated files.
- Do not add dependencies without explaining why.
- Use Python type hints.
- Write or update tests for every behavioral change.
- Run relevant tests after making changes.
- Do not disable or weaken tests merely to make them pass.
- Do not fabricate benchmark results.
- Do not commit datasets, checkpoints, secrets, or API keys.
- Prefer simple implementations over premature abstractions.
- Explain all tensor shapes in model code.
- Ask before launching expensive training or cloud resources.

## Initial technical choices

- Python 3.12
- PyTorch
- pytest
- Ruff
- mypy
- src-based package layout
- YAML configuration
- GitHub Actions for continuous integration

## Workflow

For every task:

1. Inspect the existing repository.
2. Propose a plan before editing.
3. Identify files that will change.
4. Implement one narrow issue.
5. Run tests and static checks.
6. Summarize changes and remaining risks.
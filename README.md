# The Agentic Guy's Python starter template

A modern Python project template with best practices for development, testing, and deployment. This template provides a solid foundation for building Python applications with strong typing, comprehensive testing, and robust tooling.

## Features

- **Python 3.13+**: Leveraging modern Python features
- **[uv](https://docs.astral.sh/uv/)**: Fast, reliable package management
- **Ruff**: All-in-one Python linter and formatter
- **MyPy**: Static type checking with strict mode enabled
- **Pytest**: Testing framework with coverage reporting
- **Pydantic**: Data validation using Python type annotations
- **Security Scanning**: Built-in security checks with Bandit and pip-audit
- **Task Automation**: Using poethepoet (poe) for common development tasks
- **Conventional Commits**: Enforced via commitizen
- **Coverage Requirements**: 85% code coverage minimum

## Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager

## Getting Started

### Setup

```bash
# Clone this repository
git clone https://github.com/theagenticguy/tag-python-starter.git
cd tag-python-starter
# de-git the repo
rm -rf .git

# Install dependencies
uv sync --all-groups

# Activate virtual environment
source .venv/bin/activate

# Install pre-commit hooks
pre-commit install
```

### Development Commands

The template uses [poethepoet](https://github.com/nat-n/poethepoet) to manage common tasks:

```bash
# Format code
poe format

# Lint code
poe lint

# Type check
poe typecheck

# Run all quality checks
poe code-quality

# Run tests
poe test

# Run tests with coverage reporting
poe cov

# Security scanning
poe scan
```

### Commiting

```bash
# Commit changes
cz commit
```

## Project Structure

```bash
.
├── pyproject.toml    # Project configuration and dependencies
├── src/
│   └── package/      # Main package directory
│       ├── __init__.py
│       └── hello.py  # Example module
├── tests/            # Test files
│   └── test_package.py
├── .venv/            # Virtual environment (created by UV)
├── coverage.xml      # Test coverage report
└── uv.lock           # Lock file for dependencies
```

## Customizing the Template

1. Update project metadata in `pyproject.toml`
2. Rename `src/package` to your actual package name
3. Update imports in test files to match your package name
4. Modify version tracking in `tool.commitizen` section of `pyproject.toml`

## Dependencies

- **Core**: boto3, loguru, pydantic
- **Development**: commitizen, mypy, poethepoet, pre-commit, pytest, pytest-asyncio, pytest-cov, ruff
- **Security**: bandit, pip-audit, semgrep

## Building and Publishing

```bash
# Build the package
uv build

# Install the package locally
pip install -e .
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

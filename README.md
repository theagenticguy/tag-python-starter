# tag-python-starter

A modern python project template.

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
# Navigate to your project directory
cd tag-python-starter

# start git
git init

# Install dependencies
uv sync --all-groups

# Activate virtual environment (optional with uv)
source .venv/bin/activate

# Install pre-commit hooks
pre-commit install
```

### Development Commands

The template uses [poethepoet](https://github.com/nat-n/poethepoet) to manage common tasks:

```bash
# Format code
uv run poe format

# Lint code
uv run poe lint

# Type check
uv run poe typecheck

# Run all quality checks
uv run poe code-quality

# Run tests
uv run poe test

# Run tests with coverage reporting
uv run poe cov

# Security scanning
uv run poe scan
```

### Commiting

```bash
# Commit changes
git commit -m "(feat|fix|chore|ci|docs|refactor|test): imperitive present tense message, consise, all lower case, no period at the end"
```

## Project Structure

```bash
.
├── pyproject.toml    # Project configuration and dependencies
├── src/
│   └── tag_python_starter/      # Main package directory
│       ├── __init__.py
│       └── hello.py  # Example module
├── tests/            # Test files
│   └── test_tag_python_starter.py
├── .venv/            # Virtual environment (created by UV)
├── coverage.xml      # Test coverage report
└── uv.lock           # Lock file for dependencies
```

## Next Steps

After creating your project from this template:

1. Initialize git repository: `git init`
2. Make your first commit: `git add . && git commit -m "feat: initial project setup"`
3. Create a remote repository and push your code
4. Start building your amazing Python project!

## Dependencies

- **Core**: boto3, loguru, pydantic
- **Development**: commitizen, mypy, poethepoet, pre-commit, pytest, pytest-asyncio, pytest-cov, ruff
- **Security**: bandit, pip-audit, semgrep

## Building and Publishing

```bash
# Build the package
uv build

# Install the package locally
uv tool install dist/tag_python_starter-0.1.0-py3-none-any.whl
```

## Documentation

Run `uv run poe docs` to preview the documentation locally.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

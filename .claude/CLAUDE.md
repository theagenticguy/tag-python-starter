# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python starter template that uses modern Python tooling:

- Python 3.13+ required
- Uses uv as package manager (<https://docs.astral.sh/uv/>)
- Hatch for build system
- Ruff for linting and formatting
- MyPy for type checking
- Pytest for testing with coverage requirements
- Security scanning with Bandit and pip-audit
- Task automation with poethepoet (poe)

## Virtual Environment

Always make sure to activate the virtual environment before running any commands.

```bash
source .venv/bin/activate
```

## Bash commands

- `source .venv/bin/activate` - Activate the virtual environment
- `poe <command>` - Run a command with poe
- `uv add <dependency>` - Add a dependency
- `uv add --dev <dependency>` - Add a dev dependency
- `uv sync --all-groups` - Install dependencies
- `poe code-quality` - Always run quality checks after editing or adding new code.
- `poe test` - Run tests. NEVER edit files in the tests directory to pass a test.
- `poe cov` - Run tests with coverage report
- `uv build` - Build the package. This will create a wheel file in the dist directory.

IMPORTANT: commit your changes regularly.

- `git add <file|directory> <another file|directory> ...`  - Regularly add
- `git commit -m "<(feat|fix|chore|ci|docs|refactor|test): use the imperative, present tense>"  -s` - Commit with conventional commit messages. must be a single line, valid commit message.
- `git push` - Push the changes to the remote repository

## Project Structure

```bash
.
├── pyproject.toml    # Project configuration, dependencies, and tool settings
├── src/              # Source code
│   └── package/      # Main package
│       ├── __init__.py
│       └── hello.py  # Example module
└── tests/            # Test directory
    └── test_package.py
```

## Standards and Conventions

- YOU MUST use Google docstring convention
- YOU MUST use strict type checking with MyPy
- YOU MUST have 85% minimum code test coverage requirement
- YOU MUST use conventional commit messages via `git commit -m <(feat|doc|fix etc): imperitive present tense message, consise, all lower case, no period at the end`
- YOU MUST run `poe code-quality` when you are done making a series of code changes
- YOU MUST use <type> | None syntax for optional types. PEP 604 introduced a new syntax for union type annotations based on the | operator. This syntax is more concise and readable than the previous typing.Optional syntax.
- ALWAYS dict, list, tuple natively from python isntead of from `typing`

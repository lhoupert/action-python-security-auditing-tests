# 07 · poetry · flat layout · clean

**Package manager**: `poetry`
**Source layout**: flat (Python files at project root)
**Expected outcome**: PASS

## What this tests

- `poetry export` correctly exports dependencies from `poetry.lock`
- Bandit scans the flat project directory
- No bandit issues, no vulnerable deps

## CI setup

The workflow runs `poetry lock` before the action to generate `poetry.lock` from `pyproject.toml`.
Lock file is not committed — generated fresh in CI.

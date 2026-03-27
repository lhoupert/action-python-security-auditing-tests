# 04 · uv · flat layout · clean

**Package manager**: `uv`
**Source layout**: flat (Python files at project root)
**Expected outcome**: PASS

## What this tests

- `uv export` correctly exports dependencies from `uv.lock`
- Bandit scans the flat project directory
- No bandit issues, no vulnerable deps

## CI setup

The workflow runs `uv lock` before the action to generate `uv.lock` from `pyproject.toml`.
Lock file is not committed — generated fresh in CI.

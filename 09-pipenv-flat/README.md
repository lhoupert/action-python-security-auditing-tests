# 09 · pipenv · flat layout · clean

**Package manager**: `pipenv`
**Source layout**: flat (Python files at project root)
**Expected outcome**: PASS

## What this tests

- `pipenv requirements` correctly reads `Pipfile.lock` and exports deps
- Bandit scans the flat project directory
- No bandit issues, no vulnerable deps

## CI setup

The workflow runs `pipenv install` before the action to generate `Pipfile.lock` from `Pipfile`.
Lock file is not committed — generated fresh in CI.

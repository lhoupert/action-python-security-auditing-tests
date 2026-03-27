# 10 · pipenv · src/+scripts/ · bandit HIGH

**Package manager**: `pipenv`
**Source layout**: `src/` + `scripts/` directories
**Expected outcome**: FAIL (bandit)

## What this tests

- Bandit scans two directories via `bandit_scan_dirs: src/,scripts/`
- B602 (`subprocess.call(shell=True)`) in both directories triggers HIGH threshold
- `pipenv requirements` correctly exports deps from `Pipfile.lock`
- Clean deps ensure only bandit fails the job

## Intentional issues

| File | Issue | Severity |
|------|-------|---------|
| `src/handler.py` | B602: `subprocess.call(shell=True)` | HIGH |
| `scripts/deploy.py` | B602: `subprocess.call(shell=True)` | HIGH |

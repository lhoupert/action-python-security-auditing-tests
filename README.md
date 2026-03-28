# action-python-security-auditing — Test Projects

Dummy Python projects for testing the reliability of [action-python-security-auditing](https://github.com/developmentseed/action-python-security-auditing) across different package managers and source layouts.

## Test Matrix

| # | Project | Package manager | Source layout | Expected outcome |
|---|---------|----------------|---------------|-----------------|
| 01 | `01-requirements-flat` | requirements | flat | PASS — no issues |
| 02 | `02-requirements-src-bandit` | requirements | src/ | FAIL — bandit HIGH (B602, B105) |
| 03 | `03-requirements-multi-both` | requirements | src/ + scripts/ | FAIL — bandit HIGH + pip-audit |
| 04 | `04-uv-flat` | uv | flat | PASS — no issues |
| 05 | `05-uv-src-vuln` | uv | src/ | FAIL — pip-audit (fixable CVEs) |
| 06 | `06-uv-multi-bandit` | uv | src/ + scripts/ | FAIL — bandit MEDIUM (B303, B506) |
| 07 | `07-poetry-flat` | poetry | flat | PASS — no issues |
| 08 | `08-poetry-src-both` | poetry | src/ | FAIL — bandit MEDIUM + pip-audit |
| 09 | `09-pipenv-flat` | pipenv | flat | PASS — no issues |
| 10 | `10-pipenv-multi-bandit` | pipenv | src/ + scripts/ | FAIL — bandit HIGH (B602) |
| 11 | `11-requirements-root` | requirements | flat | PASS — no issues (default working dir `.`) |
| 12 | `12-uv-flat-bandit-only` | uv | flat | FAIL — bandit HIGH (B602), pip-audit disabled |
| 13 | `13-requirements-unfixable` | requirements | flat | PASS — unfixable vulns present, `pip_audit_block_on: fixable` does not block |
| 14 | `14-uv-low-threshold` | uv | flat | FAIL — bandit LOW (B101), pip-audit disabled |

## How it works

Each project has a corresponding workflow file in `.github/workflows/`. Workflows call the action with `working_directory` set to the project subdirectory, so all package manager commands and bandit paths resolve correctly relative to the project root.

For uv, poetry, and pipenv projects that use pip-audit, a setup step generates the lock file in CI before the action runs (lock files are not committed). Bandit-only tests (12, 14) skip this step.

# action-python-security-auditing — Smoke Tests

Post-release smoke tests for [action-python-security-auditing](https://github.com/lhoupert/action-python-security-auditing). These 3 scenarios run against the published `@v1` tag after each release to confirm end-to-end behavior is intact.

The full integration test suite (14 scenarios) lives in the action repo itself under `integration-tests/` and runs on every PR there.

## Smoke Test Scenarios

| # | Project | Package manager | Source layout | Expected outcome |
|---|---------|----------------|---------------|-----------------|
| 01 | `01-requirements-flat` | requirements | flat | PASS — no issues |
| 03 | `03-requirements-multi-both` | requirements | src/ + scripts/ | FAIL — bandit HIGH + pip-audit |
| 08 | `08-poetry-src-both` | poetry | src/ | FAIL — bandit MEDIUM + pip-audit |

These three cover: happy path, both tools firing together, and a lockfile-based package manager (poetry).

## How it works

Each scenario has a workflow file in `.github/workflows/` that calls the action with `working_directory` set to the project subdirectory. The `integration-tests.yml` orchestrator runs all 3 and the `validate` job checks outcomes against `expected_results.yml`.

Test 08 (poetry) requires a `poetry.lock` committed in the directory for reliable pip-audit detection of pinned vulnerable versions.

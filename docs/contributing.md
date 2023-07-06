# Contribution guide

## Local development
- The complete test suite depends on having at least the following installed
  (possibly not a complete list)
  - git 
  - python3 (at least 3.8)
  - poetry

## Instruction for creating a commit
1. Clone the repository from your GitHub.
2. Setup development environment through [poetry](https://python-poetry.org/) (`poetry install`).
3. Setup [pre-commit](https://pre-commit.com/) hook (`poetry run pre-commit install`)

## Creating releases

The project uses commitizen for creating releases.
The commitizen uses [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
to release new versions automatically.

*  Commits of type `fix` will trigger bugfix releases, think `0.0.1` e.g. `fix: fix schema`
*  Commits of type `feat` will trigger feature releases, think `0.1.0` e.g. `feat: introduce new schema`
*  Commits with `BREAKING CHANGE` in body or footer will trigger breaking releases, think `1.0.0` `BREAKING CHANGE: introduce V2`

All other commit types will trigger no new release.

More info for [commitizen](https://commitizen-tools.github.io/commitizen/) 
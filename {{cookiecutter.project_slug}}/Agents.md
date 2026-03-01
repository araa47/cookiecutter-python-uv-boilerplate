# Agent Guidelines

- Use `uv` for all dependency management (`uv add`, `uv run`). Never use `requirements.txt`.
- Python 3.13+. Use modern type annotations (`list`, `dict`, not `List`, `Dict`). All code must pass `ty` type checking.
- ClickHouse is the default database. Use `clickhouse_connect` for all interactions.
- Before committing: run `prek run --all-files` and `uv run -m pytest`. All hooks and tests must pass.

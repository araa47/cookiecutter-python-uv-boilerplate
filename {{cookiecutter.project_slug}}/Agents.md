# Agent Development Guidelines

This document outlines best practices and required conventions for developing in this repository.

## Dependency Management

- **Use `uv` for all Python dependency management.**
  - Add new libraries:
    ```sh
    uv add <library>
    ```
  - Run scripts:
    ```sh
    uv run <script.py>
    ```
  - All dependencies are managed in `pyproject.toml`.
  - **Do NOT create or use `requirements.txt`.**
    - Always use `uv add` to manage dependencies.

## Python & ClickHouse Standards

- **Python Version:** Use Python 3.12+.
- **Type Annotations:**
  - Always use standard Python types (e.g., `list`, `dict`, not `List`, `Dict`).
  - Ensure all functions and variables are type-annotated for Pyright compatibility.
- **Database:**
  - Assume ClickHouse as the default database.
  - Use the `clickhouse_connect` library for all ClickHouse interactions.
- **SQL Help:**
  - If a request is for SQL only, focus solely on ClickHouse SQL (ignore Python).

## Development Workflow

- **Pre-commit Hooks:**
  - Always run pre-commit hooks before committing code:
    ```sh
    pre-commit run --all-files
    ```
- **Testing:**
  - Run all `pytest` tests before committing:
    ```sh
    uv run -m pytest
    ```
- **Version Control:**
  - Use clear, descriptive commit messages.
  - Commit only code that passes all hooks and tests.

## Summary

- Use `uv` for all dependency management.
- Do not use `requirements.txt`.
- Use Python 3.12+ with full type annotations.
- Use `clickhouse_connect` for all ClickHouse operations.
- Run pre-commit hooks and tests before every commit.

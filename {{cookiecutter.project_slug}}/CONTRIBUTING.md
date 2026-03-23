# Contributing

1. Install dependencies: `uv sync --all-extras`
2. Make your changes.
3. Ensure pre-commit hooks pass: `prek run --all-files`
4. Ensure tests pass with no regression in coverage: `uv run pytest --cov --cov-report=term-missing`
   A coverage report is also posted automatically on each PR.
5. Submit a PR.

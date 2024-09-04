# Cookiecutter Python UV Boilerplate

This project is a cookiecutter template for a Python project using uv.

## Requirements

- [direnv](https://direnv.net/)
- [uv](https://github.com/astral-sh/uv)

## Setup

1. Run the following command to get started:
   ```
   uvx cookiecutter https://github.com/araa47/cookiecutter-python-uv-boilerplate.git
   ```
   This will prompt you for project information (name, description, version) and create a new directory with your project.

2. Navigate to the project directory and run:
   ```
   direnv allow
   ```
   This sets up the environment. See [.envrc]({{cookiecutter.project_slug}}/.envrc) for details.

## Project Features

1. **Environment Management**: [direnv](https://direnv.net/) for automatic environment setup.

2. **Dependency Management**: [uv](https://github.com/astral-sh/uv) for managing Python versions and dependencies, replacing pyenv and poetry.

3. **Code Quality**: [pre-commit](https://pre-commit.com/) for managing pre-commit hooks. See [.pre-commit-config.yaml]({{cookiecutter.project_slug}}/.pre-commit-config.yaml) for configured hooks.

4. **Testing**: [pytest](https://docs.pytest.org/) for writing and running tests.

5. **Continuous Integration**:
   - GitHub Actions for linting, formatting, and testing on pull requests.
   - GitHub Actions for testing on merges to main.

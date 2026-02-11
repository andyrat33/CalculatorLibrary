# CLAUDE.md

## Project Overview
A Python calculator library (`calculator.py`) providing basic math operations as standalone functions: add, subtract, multiply, divide, divide_fl (float division), square, cube, power, mod, square_root, and itob (int to binary).

## Running Tests
```bash
pytest test_calculator.py
```
With coverage: `pytest --cov=calculator test_calculator.py`

## Code Conventions
- Functions are module-level (no classes), using `snake_case` names
- Parameters are named `first_term` and `second_term`
- Division-by-zero is handled by raising `ValueError("Cannot divide by zero")` in `divide`, `divide_fl`, and `mod`
- Tests use a single `TestCalculator` class with pytest

## Tooling
- **Formatter:** Black (via pre-commit)
- **Linter:** Flake8 (via pre-commit)
- **Pre-commit hooks:** check-yaml, end-of-file-fixer, trailing-whitespace, black, flake8
- **CI:** GitHub Actions (pytest), CircleCI, Semgrep

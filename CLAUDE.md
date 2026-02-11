# CLAUDE.md

## Project Overview
A Python calculator library (`calculator.py`) providing basic math operations as standalone functions: add, subtract, multiply, divide, divide_fl (float division), square, cube, power, mod, square_root, and itob (int to binary).

The library is also exposed as a **FastAPI application** (`main.py`) with REST API endpoints.

## Running Tests
```bash
pytest
```
This runs both unit tests (`test_calculator.py`) and API tests (`test_main.py`).

With coverage: `pytest --cov=calculator`

## Running the Server
```bash
uvicorn main:app --reload
```
The API is available at `http://localhost:8000`. Interactive docs at `/docs`.

## API Endpoints
All endpoints return JSON `{"result": <value>}`.

- `GET /health` — health check
- `GET /add?a=<num>&b=<num>`
- `GET /subtract?a=<num>&b=<num>`
- `GET /multiply?a=<num>&b=<num>`
- `GET /divide?a=<num>&b=<num>` — integer division
- `GET /divide_fl?a=<num>&b=<num>` — float division
- `GET /square?a=<num>`
- `GET /cube?a=<num>`
- `GET /power?a=<num>&b=<num>`
- `GET /mod?a=<num>&b=<num>`
- `GET /square_root?a=<num>`
- `GET /itob?a=<int>` — integer to binary string

Division-by-zero on `/divide`, `/divide_fl`, `/mod` returns HTTP 400.

## Code Conventions
- Functions are module-level (no classes), using `snake_case` names
- Parameters are named `first_term` and `second_term`
- Division-by-zero is handled by raising `ValueError("Cannot divide by zero")` in `divide`, `divide_fl`, and `mod`
- Tests use a single `TestCalculator` class (unit) and `TestAPI` class (API) with pytest

## Tooling
- **Formatter:** Black (via pre-commit)
- **Linter:** Flake8 (via pre-commit)
- **Pre-commit hooks:** check-yaml, end-of-file-fixer, trailing-whitespace, black, flake8
- **CI:** GitHub Actions (pytest), CircleCI (pytest + Docker build), Semgrep
- **Container:** Dockerfile using `python:3.12-slim`, runs uvicorn on port 8000

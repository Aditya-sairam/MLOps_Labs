# Git Actions Lab 03

Temperature conversion utility with automated testing.

## Project Structure

- `src/` - Temperature conversion functions
- `tests/` - Test files (pytest and unittest)
- `.github/workflows/` - GitHub Actions CI/CD pipelines

## Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install pytest
```

## Run Tests

**Pytest:**
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest tests/ -v
```

**Unittest:**
```bash
python tests/unit_test.py
```

## GitHub Actions

Tests run automatically on push to main branch. Check the Actions tab to view results.
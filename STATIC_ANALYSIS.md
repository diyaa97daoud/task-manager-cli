# Static Code Analysis Configuration

This directory contains configuration files for static code analysis tools.

## Configuration Files

### setup.cfg

Contains configuration for:

- **Pylint** - Code quality and bug detection
- **Flake8** - PEP 8 style guide enforcement
- **MyPy** - Static type checking
- **Pytest** - Unit testing framework

### pyproject.toml

Contains configuration for:

- **Black** - Code formatter

### .pre-commit-config.yaml

Contains configuration for:

- Pre-commit hooks that run all static analysis tools automatically

## How to Install Static Analysis Tools

All tools are included in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

## How to Run Static Analysis

### Method 1: Run All Tools at Once

**Windows PowerShell:**

```powershell
.\run_analysis.ps1
```

**Linux/Mac:**

```bash
chmod +x run_analysis.sh
./run_analysis.sh
```

### Method 2: Run Individual Tools

```bash
# Black - Code formatter (check mode)
black --check src/ tests/

# Black - Code formatter (fix mode)
black src/ tests/

# Flake8 - Style checker
flake8 src/ tests/

# Pylint - Code quality analyzer
pylint src/ tests/

# MyPy - Type checker
mypy src/
```

## Tool Descriptions

### Black

**Purpose:** Automatic code formatting

- Ensures consistent code style across the project
- Configured for 100 character line length
- No debates about formatting - it just works!

**Example:**

```bash
black src/
```

### Flake8

**Purpose:** PEP 8 style guide enforcement

- Checks for style violations
- Identifies unused imports
- Detects undefined names
- Measures code complexity

**Example:**

```bash
flake8 src/
```

### Pylint

**Purpose:** Comprehensive code analysis

- Code quality metrics
- Bug detection
- Refactoring suggestions
- Convention enforcement

**Example:**

```bash
pylint src/task_manager.py
```

### MyPy

**Purpose:** Static type checking

- Verifies type hints
- Catches type-related bugs before runtime
- Improves code reliability

**Example:**

```bash
mypy src/
```

## Understanding the Output

### Black Output

- **"All done! ✨ 🍰 ✨"** - Code is properly formatted
- **"would reformat"** - Code needs formatting (use `black src/` to fix)

### Flake8 Output

Format: `filename:line:column: code message`

Example:

```
src/cli.py:45:1: E302 expected 2 blank lines, found 1
```

Common codes:

- E### - PEP 8 errors
- W### - PEP 8 warnings
- F### - PyFlakes errors
- C901 - Complexity too high

### Pylint Output

Rating: x.xx/10.00

Format: `filename:line:column: code: message`

Example:

```
src/task_manager.py:15:0: C0301: Line too long (105/100) (line-too-long)
```

### MyPy Output

Format: `filename:line: error: message`

Example:

```
src/task_manager.py:25: error: Incompatible return value type
```

## Fixing Common Issues

### "Line too long"

Split long lines or use parentheses for continuation:

```python
# Before
result = some_function(arg1, arg2, arg3, arg4, arg5, arg6)

# After
result = some_function(
    arg1, arg2, arg3,
    arg4, arg5, arg6
)
```

### "Missing docstring"

Add docstrings to modules, classes, and functions:

```python
def my_function(arg):
    """Brief description of what the function does."""
    pass
```

### "Type hint missing"

Add type hints to function signatures:

```python
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

## Integration with Development Workflow

1. Write code
2. Run static analysis: `.\run_analysis.ps1`
3. Fix any issues reported
4. Run again until all checks pass
5. Commit code (pre-commit hooks will run automatically)

## Continuous Integration

These tools can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run Static Analysis
  run: |
    pip install -r requirements.txt
    black --check src/ tests/
    flake8 src/ tests/
    pylint src/ tests/
    mypy src/
```

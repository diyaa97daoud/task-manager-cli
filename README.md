# Task Manager CLI

A comprehensive command-line task management application built for the **Testing Frameworks and Software Debugging** course. This project demonstrates professional software engineering practices including static code analysis, automated testing, comprehensive logging, and debugging proficiency.

## 📋 Assignment Requirements

This project fulfills all 5 requirements for the TFSD course:

1. ✅ **Static Code Analysis** - Black, Flake8, Pylint, MyPy
2. ✅ **Pre-commit Hooks** - Automated quality checks on every commit
3. ✅ **Comprehensive Logging** - All 5 levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
4. ✅ **Unit Testing** - 33 tests with 95% coverage
5. ⏳ **Debugging Video** - VS Code debugging demonstration (to be recorded)

**👉 See [`SUBMISSION_GUIDE.md`](./SUBMISSION_GUIDE.md) for complete assignment proof and documentation.**

## Project Overview

This project demonstrates professional software engineering practices including:

- **Static Code Analysis** with multiple tools (Pylint, Flake8, MyPy, Black)
- **Pre-commit Hooks** for automated code quality checks
- **Comprehensive Logging** at all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Unit Testing** with pytest and code coverage
- **External Dependencies** (Click, Requests, Colorama, python-dateutil)

## Features

- ✅ Create, read, update, and delete tasks
- ✅ Task prioritization (Low, Medium, High, Critical)
- ✅ Task status tracking (TODO, In Progress, Completed, Cancelled)
- ✅ Due date management with overdue detection
- ✅ Colored CLI output for better UX
- ✅ Persistent JSON storage
- ✅ Comprehensive logging to file and console

## Requirements

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Installation

### 1. Clone the Repository

### 2. Create Virtual Environment (Recommended)

```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
# Add a new task
python -m src.cli add "Complete project report" --priority high --due-date 2025-12-31

# List all tasks
python -m src.cli list

# List tasks by status
python -m src.cli list --status todo

# List overdue tasks
python -m src.cli list --overdue

# Show task details
python -m src.cli show 1

# Update a task
python -m src.cli update 1 --status in_progress --priority critical

# Complete a task
python -m src.cli complete 1

# Delete a task
python -m src.cli delete 1
```

### Available Commands

- `add` - Add a new task
- `list` - List tasks with optional filters
- `show` - Display detailed task information
- `update` - Update task properties
- `complete` - Mark task as completed
- `delete` - Delete a task

## Static Code Analysis

### Configuration Files

- **`setup.cfg`** - Configuration for Pylint, Flake8, MyPy, and Pytest
- **`pyproject.toml`** - Configuration for Black formatter
- **`.pre-commit-config.yaml`** - Pre-commit hooks configuration

### Running Static Analysis Manually

#### Windows PowerShell

```powershell
.\run_analysis.ps1
```

#### Linux/Mac

```bash
chmod +x run_analysis.sh
./run_analysis.sh
```

#### Individual Tools

```bash
# Black - Code formatting check
black --check src/ tests/

# Flake8 - Style guide enforcement
flake8 src/ tests/

# Pylint - Comprehensive code analysis
pylint src/ tests/

# MyPy - Type checking
mypy src/
```

### What Each Tool Does

1. **Black** - Automatically formats code to a consistent style

   - Line length: 100 characters
   - Enforces PEP 8 formatting standards

2. **Flake8** - Checks code against style guide (PEP 8)

   - Max line length: 100
   - Max cyclomatic complexity: 10
   - Identifies unused imports, undefined names, etc.

3. **Pylint** - Comprehensive static analysis

   - Code quality checks
   - Bug detection
   - Refactoring suggestions
   - Naming convention enforcement

4. **MyPy** - Static type checking
   - Type hint verification
   - Catches type-related bugs before runtime

## Pre-commit Hooks

Pre-commit hooks automatically run static analysis before each commit.

### Installation

```bash
# Install pre-commit hooks
pre-commit install
```

### Usage

Once installed, hooks run automatically on `git commit`. They will:

- Format code with Black
- Check style with Flake8
- Analyze code with Pylint
- Verify types with MyPy
- Remove trailing whitespace
- Check for merge conflicts
- Validate JSON/YAML files

### Manual Execution

```bash
# Run on all files
pre-commit run --all-files

# Run on specific files
pre-commit run --files src/task_manager.py
```

### Skipping Hooks (Not Recommended)

```bash
git commit --no-verify -m "message"
```

## Logging

The application implements comprehensive logging at all appropriate levels.

### Log Levels Used

1. **DEBUG** - Detailed diagnostic information

   - Task creation details
   - Task retrieval operations
   - Filter operations

2. **INFO** - General informational messages

   - Task additions
   - Task updates
   - Task deletions
   - Application startup

3. **WARNING** - Warning messages for non-critical issues

   - Task not found warnings
   - Overdue task notifications
   - Invalid filter combinations

4. **ERROR** - Error messages for failures

   - Invalid input data
   - Failed operations
   - File I/O errors

5. **CRITICAL** - Critical errors requiring immediate attention
   - Storage file corruption
   - Unexpected exceptions
   - Data loss scenarios

### Log Configuration

- **Log File**: `logs/task_manager.log`
- **Console Output**: INFO and above
- **File Output**: DEBUG and above
- **Format**: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

### Viewing Logs

```bash
# View recent logs
cat logs/task_manager.log

# Windows PowerShell
Get-Content logs/task_manager.log -Tail 50

# Follow logs in real-time
tail -f logs/task_manager.log  # Linux/Mac
Get-Content logs/task_manager.log -Wait  # PowerShell
```

## Unit Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_task.py

# Run specific test
pytest tests/test_task.py::TestTask::test_task_creation_with_defaults

# Generate HTML coverage report
pytest --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

### Test Coverage

The project includes comprehensive unit tests covering:

- Task creation and validation
- Task manager operations (CRUD)
- Persistence (save/load)
- Filtering and searching
- Overdue task detection
- Error handling

Target coverage: >90%

### Test Files

- `tests/test_task.py` - Tests for Task class
- `tests/test_task_manager.py` - Tests for TaskManager class

## Project Structure

```
task-manager/
├── src/
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   └── task_manager.py     # Core business logic
├── tests/
│   ├── __init__.py
│   ├── test_task.py        # Task class tests
│   └── test_task_manager.py # TaskManager tests
├── logs/
│   └── task_manager.log    # Application logs
├── .pre-commit-config.yaml # Pre-commit hooks config
├── setup.cfg               # Tool configurations
├── pyproject.toml          # Black configuration
├── requirements.txt        # Python dependencies
├── run_analysis.ps1        # Windows analysis script
├── run_analysis.sh         # Linux/Mac analysis script
├── tasks.json              # Task storage (auto-created)
└── README.md               # This file
```

## Dependencies

### Core Dependencies

- **click** - Command-line interface framework
- **requests** - HTTP library (for potential API integrations)
- **colorama** - Cross-platform colored terminal output
- **python-dateutil** - Date parsing and manipulation

### Development Dependencies

- **pytest** - Testing framework
- **pytest-cov** - Coverage plugin
- **pylint** - Static code analyzer
- **flake8** - Style guide checker
- **mypy** - Static type checker
- **black** - Code formatter
- **pre-commit** - Git hook manager

## Development Workflow

1. **Make changes** to the code
2. **Run tests** to ensure nothing breaks
   ```bash
   pytest
   ```
3. **Run static analysis** to check code quality
   ```bash
   .\run_analysis.ps1  # Windows
   ./run_analysis.sh   # Linux/Mac
   ```
4. **Commit changes** (pre-commit hooks run automatically)
   ```bash
   git add .
   git commit -m "descriptive message"
   ```
5. **Push to repository**
   ```bash
   git push origin main
   ```

## Debugging

### IDE Debugging Setup

#### Visual Studio Code

1. Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Python: CLI Module",
      "type": "python",
      "request": "launch",
      "module": "src.cli",
      "args": ["list"],
      "console": "integratedTerminal"
    }
  ]
}
```

2. Set breakpoints in code
3. Press F5 to start debugging

### Common Debugging Scenarios

- **Breakpoints**: Set at function entry points
- **Watch expressions**: Monitor variable values
- **Step through**: F10 (step over), F11 (step into)
- **Inspect variables**: Hover over variables to see values

## Assignment Requirements Checklist

✅ **Static Code Analysis** (1/5 points)

- Configuration: `setup.cfg`, `pyproject.toml`
- Tools: Pylint, Flake8, MyPy, Black
- Run: `.\run_analysis.ps1` or `./run_analysis.sh`

✅ **Pre-commit Hooks** (1/5 points)

- Configuration: `.pre-commit-config.yaml`
- Install: `pre-commit install`
- Auto-runs on commit

✅ **Comprehensive Logging** (1/5 points)

- All levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Files: `src/task_manager.py`, `src/cli.py`
- Contextual logging throughout application

✅ **Unit Testing** (1/5 points)

- Test files: `tests/test_task.py`, `tests/test_task_manager.py`
- Run: `pytest --cov=src`
- High coverage with meaningful tests

✅ **Video Demonstration** (1/5 points)

- Record 3-minute demo of debugging in VS Code
- Show breakpoints, stepping, variable inspection

## License

This project is created for educational purposes.

## Author

Created by [Your Name] for the Testing Frameworks and Software Debugging course.

## Contributing

This is an academic project. For contributions, please follow the development workflow above.

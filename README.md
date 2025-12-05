# Task Manager CLI

A comprehensive command-line task management application built for the **Testing Frameworks and Software Debugging**. This project demonstrates professional software engineering practices including static code analysis, automated testing, comprehensive logging, and debugging proficiency.

## 📋 Assignment Requirements

This project fulfills all 5 requirements for the TFSD course:

**See [`SUBMISSION_GUIDE.md`](./SUBMISSION_GUIDE.md) for complete assignment proof and documentation.**

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

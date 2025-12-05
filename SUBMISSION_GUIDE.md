## Assignment Requirements - Complete Checklist

### **Requirement 1/5: Static Code Analysis**

**Configuration Files:**

- [`setup.cfg`](./setup.cfg) - Configuration for Pylint, Flake8, MyPy, and Pytest
- [`pyproject.toml`](./pyproject.toml) - Configuration for Black code formatter
- [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) - Pre-commit hooks configuration

**Documentation:**

- [`STATIC_ANALYSIS.md`](./STATIC_ANALYSIS.md) - Complete guide on static analysis tools

**How to Install and Run:**

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run all static analysis tools
# Windows PowerShell:
.\run_analysis.ps1

# Linux/Mac:
chmod +x run_analysis.sh
./run_analysis.sh

# 3. Run individual tools
black --check src/ tests/     # Code formatter
flake8 src/ tests/            # Style checker
pylint src/ tests/            # Code quality analyzer
mypy src/                     # Type checker
```

**Tools Used:**

- **Black** - Code formatting
- **Flake8** - PEP 8 style guide enforcement
- **Pylint** - Comprehensive code quality analysis
- **MyPy** - Static type checking

**Proof:** See configuration files and run scripts in the repository root.

---

### **Requirement 2/5: Pre-commit Hooks**

**Configuration File:**

- [`.pre-commit-config.yaml`](./.pre-commit-config.yaml)

**Documentation:**

- [`PRECOMMIT_SETUP.md`](./PRECOMMIT_SETUP.md) - Complete setup and usage guide

**How to Set Up:**

```bash
# 1. Install pre-commit framework
pip install pre-commit

# 2. Install git hooks
pre-commit install

# 3. Test the hooks
pre-commit run --all-files
```

**What Gets Automated:**

- Black code formatting
- Flake8 style checks
- Pylint code quality checks
- MyPy type checking
- Trailing whitespace removal
- YAML/JSON validation
- Merge conflict detection

**Proof:**

- Configuration: [`.pre-commit-config.yaml`](./.pre-commit-config.yaml)
- Initial commit shows all hooks passed
- Every commit triggers automatic analysis

---

### **Requirement 3/5: Relevant Logging (All 5 Levels)**

**Files with Logging:**

- [`src/task_manager.py`](./src/task_manager.py) - Core business logic logging
- [`src/cli.py`](./src/cli.py) - CLI interface logging

**All 5 Log Levels Used Contextually:**

1. **DEBUG** - Detailed diagnostic information

   - `logger.debug("Task created: id=%s, title='%s', priority=%s", ...)`
   - `logger.debug("Task found: id=%d", task_id)`
   - `logger.debug("Saved %d tasks to storage", len(self.tasks))`
   - Used for: Task creation details, database operations, filter operations

2. **INFO** - General informational messages

   - `logger.info("TaskManager initialized with storage: %s", ...)`
   - `logger.info("Task added: id=%d, title='%s'", ...)`
   - `logger.info("Task %d status changed: %s -> %s", ...)`
   - Used for: Application startup, successful operations, state changes

3. **WARNING** - Warning messages for concerning situations

   - `logger.warning("Task %s ('%s') is overdue! Due: %s", ...)`
   - `logger.warning("Task not found: id=%d", task_id)`
   - `logger.warning("Found %d overdue tasks", len(overdue))`
   - Used for: Overdue tasks, missing resources, potential issues

4. **ERROR** - Error messages for failures

   - `logger.error("Attempted to create task with empty title")`
   - `logger.error("Cannot update task %d: task not found", ...)`
   - `logger.error("Failed to parse JSON from %s: %s", ...)`
   - Used for: Invalid input, failed operations, recoverable errors

5. **CRITICAL** - Critical errors requiring immediate attention
   - `logger.critical("Unexpected error loading tasks from %s: %s", ...)`
   - `logger.critical("Failed to write to %s: %s", ...)`
   - `logger.critical("Unexpected error adding task: %s", ...)`
   - Used for: Data corruption, system failures, unrecoverable errors

**Log Configuration:**

- Log file: `logs/task_manager.log`
- Console output: INFO level and above
- File output: DEBUG level and above (everything)
- Format: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`

**Proof:**

- Commit link: Initial commit with all logging implemented
- Files: [`src/task_manager.py`](./src/task_manager.py) and [`src/cli.py`](./src/cli.py)

---

### **Requirement 4/5: Unit Testing**

**Test Files:**

- [`tests/test_task.py`](./tests/test_task.py) - Task class unit tests (11 tests)
- [`tests/test_task_manager.py`](./tests/test_task_manager.py) - TaskManager class unit tests (22 tests)

**Test Statistics:**

- **Total Tests:** 33
- **Passing:** 33 (100%)
- **Code Coverage:** 95% on core logic
- **Test Framework:** pytest with pytest-cov

**How to Run:**

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/test_task.py

# Generate HTML coverage report
pytest --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

**Test Coverage Areas:**

- Task creation and validation
- Task CRUD operations (Create, Read, Update, Delete)
- Data persistence (save/load)
- Filtering and searching
- Overdue task detection
- Error handling and edge cases
- Input validation

**Example Tests:**

- `test_task_creation_with_defaults()` - Verify default values
- `test_task_creation_empty_title_raises_error()` - Input validation
- `test_is_overdue_past_date()` - Business logic
- `test_persistence_save_and_load()` - Data persistence
- `test_update_task_multiple_fields()` - Complex operations

**Proof:**

- Commit link: Initial commit with complete test suite
- Files: [`tests/test_task.py`](./tests/test_task.py) and [`tests/test_task_manager.py`](./tests/test_task_manager.py)

---

### 🎥 **Requirement 5/5: Debugging Video**

**Video Content (3 minutes max):**

1. Setting breakpoints in VS Code
2. Starting debug session
3. Stepping through code (step over, step into, step out)
4. Inspecting variables and expressions
5. Using watch expressions
6. Evaluating expressions in debug console
7. Demonstrating conditional breakpoints

**Files to Debug:**

- `src/task_manager.py` - Set breakpoints in `add_task()`, `is_overdue()`
- `src/cli.py` - Set breakpoints in command handlers

**Video Link:** [To be recorded and uploaded]

---

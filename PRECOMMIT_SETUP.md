# Pre-commit Hooks Setup and Configuration

This document explains how to set up and use pre-commit hooks for automated static code analysis.

## What are Pre-commit Hooks?

Pre-commit hooks are scripts that run automatically before each git commit. They help maintain code quality by:

- Running static analysis tools
- Formatting code automatically
- Preventing commits with issues
- Saving time in code reviews

## Installation

### Step 1: Install Dependencies

Make sure you have installed all requirements:

```bash
pip install -r requirements.txt
```

This includes the `pre-commit` package.

### Step 2: Install Git Hooks

Run this command in your project root:

```bash
pre-commit install
```

This installs the hooks into your `.git/hooks/` directory.

**Expected Output:**

```
pre-commit installed at .git/hooks/pre-commit
```

## Configuration

The configuration is in `.pre-commit-config.yaml`:

```yaml
repos:
  # Black - Code Formatter
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3
        args: ["--line-length=100"]

  # Flake8 - Style Guide Enforcement
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ["--max-line-length=100", "--max-complexity=10"]

  # Pylint - Code Quality
  - repo: https://github.com/pycqa/pylint
    rev: v3.0.3
    hooks:
      - id: pylint
        args: ["--max-line-length=100"]

  # MyPy - Type Checking
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-python-dateutil]

  # Additional hooks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace # Remove trailing whitespace
      - id: end-of-file-fixer # Ensure files end with newline
      - id: check-yaml # Validate YAML files
      - id: check-added-large-files # Prevent large files
      - id: check-json # Validate JSON files
      - id: check-merge-conflict # Detect merge conflict markers
      - id: detect-private-key # Detect private keys
```

## Usage

### Automatic Execution

Once installed, hooks run automatically when you commit:

```bash
git add .
git commit -m "Your commit message"
```

**What happens:**

1. Git stages your changes
2. Pre-commit hooks run on staged files
3. If all checks pass, commit proceeds
4. If any check fails, commit is blocked

**Example successful output:**

```
black....................................................................Passed
flake8...................................................................Passed
pylint...................................................................Passed
mypy.....................................................................Passed
trailing-whitespace......................................................Passed
end-of-file-fixer........................................................Passed
check-yaml...............................................................Passed
[main abc123] Your commit message
 2 files changed, 10 insertions(+)
```

**Example failed output:**

```
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted src/task_manager.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

### Manual Execution

You can run hooks manually without committing:

```bash
# Run on all files
pre-commit run --all-files

# Run on specific files
pre-commit run --files src/task_manager.py

# Run specific hook
pre-commit run black --all-files
```

### First Time Setup

After installation, run hooks on all files:

```bash
pre-commit run --all-files
```

This ensures all existing code passes the checks.

## Hooks Explained

### 1. Black (Formatter)

- **What it does:** Automatically formats Python code
- **When it runs:** On Python files
- **Auto-fix:** Yes (modifies files)
- **Action if failed:** Review changes, add files, commit again

### 2. Flake8 (Style Checker)

- **What it does:** Checks PEP 8 style violations
- **When it runs:** On Python files
- **Auto-fix:** No
- **Action if failed:** Manually fix issues, commit again

### 3. Pylint (Code Analyzer)

- **What it does:** Comprehensive code quality checks
- **When it runs:** On Python files
- **Auto-fix:** No
- **Action if failed:** Fix issues based on messages

### 4. MyPy (Type Checker)

- **What it does:** Verifies type hints
- **When it runs:** On Python files
- **Auto-fix:** No
- **Action if failed:** Fix type issues

### 5. Trailing Whitespace

- **What it does:** Removes trailing spaces
- **Auto-fix:** Yes

### 6. End of File Fixer

- **What it does:** Ensures files end with newline
- **Auto-fix:** Yes

### 7. Check YAML

- **What it does:** Validates YAML syntax
- **Auto-fix:** No

### 8. Check JSON

- **What it does:** Validates JSON syntax
- **Auto-fix:** No

### 9. Check Merge Conflict

- **What it does:** Detects merge conflict markers
- **Auto-fix:** No

### 10. Detect Private Key

- **What it does:** Prevents committing private keys
- **Auto-fix:** No

## Workflow Example

### Scenario 1: All Checks Pass

```bash
# Make changes
echo "def hello(): print('world')" > src/new_feature.py

# Stage changes
git add src/new_feature.py

# Commit (hooks run automatically)
git commit -m "Add new feature"

# Output: All hooks pass, commit succeeds
```

### Scenario 2: Black Reformats Code

```bash
# Make changes (poorly formatted)
echo "def hello(  ):print(  'world' )" > src/new_feature.py

# Try to commit
git add src/new_feature.py
git commit -m "Add new feature"

# Output: Black fails, reformats file
# Action required: Re-add the formatted file
git add src/new_feature.py
git commit -m "Add new feature"

# Now commit succeeds
```

### Scenario 3: Style Violation

```bash
# Make changes with style violation
echo "x=1" > src/bad_style.py  # Missing spaces around =

# Try to commit
git add src/bad_style.py
git commit -m "Add feature"

# Output: Flake8 fails
# src/bad_style.py:1:2: E225 missing whitespace around operator

# Fix the issue
echo "x = 1" > src/bad_style.py

# Commit again
git add src/bad_style.py
git commit -m "Add feature"

# Now commit succeeds
```

## Skipping Hooks (NOT RECOMMENDED)

In rare cases, you might need to skip hooks:

```bash
# Skip all hooks
git commit --no-verify -m "Emergency fix"

# Skip specific hook
SKIP=pylint git commit -m "Skip pylint only"
```

**⚠️ Warning:** Only skip hooks if absolutely necessary. It defeats the purpose of automated quality checks.

## Updating Hooks

To update hook versions:

```bash
# Update to latest versions
pre-commit autoupdate

# Then commit the updated config
git add .pre-commit-config.yaml
git commit -m "Update pre-commit hooks"
```

## Troubleshooting

### Hooks Not Running

**Problem:** Hooks don't run on commit

**Solution:**

```bash
# Reinstall hooks
pre-commit uninstall
pre-commit install
```

### Hook Installation Failed

**Problem:** Error during `pre-commit install`

**Solution:**

```bash
# Ensure pre-commit is installed
pip install pre-commit

# Try installation again
pre-commit install
```

### Specific Hook Always Fails

**Problem:** One hook consistently fails

**Solution:**

```bash
# Run the hook manually to see detailed output
pre-commit run <hook-name> --all-files

# Example
pre-commit run pylint --all-files
```

### Performance Issues

**Problem:** Hooks take too long

**Solution:**

- Hooks only run on changed files by default
- Use `--files` to run on specific files
- Consider disabling expensive hooks for large projects

## CI/CD Integration

Pre-commit can also run in CI/CD:

```yaml
# GitHub Actions example
name: Pre-commit
on: [push, pull_request]
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - uses: pre-commit/action@v2.0.0
```

## Benefits

✅ **Automatic Quality Checks** - No manual running of tools
✅ **Consistent Code Style** - All code follows same standards
✅ **Early Error Detection** - Catch issues before they reach repository
✅ **Reduced Review Time** - Automated checks reduce manual review load
✅ **Learning Tool** - Developers learn best practices from feedback

## Best Practices

1. **Install hooks immediately** after cloning repository
2. **Run hooks on all files** initially to clean up codebase
3. **Don't skip hooks** unless absolutely necessary
4. **Update hooks regularly** to get latest improvements
5. **Keep hook configuration in version control** (`.pre-commit-config.yaml`)

## Additional Resources

- [Pre-commit Official Documentation](https://pre-commit.com/)
- [Supported Hooks](https://pre-commit.com/hooks.html)
- [Creating Custom Hooks](https://pre-commit.com/#creating-new-hooks)

## Proof of Setup

To prove pre-commit hooks are properly configured:

1. File `.pre-commit-config.yaml` exists in repository root
2. Run `pre-commit run --all-files` and show output
3. Make a commit and show hooks executing
4. Screenshot of hooks in action (for assignment submission)

## For Assignment Submission

**Configuration File:** `.pre-commit-config.yaml` (link to this file in your repository)

**Installation Instructions:**

```bash
pip install -r requirements.txt
pre-commit install
```

**Verification:**

```bash
pre-commit run --all-files
```

This demonstrates fully automated static code analysis on every commit! ✅

#!/usr/bin/env bash
# Static Code Analysis Script
# This script runs all configured static analysis tools

echo "Running Static Code Analysis..."
echo "================================"

# Track if any checks fail
FAILED=0

# Run Black (code formatter check)
echo ""
echo "1. Running Black (Code Formatter)..."
black --check src/ tests/ || FAILED=1

# Run Flake8 (style guide enforcement)
echo ""
echo "2. Running Flake8 (Style Checker)..."
flake8 src/ tests/ || FAILED=1

# Run Pylint (comprehensive code analysis)
echo ""
echo "3. Running Pylint (Code Quality)..."
pylint src/ tests/ || FAILED=1

# Run MyPy (type checking)
echo ""
echo "4. Running MyPy (Type Checker)..."
mypy src/ || FAILED=1

echo ""
echo "================================"
if [ $FAILED -eq 0 ]; then
    echo "✓ All static analysis checks passed!"
    exit 0
else
    echo "✗ Some static analysis checks failed!"
    exit 1
fi

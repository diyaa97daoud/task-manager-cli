# Static Code Analysis Script for Windows PowerShell
# This script runs all configured static analysis tools

Write-Host "Running Static Code Analysis..." -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

# Track if any checks fail
$Failed = $false

# Run Black (code formatter check)
Write-Host ""
Write-Host "1. Running Black (Code Formatter)..." -ForegroundColor Yellow
black --check src/ tests/
if ($LASTEXITCODE -ne 0) { $Failed = $true }

# Run Flake8 (style guide enforcement)
Write-Host ""
Write-Host "2. Running Flake8 (Style Checker)..." -ForegroundColor Yellow
flake8 src/ tests/
if ($LASTEXITCODE -ne 0) { $Failed = $true }

# Run Pylint (comprehensive code analysis)
Write-Host ""
Write-Host "3. Running Pylint (Code Quality)..." -ForegroundColor Yellow
pylint src/ tests/
if ($LASTEXITCODE -ne 0) { $Failed = $true }

# Run MyPy (type checking)
Write-Host ""
Write-Host "4. Running MyPy (Type Checker)..." -ForegroundColor Yellow
mypy src/
if ($LASTEXITCODE -ne 0) { $Failed = $true }

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
if (-not $Failed) {
    Write-Host "✓ All static analysis checks passed!" -ForegroundColor Green
    exit 0
} else {
    Write-Host "✗ Some static analysis checks failed!" -ForegroundColor Red
    exit 1
}

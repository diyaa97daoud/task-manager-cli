# 🎯 Quick Assignment Reference

**Repository:** https://github.com/diyaa97daoud/task-manager-cli

## ✅ Assignment Requirements - Quick Links

### 1/5: Static Code Analysis

- **Config:** [setup.cfg](https://github.com/diyaa97daoud/task-manager-cli/blob/main/setup.cfg) | [pyproject.toml](https://github.com/diyaa97daoud/task-manager-cli/blob/main/pyproject.toml)
- **Script:** [run_analysis.ps1](https://github.com/diyaa97daoud/task-manager-cli/blob/main/run_analysis.ps1)
- **Docs:** [STATIC_ANALYSIS.md](https://github.com/diyaa97daoud/task-manager-cli/blob/main/STATIC_ANALYSIS.md)

### 2/5: Pre-commit Hooks

- **Config:** [.pre-commit-config.yaml](https://github.com/diyaa97daoud/task-manager-cli/blob/main/.pre-commit-config.yaml)
- **Docs:** [PRECOMMIT_SETUP.md](https://github.com/diyaa97daoud/task-manager-cli/blob/main/PRECOMMIT_SETUP.md)

### 3/5: Logging (All 5 Levels)

- **Files:** [src/task_manager.py](https://github.com/diyaa97daoud/task-manager-cli/blob/main/src/task_manager.py) | [src/cli.py](https://github.com/diyaa97daoud/task-manager-cli/blob/main/src/cli.py)
- **Commit:** [f6aae40](https://github.com/diyaa97daoud/task-manager-cli/commit/f6aae40)

### 4/5: Unit Testing

- **Tests:** [tests/test_task.py](https://github.com/diyaa97daoud/task-manager-cli/blob/main/tests/test_task.py) | [tests/test_task_manager.py](https://github.com/diyaa97daoud/task-manager-cli/blob/main/tests/test_task_manager.py)
- **Coverage:** 95% (33 tests, all passing)
- **Commit:** [f6aae40](https://github.com/diyaa97daoud/task-manager-cli/commit/f6aae40)

### 5/5: Debugging Video

- **Guide:** [DEBUGGING_VIDEO_GUIDE.md](https://github.com/diyaa97daoud/task-manager-cli/blob/main/DEBUGGING_VIDEO_GUIDE.md)
- **Configs:** [.vscode/launch.json](https://github.com/diyaa97daoud/task-manager-cli/blob/main/.vscode/launch.json)
- **Video:** [To be recorded]

## 📚 Full Documentation

See [SUBMISSION_GUIDE.md](https://github.com/diyaa97daoud/task-manager-cli/blob/main/SUBMISSION_GUIDE.md) for complete details.

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/diyaa97daoud/task-manager-cli.git
cd task-manager-cli

# Setup
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

# Run Tests
pytest --cov=src

# Run Static Analysis
.\run_analysis.ps1

# Install Pre-commit
pre-commit install
```

## 📊 Project Stats

- **Language:** Python 3.9+
- **Lines of Code:** 300+ (production)
- **Tests:** 33 (100% passing)
- **Coverage:** 95%
- **Commits:** 4 meaningful commits
- **Documentation:** 6 comprehensive guides

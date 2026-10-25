# Contributing & Git Workflow Guide

Welcome to the Team Apsara practice repository!
This repository is used by teammates to practice everyday Git operations (cloning, branching, committing, and opening Pull Requests).

---

## 1. Daily Git Workflow

### Step 1: Always Pull Latest Changes
Before starting any work, update your local `main` branch:
```bash
git checkout main
git pull origin main
```

### Step 2: Create a Feature Branch
Never commit directly to `main`. Create a new branch named after your task or your name:
```bash
git checkout -b feature/yourname-exercise1
```

### Step 3: Make Your Code Edits
Open the practice files in your editor (VS Code, Antigravity, PyCharm, etc.) and complete the exercise tasks.

### Step 4: Check Status and Diff
See what files you modified:
```bash
git status
git diff
```

### Step 5: Stage and Commit
Write clear, meaningful commit messages:
```bash
git add exercise_1_hello_drone.py
git commit -m "feat(ex1): add sensor check to subsystems dictionary"
```

### Step 6: Push Your Branch
Push your branch to GitHub:
```bash
git push -u origin feature/yourname-exercise1
```

### Step 7: Open a Pull Request (PR)
1. Go to https://github.com/SoSereysokbotra/kibo-rpc-7th-apsara-practice
2. Click **Compare & pull request**.
3. Ask a teammate or your teacher to review and approve!

---

## 2. Commit Message Guidelines
Use clear prefixes for your commit messages:
* `feat:` A new feature or exercise implementation.
* `fix:` A bug fix.
* `docs:` Documentation updates.
* `style:` Formatting or whitespace changes.
* `refactor:` Code cleanup without changing functionality.
* `test:` Adding or updating tests.

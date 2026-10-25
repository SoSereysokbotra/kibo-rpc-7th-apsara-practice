# Git Cheatsheet for Space Robotics Practice

A quick reference card of the most commonly used Git commands.

---

## 1. Inspecting State
* `git status` — Check which files are modified, staged, or untracked.
* `git log --oneline -n 10` — View the last 10 commits concisely.
* `git diff` — View unstaged changes in your working tree.
* `git diff --staged` — View changes that are staged for the next commit.

## 2. Working with Branches
* `git branch` — List all local branches.
* `git checkout -b <branch-name>` — Create a new branch and switch to it.
* `git switch <branch-name>` — Switch to an existing branch.
* `git branch -d <branch-name>` — Safely delete a branch that has been merged.

## 3. Staging and Committing
* `git add <file>` — Stage a specific file.
* `git add .` — Stage all modified and untracked files in current folder.
* `git commit -m "your message"` — Record a commit with a message.
* `git commit --amend` — Modify the most recent commit message.

## 4. Syncing with Remote
* `git fetch origin` — Fetch latest remote commits without merging.
* `git pull origin main` — Pull and merge remote main into your current branch.
* `git push origin <branch-name>` — Push your local branch to GitHub.

## 5. Undoing Mistakes Safely
* `git restore <file>` — Discard uncommitted changes in a specific file.
* `git stash` — Temporarily save uncommitted changes to a clean slate.
* `git stash pop` — Restore your stashed changes.

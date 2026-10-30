# Repository Reference Guide

> **Summary** Reference Commands for Git Operations

---


## Table of Contents

-[1. Basic Operations](#1-basic-operations)
-[2. Undoing Changes](#2-undoing-changes)
-[3. Remote Synchronization](#3-remote-synchronization)

---

## 1. Basic Operations

Standard workflow for staging and committing changes.

* **`git status`**  
  Inspect tracked/untracked file states.
* **`git add .`**  
  Stage all modified and new files.
* **`git commit -m "message"`**  
  Create a new commit snapshot.

--- 2. Undoing Changes


Options for modifying history and working directory state.

### Soft Reset

Keeps file changes staged in the index.

```bash
git reset --soft HEAD~1
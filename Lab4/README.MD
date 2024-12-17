# Lab 4: Creating a Python Package

This lab demonstrates how to create Python packages, organize modules, and verify their functionality to improve code organization and reusability.

## Objectives

- Create a module named `basic`.
- Add two functions to the module `basic`.
- Create a module named `stats`.
- Add two functions to the module `stats`.
- Create a Python package named `mymath`.
- Verify that the package is working.

---

## Tasks

### Task 1: Set-up
- Clone the repository containing the lab artifacts.
- Navigate to the directory with the exercise files.

### Task 2: Create the `basic` Module
- Create a new Python file named `basic.py` inside a directory named `mymath`.
- Add the following functions to `basic.py`:
  ```python
  # mymath/basic.py

  def add(a, b):
      return a + b
  
  def subtract(a, b):
      return a - b

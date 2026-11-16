# Python Fundamentals Assignment

This repository contains solutions to the Python Fundamentals assignment, arranged topic-wise.

## Folder structure

```text
python_fundamentals_assignment/
│
├── 01_conditional_statements.py
├── 02_loops.py
├── 03_strings.py
├── 04_data_structures.py
├── 05_functions_recursion.py
├── 06_error_exception.py
├── 07_modules_packages.py
├── 07_geometry_test.py
├── 08_object_oriented_programming.py
└── geometry/
    ├── __init__.py
    ├── circle.py
    └── rectangle.py
```

## Requirements

- Python 3.10 or later (the programs use standard Python libraries only).
- No third-party packages are needed.

## How to run

Open a terminal in this folder and run one file at a time:

```bash
python 01_conditional_statements.py
python 02_loops.py
python 03_strings.py
python 04_data_structures.py
python 05_functions_recursion.py
python 06_error_exception.py
python 07_modules_packages.py
python 07_geometry_test.py
python 08_object_oriented_programming.py
```

On some systems, use `python3` instead of `python`.

The geometry test file imports `circle.py` and `rectangle.py` from the `geometry` package. Run it from the main assignment folder so Python can find that package.

## Notes

- Each topic file contains the exercises from that section of the assignment.
- Some questions use sample values to demonstrate the logic; you can change those values and test again.
- The loan assignment does not define exact conditions for conditional approval. In this solution, the middle range (salary at least Rs. 25,000 and credit score at least 650, with age 21–60) is treated as conditional approval. Confirm this interpretation with your teacher if a specific rule was given in class.
- For the exam result question, division is printed only for the ranges specified in the assignment. A student who passes all subjects but has less than 40% overall is shown separately.

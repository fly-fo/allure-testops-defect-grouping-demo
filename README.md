# allure-testops-defect-grouping-demo

Synthetic demo project for Allure TestOps using Python, Pytest, Allure Framework, and GitHub Actions.

## Purpose

This project is designed to demonstrate how a large launch can be analyzed and resolved faster in Allure TestOps.

It creates:

- around **400 test results**
- **350 passed**
- **40 failed**
- **10 broken**

The 50 problematic results are intentionally grouped into **5 repeated failure patterns**:

- 4 failed defect patterns × 10 results
- 1 broken defect pattern × 10 results

This allows a demo where:

- a large launch arrives in TestOps
- unresolved failures look numerous at first
- one defect is created from one result
- similar results are automatically linked through the same error pattern
- unresolved results decrease step by step
- the narrative shifts from **50 separate failures** to **5 grouped issues**

## Tech stack

- Python 3.11
- Pytest
- Allure Pytest
- GitHub Actions
- allurectl

## Project structure

```text
.
├── .github
│   └── workflows
│       └── testops.yml
├── tests
│   ├── __init__.py
│   ├── test_failed_groups.py
│   ├── test_broken_group.py
│   └── test_passed_generated.py
├── requirements.txt
├── pytest.ini
└── README.md

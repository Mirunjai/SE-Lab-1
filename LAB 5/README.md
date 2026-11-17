# LAB 5 - Static Code Analysis

This folder contains the completed Lab 5 work based on the assigned repository `SETAPESU26/L5_36_smart_home`.

## Files

- `smart_home.py` - cleaned and secured version of the assigned program.
- `issues.md` - issue table with the detected bugs, security problems, and style problems.
- `reflection.md` - reflection responses aligned with the lab learning outcomes.
- `reports/before/` - notes covering the issues present before fixes.
- `reports/after/` - final verification notes and the exact commands to regenerate raw tool output.
- `program_after.txt` - verified runtime output from the final version.

## Main fixes

1. Replaced the shared mutable default argument with `settings=None`.
2. Converted identifiers to PEP 8 snake_case naming.
3. Added an import-safe `if __name__ == "__main__"` guard.
4. Added explicit UTF-8 encoding for JSON output.
5. Removed the hard-coded password.
6. Changed the default hub bind address from `0.0.0.0` to `127.0.0.1`.
7. Removed the unused `subprocess.call(..., shell=True)` helper.
8. Cleaned remaining formatting and long-line issues.

## Reproduce the analysis

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pylint bandit flake8

python -m pylint smart_home.py > reports/after/pylint_report.txt
python -m bandit -r smart_home.py > reports/after/bandit_report.txt
python -m flake8 smart_home.py > reports/after/flake8_report.txt
```

The preparation sandbox used for these commits could execute Python but could not install packages from PyPI, so the repository does not pretend that unavailable lint tools were run. The report files explain this and provide reproducible commands.

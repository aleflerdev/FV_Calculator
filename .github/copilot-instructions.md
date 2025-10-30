## Quick context

This repository is a tiny single-file Python CLI: `FutureValueCalculator.py`.
The core calculation is the `future_value(principal, annual_rate, years, monthly_deposit=0, compounds_per_year=12)` function. The script gathers inputs via Python's built-in `input()` and prints a single formatted result.

## What an AI coding agent should know before editing

- Project scope: single script, no package layout, no tests, no dependencies. Keep edits minimal unless the user asks for a refactor to a package or test-suite.
- Inputs are read with `input()` at top-level; any behavior changes to UX (prompts, CLI flags) must be explicit in the user's request.
- Calculation detail: monthly deposit term uses formula
  fv_deposits = monthly_deposit*(((1+ r/n)**(n*t)-1)/(r/n))
  which divides by `r/n`. If `annual_rate` is zero (or very small), the current code will raise a division-by-zero error — handle `r == 0` as a special case when modifying the function.

## Coding conventions and patterns to follow

- Keep the `future_value(...)` function focused on numeric calculation (input parsing and printing are top-level script concerns).
- When adding changes, prefer small, testable functions and avoid modifying the top-level interactive flow unless asked.
- Use explicit floats and clear variable names: current code uses `r`, `n`, `t` for rate, compounds, years — keep these names in local small functions to match existing style.

## Example edits an agent might be asked to do (and how to do them)

- Fix zero-rate bug: inside `future_value`, if `annual_rate == 0`, compute `fv_deposits = monthly_deposit * n * t` and `fv_principal = principal` (no growth). Return the sum. Add a small docstring note about the zero-rate case.
- Add type hints and a simple unit test file (if requested): keep tests minimal (pytest) and only change layout if the user asks to add test tooling.
- Convert to CLI flags (argparse) only if asked; preserve the current `input()` interactive flow by default.

## How to run / debug locally

- Run the script in PowerShell (Windows):

```powershell
python FutureValueCalculator.py
```

- There are no external packages; use the system Python. If adding tests, the project currently has no test runner configured — add pytest to `requirements.txt` only when tests are requested.

## Files to reference when editing

- `FutureValueCalculator.py` — single source of truth for calculation and CLI behavior.

## Safety and UX guardrails for the agent

- Don't change prompts, printed output format, or interactive behavior without an explicit instruction from the user.
- If making math changes, include a short comment in the function showing the algebraic reasoning and a brief unit test demonstrating the expected numeric result.

## If you can't find explicit instructions from the user

- Make a small, reversible change and add a clear commit message; prefer adding a new function or test over rewriting the UI.

---
If any of these areas are unclear or you want a different level of refactor (tests, packaging, CLI flags), tell me which direction and I will update or expand this file.

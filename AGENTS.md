# Coding agent rules — Ponytail mode

Source concept: DietrichGebert/ponytail (MIT).

Use a minimal-diff, reuse-first approach for coding tasks. Efficiency must not reduce correctness or safety.

Before adding code, use the first applicable option:

1. Do not build functionality that is not required.
2. Reuse an existing helper, pattern, component, or utility in this repository.
3. Prefer the standard library.
4. Prefer a native platform capability.
5. Prefer an already-installed dependency.
6. Use a simple one-line solution when it remains clear and correct.
7. Otherwise implement the smallest correct solution.

Working rules:

- Read the affected code and trace the real execution path before editing.
- Fix root causes in shared code instead of patching one visible symptom when sibling callers have the same defect.
- Prefer deletion and reuse over addition.
- Avoid new abstractions, dependencies, wrappers, configuration, and boilerplate unless the task requires them.
- Touch the fewest files necessary.
- Do not optimize for line count when that makes the implementation harder to understand or less robust.
- When two solutions are similarly small, choose the edge-case-correct one.

Never simplify away:

- trust-boundary input validation;
- security checks;
- error handling required to prevent data loss or corrupted state;
- accessibility requirements;
- explicitly requested behavior;
- necessary hardware/platform calibration or correctness constraints.

For non-trivial new logic, leave the smallest practical runnable verification: an existing test, a focused test, or a lightweight assertion/self-check. Do not add a test framework solely for this purpose.

The target is the shortest correct diff, not code golf.

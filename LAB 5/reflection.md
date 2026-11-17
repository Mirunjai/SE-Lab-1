# Reflection

> Note: the uploaded three-page handout says to answer reflection questions, but the actual four question prompts are not included in the supplied pages. The responses below are therefore organized around the lab's stated learning outcomes rather than presented as verbatim instructor questions.

## 1. What did static analysis reveal that normal execution did not?

Running the original program exposed the mutable-default bug because the Ceiling Light unexpectedly received the thermostat temperature setting. Static analysis adds another layer by detecting problems that may not appear during one execution, such as insecure shell usage, hard-coded secrets, naming/style violations, and maintainability issues.

## 2. How did Pylint improve the code?

Pylint-oriented cleanup improved readability and correctness. The mutable default argument was replaced with `None`, functions and parameters were renamed using snake_case, docstrings were added, file encoding was made explicit, missing-device handling became safer, and the module was protected with a main guard so importing it does not automatically run the demo.

## 3. How did Bandit improve security?

The security pass removed the hard-coded password and the unused shell command built with `shell=True`. It also changed the hub's default address from `0.0.0.0`, which binds on every interface, to `127.0.0.1`, which is safer for a local demonstration. These changes reduce exposure and command-injection risk.

## 4. How did Flake8 contribute to maintainability?

The formatting pass made the code consistently PEP 8 compliant in spacing, blank lines, naming, comments, and line length. Consistent formatting makes code easier to scan, review, and modify, while also reducing avoidable warnings during continuous integration or code review.

## Overall reflection

Using multiple static-analysis tools is useful because they focus on different classes of problems. Pylint emphasizes code quality, Flake8 emphasizes style and formatting, and Bandit emphasizes security. Together with actually running the program, they provide broader coverage than any one method alone.

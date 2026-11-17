# Lab 5 - Identified Static Analysis Issues

| Issue | Type / Tool | Line(s) in assigned file | Description | Fix Approach |
|---|---|---:|---|---|
| Mutable default argument | Bug / Pylint | 11 | `settings={}` is shared by every call, so changing one device's settings can affect another device. | Use `settings=None` and create a fresh dictionary inside the function. |
| Non-PEP-8 function/parameter names | Style / Pylint + Flake8 | 11-49 | Names such as `addDevice`, `deviceName`, and `powerUsage` use camelCase. | Rename to snake_case and update call sites. |
| Missing main guard | Quality / Pylint | 67 | `main()` runs immediately when the module is imported. | Use `if __name__ == "__main__": main()`. |
| Hard-coded password | Security / Bandit | 7 | `HUB_PASSWORD` contains a password-like constant in source code. | Remove the unused secret from source; real secrets should come from protected configuration. |
| Bind to all interfaces | Security / Bandit | 4 | `0.0.0.0` exposes the service on every network interface. | Default to `127.0.0.1` for local-only access. |
| Shell command construction | Security / Bandit | 49 | `subprocess.call(..., shell=True)` concatenates user-controlled text into a shell command. | Remove the unused helper (or use a validated argument list without a shell). |
| Formatting / whitespace | Style / Flake8 | 6, 35, 60 | Spacing, blank-line, and inline-comment formatting violate PEP 8. | Reformat to PEP 8 and keep lines within the style limits. |
| File opened without explicit encoding | Quality / Pylint | 40 | Text-file encoding depends on the host environment. | Open JSON using `encoding="utf-8"`. |

## Runtime observation

Before the fix, the demo printed the Ceiling Light settings as `{'temperature': 30}` after only the thermostat was configured. This demonstrates the shared mutable-default bug directly.

## Priority

Security findings and the shared-state bug were treated as the highest priority, followed by maintainability and formatting issues.

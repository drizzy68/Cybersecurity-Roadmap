# 🐍 Python for Security

Python is used here as an automation and reasoning tool, not as a replacement for understanding the underlying system.

## 1. Language fundamentals

Master:

- Variables and data types
- Strings, lists, tuples, sets and dictionaries
- Conditions
- Loops
- Functions
- Modules
- Exceptions
- File handling
- Classes when useful

A security script should be readable enough that another analyst can understand what it will do before running it.

## 2. Virtual environments

Use isolated environments for project dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install <package>
```

Keep dependency files and avoid committing secrets or local environment artifacts.

## 3. Files and structured data

Security automation frequently processes:

- logs
- JSON
- CSV
- configuration files
- IOC lists
- command output

Example:

```python
from pathlib import Path

log_path = Path("events.log")

for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
    if "failed" in line.lower():
        print(line)
```

The example is intentionally simple: understand the data model before building a complex parser.

## 4. Regex and parsing

Regular expressions are useful for extracting structured indicators from semi-structured text, but they should not be used blindly.

Ask:

- What input format is expected?
- What false positives are possible?
- What happens when the format changes?
- Can a structured parser do the job more safely?

## 5. HTTP

Python can automate HTTP interactions for authorized testing and defensive analysis.

Understand:

- methods
- status codes
- headers
- cookies
- redirects
- authentication
- timeouts
- TLS verification
- response parsing

Automation should respect scope, rate limits and authorization.

## 6. Sockets

Sockets expose transport-layer communication to applications.

Before writing a socket scanner, understand the networking material in [`../networking/`](../networking/README.md).

A script should never treat a timeout, refusal or successful connection as proof of a specific application without additional evidence.

## 7. Subprocesses

Python can execute operating-system commands, but subprocess calls require careful handling of arguments and untrusted input.

Prefer argument arrays over shell interpolation when a shell is unnecessary.

```python
import subprocess

result = subprocess.run(
    ["ip", "addr"],
    capture_output=True,
    text=True,
    check=False,
)

print(result.stdout)
```

## 8. Logging and errors

Security automation needs observable failure modes.

A useful program should distinguish:

- invalid input
- missing files
- network timeout
- authentication failure
- unexpected response
- internal programming error

Use the `logging` module for reusable tools rather than scattering debug prints throughout production-quality scripts.

## 9. Security automation projects

Good beginner projects include:

1. Log parser
2. IOC extractor
3. Hash verification utility
4. HTTP header analyzer
5. Authorized asset inventory helper
6. Subnet calculator
7. Report-generation helper
8. Simple detection-rule tester

Each project should include input validation, clear scope, useful output and a README.

## 10. Secure coding principles

- Validate input.
- Avoid unnecessary shell execution.
- Never hard-code secrets.
- Handle errors explicitly.
- Use timeouts for network operations.
- Avoid excessive request rates.
- Record meaningful logs.
- Keep dependencies controlled.
- Test against known inputs.
- Document assumptions and limitations.

### Competency gate

I should be able to write small Python programs from memory, parse files and structured data, make controlled HTTP requests, automate repetitive security tasks, handle errors, and explain the security implications of the code I wrote.

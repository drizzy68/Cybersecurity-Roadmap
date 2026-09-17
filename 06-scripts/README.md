# 06 — Security Scripts

This section is the **index and design layer** for security automation. The executable scripts currently live in the repository's `scripts/` directory so there is one canonical location for code.

## Script quality standard

A useful security script should have:

- clear purpose
- explicit scope
- safe defaults
- input validation
- error handling
- useful output
- reasonable performance
- documented assumptions
- no hard-coded secrets
- tests or example inputs where practical

## Current scripts

### `scripts/subnet_calc.py`

Subnetting utility supporting the networking learning track.

The script is an implementation artifact. The networking concepts it uses remain canonical under [`01-foundations/networking`](../01-foundations/networking/README.md).

## Planned automation

- log parser
- IOC extractor
- hash verification utility
- HTTP header analyzer
- authorized asset inventory helper
- report generator
- simple detection-rule test harness

## Security rule

Automation must not become an excuse to remove judgment.

Before running a script against a real environment, confirm:

```text
Authorization
→ Scope
→ Input validation
→ Rate/impact controls
→ Logging
→ Safe failure behavior
```

A script that is technically correct but operationally unsafe is not a successful security tool.

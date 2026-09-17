# 🐍 Security Scripts

This directory contains the executable automation used by the roadmap.

## Current script

- [`subnet_calc.py`](subnet_calc.py) — subnetting practice and network calculation utility.

## Code standard

Scripts should be:

- readable
- scoped
- documented
- safe by default
- free of hard-coded secrets
- explicit about inputs and outputs
- tested against representative cases

## Planned automation

- log parser
- IOC extractor
- hash verification utility
- HTTP header analyzer
- authorized asset inventory helper
- report generator
- detection-rule test harness

## Architecture

- **Technical theory:** `01-foundations/`
- **Hands-on labs and CTFs:** `04-ctf-training/` and `05-projects/`
- **Executable automation:** this directory

The same concept should not be copied into multiple sections. Scripts should apply the underlying theory rather than reproduce it.

## Safety rule

Before running automation against a real environment, confirm:

```text
Authorization
→ Scope
→ Input validation
→ Rate/impact controls
→ Logging
→ Safe failure behavior
```

A technically correct script that is operationally unsafe is not a successful security tool.

# 02 — Offensive Security

This section contains the canonical offensive-security methodology and technical knowledge used for **authorized labs, CTFs and explicitly authorized assessments**.

It is not a list of tools. The goal is to understand the attack surface, form hypotheses, validate them safely, obtain evidence, and communicate risk accurately.

## Workflow

```text
Authorization & Scope
        ↓
Reconnaissance
        ↓
Enumeration
        ↓
Attack-Surface Analysis
        ↓
Vulnerability Validation
        ↓
Controlled Exploitation
        ↓
Privilege Escalation
        ↓
Evidence & Impact Analysis
        ↓
Remediation
        ↓
Report
```

## Canonical topics

### 🔎 Reconnaissance

- Scope definition
- Passive vs active reconnaissance
- Asset discovery
- Technology identification
- Attack-surface mapping

→ [`Reconnaissance`](reconnaissance/README.md)

### 🧭 Enumeration

- Host discovery
- Port and service discovery
- Version identification
- Service-specific enumeration
- Web enumeration
- Validation of scanner output

→ [`Enumeration`](enumeration/README.md)

### 🌐 Web Security

- HTTP request/response model
- Authentication and sessions
- Authorization and access control
- Input validation
- XSS
- Injection
- SSRF
- Path traversal
- File upload
- CSRF
- Security headers and configuration

→ [`Web Security`](web-security/README.md)

### ⬆️ Privilege Escalation

- Linux privilege boundaries
- Windows privilege boundaries
- Misconfigurations
- Services and scheduled execution
- Credentials and secrets in authorized labs
- Local enumeration methodology

→ [`Privilege Escalation`](privilege-escalation/README.md)

### 📋 Penetration-Testing Methodology

- Rules of engagement
- Scope and exclusions
- Evidence handling
- Finding construction
- Risk reasoning
- Remediation
- Reporting

→ [`Pentesting Methodology`](pentesting-methodology/README.md)

---

## eJPT readiness model

The offensive track should eventually demonstrate competence across:

1. Network reconnaissance and enumeration
2. Service and application analysis
3. Web application testing
4. Vulnerability validation
5. Initial access in controlled environments
6. Linux and Windows privilege escalation
7. Pivoting concepts and network segmentation
8. Evidence collection
9. Clear technical reporting
10. Repeatable troubleshooting

### Important distinction

A successful exploit is **not** the same thing as a successful security assessment.

A professional assessment must also answer:

- Was the action authorized?
- What asset and scope were affected?
- What evidence proves the issue?
- What was the root cause?
- What could an attacker realistically achieve?
- How should the issue be fixed?
- Can the result be reproduced safely?

Other sections should link to the canonical foundation material instead of re-explaining networking, Linux or Windows internals.

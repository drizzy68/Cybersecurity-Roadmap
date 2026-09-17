# 02 — Offensive Security

This track develops the ability to assess authorized systems methodically. The goal is not to memorize exploits; it is to understand attack surfaces, validate hypotheses, control risk, collect evidence and communicate remediation.

## 1. Authorization and scope

Before touching a target, define:
- authorized assets and IP ranges
- excluded systems and actions
- testing window
- allowed techniques
- data-handling requirements
- stop conditions
- evidence-storage rules

A technically successful test outside scope is still a failed professional process.

## 2. Reconnaissance

### Passive reconnaissance
Learn what can be established without directly interacting with the target, such as public DNS information, documented technologies and publicly available organizational information.

### Active reconnaissance
Within authorization, identify reachable hosts and observable services. Record timestamps and commands so results are reproducible.

### Questions
- What assets exist?
- Which addresses belong to the authorized scope?
- What technologies appear exposed?
- What information is uncertain and needs validation?

## 3. Enumeration

Enumeration converts discovery into detail.

### Network/service enumeration
For each host, establish:
- open/filtered/closed ports
- protocol
- service
- version where safely observable
- TLS behavior where relevant
- likely function
- confidence level

Never equate an open port with a vulnerability. A port is an observation; the service and configuration determine the security significance.

### Web enumeration
Map:
- domains and virtual hosts where authorized
- HTTP methods
- application paths
- parameters
- authentication boundaries
- cookies/session behavior
- technologies
- error handling
- access-control boundaries

## 4. Vulnerability validation

Move from scanner output to evidence:

**Observation → Hypothesis → Safe test → Result → Impact → Root cause → Remediation**

Avoid destructive proof when a low-impact demonstration is sufficient.

## 5. Web application security

Core learning areas:
- authentication vs authorization
- IDOR/BOLA
- XSS
- SQL injection concepts
- command injection concepts
- SSRF concepts
- file upload risks
- path traversal
- CSRF
- session management
- security misconfiguration
- access-control failures

For each finding, document the affected function, prerequisite, safe reproduction, evidence, impact and recommended control.

## 6. Initial access

The objective is to understand how a validated weakness can cross a security boundary in a controlled lab. Focus on root cause and defensive implications rather than exploit collection.

Record:
- entry condition
- technique
- privileges obtained
- affected component
- evidence
- cleanup

## 7. Privilege escalation

Study the difference between a low-privileged context and a higher-privileged context.

### Linux
- permissions and ownership
- SUID/SGID
- sudo configuration
- scheduled tasks
- services
- writable paths
- credentials/configuration exposure

### Windows
- service permissions
- scheduled tasks
- weak file/registry permissions
- token/privilege concepts
- credential exposure
- misconfigured software/services

Use isolated training environments and explain why the escalation is possible.

## 8. Post-exploitation concepts

Understand what an attacker could do after access:
- identify current identity and privileges
- inspect local configuration
- identify reachable resources
- determine persistence opportunities conceptually
- assess lateral-movement paths conceptually
- collect only necessary evidence
- clean up the lab

## 9. Reporting

A professional finding should contain:

**Title → Severity/risk rationale → Affected asset → Description → Root cause → Preconditions → Reproduction → Evidence → Impact → Remediation → References**

Separate facts from assumptions. State limitations explicitly.

## 10. eJPT readiness gate

Before treating eJPT preparation as complete, demonstrate repeated independent performance in:
- host/network auditing
- enumeration
- network/service analysis
- basic exploitation in labs
- web application testing
- privilege escalation fundamentals
- evidence collection
- structured reporting

The target is not simply finishing a course. The target is being able to reason through an unfamiliar authorized lab.

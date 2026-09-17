# 05 — Projects & Security Evidence

This is the portfolio layer. A project earns a place here when it demonstrates a capability that another person can inspect, understand and reproduce safely.

## Project lifecycle

**Question → Scope → Design → Build/Test → Observe → Troubleshoot → Validate → Document → Review → Publish**

## Required project structure

### 1. Objective
State the security or technical question being answered.

### 2. Scope
Define systems, assumptions, authorization and exclusions.

### 3. Environment
Document operating systems, network model, versions and relevant configuration without exposing secrets or sensitive infrastructure.

### 4. Methodology
Explain the sequence of actions and why each stage was selected.

### 5. Evidence
Include sanitized command output, screenshots, packet captures, logs, diagrams, code or measurements where appropriate.

### 6. Findings/outcome
State exactly what was observed. Separate observation from interpretation.

### 7. Troubleshooting
Record failures. A portfolio artifact becomes more valuable when it demonstrates diagnosis rather than only a perfect final run.

### 8. Security relevance
Explain how the result maps to confidentiality, integrity, availability, authentication, authorization, detection or operational risk.

### 9. Remediation
Where applicable, provide a concrete defensive recommendation and explain the underlying control.

### 10. Reflection
Answer:
- What did I initially misunderstand?
- What changed my hypothesis?
- What would I test next?
- What would I automate?
- What limitation remains?

## Current portfolio candidates

### Authorized network enumeration
Demonstrate scope validation, host discovery, service enumeration, result validation and reporting.

### Web application security
Document root cause, affected functionality, safe reproduction, impact and remediation for vulnerabilities studied in authorized labs.

### Penetration-testing assessment
Show the complete workflow from scope through reporting while sanitizing all client/internship information.

### VMware/virtualization
Explain hypervisor architecture, VM networking, resource allocation, service reachability and troubleshooting.

### SOC investigation
Build a small incident case from authentication, process and network telemetry.

### Python security automation
Create small scripts that solve a real repetitive analysis problem, include error handling and explain limitations.

## Portfolio quality levels

**Level 1 — Note:** records that something was learned.

**Level 2 — Reproducible lab:** another learner can repeat the exercise.

**Level 3 — Technical artifact:** includes evidence, reasoning and troubleshooting.

**Level 4 — Professional artifact:** polished methodology, limitations, security impact and remediation.

**Level 5 — Demonstrated capability:** project is independently executed, technically defensible and connected to a real security workflow.

The goal is depth over volume. Three excellent artifacts are more useful than a large collection of shallow completion notes.

# 🛡️ Cybersecurity Career Roadmap

> **An evidence-driven cybersecurity learning and portfolio system.**

This repository is the public technical record of my cybersecurity journey: what I learn, what I can do, how I troubleshoot, and what evidence I can produce.

## 🎯 Career Direction

| Track | Role |
|---|---|
| **Blue Team / SOC** | Primary employability direction |
| **Offensive Security** | Secondary direction + eJPT preparation |
| **Security Engineering** | Long-term path |
| **DFIR / Threat Intelligence** | Long-term investigation paths |
| **Cloud Security** | Future specialization |

**Current certification target:** eJPT

**Operating principle:** Fundamentals → Practice → Investigation/Building → Evidence → Certification → Employability → Specialization

## 🧭 Repository Structure

```text
01-foundations/             # Canonical technical foundations
02-offensive-security/      # Canonical offensive-security knowledge
03-blue-team/               # Canonical defensive/SOC knowledge
04-ctf-training/            # Challenge-specific learning
05-projects/                # Projects and portfolio evidence
07-dfir/                    # Forensics and incident-response specialization
notes/                      # Dated learning journal
scripts/                    # Executable security automation
SECURITY.md                 # Public repository security policy
```

### Single-source-of-truth rule

Each important concept has one canonical home:

- Networking → `01-foundations/networking/`
- Linux → `01-foundations/linux/`
- Windows → `01-foundations/windows/`
- Python → `01-foundations/python/`
- Offensive security → `02-offensive-security/`
- Blue Team/SOC → `03-blue-team/`
- CTF reasoning → `04-ctf-training/`
- Portfolio evidence → `05-projects/`
- DFIR → `07-dfir/`
- Executable scripts → `scripts/`

Other sections should apply or reference concepts rather than reproduce the same theory.

## 🗺️ Learning Path

**01 — Foundations**

Networking, Linux, Windows and Python.

**02 — Offensive Security**

Reconnaissance, enumeration, web security, privilege escalation and penetration-testing methodology.

**03 — Blue Team**

Logs, SIEM, incident response and detection engineering.

**04 — CTF Training**

Current OverTheWire Bandit milestone: **Level 20 reached; next 20 → 21**.

**05 — Projects**

Turn practical work into sanitized, reproducible technical evidence.

**07 — DFIR**

Endpoint artifacts, timelines, evidence handling and incident investigation.

## 🥷 Bandit

Bandit develops Linux fluency, command-line reasoning, protocol awareness and problem-solving discipline.

- [`Bandit track`](04-ctf-training/overthewire/bandit/README.md)
- [`Levels 0–20 deep write-up`](04-ctf-training/overthewire/bandit/levels-0-20.md)

Passwords and other reusable secrets are intentionally excluded from public documentation.

## 🧠 Learning Standard

For every major skill:

**Definition → Mechanism → Practice → Failure → Troubleshooting → Security relevance → Evidence → Transfer**

The target is technical reasoning, not tool memorization.

## 🔐 Public-Safety Rules

Never publish passwords, API keys, tokens, private credentials, confidential client data, sensitive production topology, or unapproved screenshots/data.

All offensive testing documented here is limited to systems I own, controlled training environments, CTF platforms, or explicitly authorized assessments.

See [`SECURITY.md`](SECURITY.md) for the repository security policy.

## 📈 Competency Gate

A topic is not complete because I read about it.

**Explain → Perform → Troubleshoot → Apply → Document → Teach**

## 📌 Current Mission

Deepen networking/Linux/Windows fundamentals, continue Bandit, build eJPT-level practical capability, develop SOC investigation skills, and continuously turn practical work into high-quality evidence.

**Build it. Break it safely. Investigate it. Document it. Explain it.**

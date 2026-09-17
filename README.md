# 🛡️ Cybersecurity Career Roadmap

> **An evidence-driven cybersecurity learning and portfolio system.**

This repository is the public technical layer of my cybersecurity journey. It is designed to show **what I understand, what I can do, how I troubleshoot, and what evidence I can produce**.

## 🎯 Career Direction

| Track | Role in the roadmap |
|---|---|
| **Blue Team / SOC** | Primary employability direction |
| **Offensive Security** | Secondary technical direction and eJPT preparation |
| **Security Engineering** | Long-term engineering path |
| **DFIR / Threat Intelligence** | Long-term investigation paths |
| **Cloud Security** | Future specialization |

**Current certification target:** eJPT

The operating principle is:

**Fundamentals → Hands-on practice → Investigation/building → Evidence → Certification → Employability → Specialization**

---

## 🧭 How This Repository Is Organized

The repository deliberately separates **knowledge, practice, evidence, and personal notes** so the same explanation is not copied into several places.

```text
Cybersecurity-Roadmap/
│
├── 01-foundations/             # Canonical technical foundations
│   ├── networking/
│   ├── linux/
│   ├── windows/
│   └── python/
│
├── 02-offensive-security/      # Canonical offensive-security knowledge
│   ├── reconnaissance/
│   ├── enumeration/
│   ├── web-security/
│   ├── privilege-escalation/
│   └── pentesting-methodology/
│
├── 03-blue-team/               # Canonical SOC / defensive knowledge
│   ├── logs/
│   ├── siem/
│   ├── incident-response/
│   └── detection/
│
├── 04-ctf-training/            # Challenge-specific learning
│   └── overthewire/bandit/
│
├── 05-projects/                # Actual investigations, labs and portfolio evidence
├── 06-scripts/                 # Automation index; executable scripts remain under scripts/
├── 07-dfir/                    # Forensic and investigation specialization
├── labs/                       # Reserved for future standalone lab material
├── notes/                      # Dated learning journal; not canonical reference material
└── scripts/                    # Working security scripts
```

### The single-source-of-truth rule

Each important concept has one **canonical home**.

- Networking concepts → `01-foundations/networking/`
- Linux administration → `01-foundations/linux/`
- Windows security administration → `01-foundations/windows/`
- Python security automation → `01-foundations/python/`
- Web vulnerabilities → `02-offensive-security/web-security/`
- SOC/log concepts → `03-blue-team/`
- Challenge reasoning → `04-ctf-training/`
- Real project evidence → `05-projects/`
- Forensic methodology → `07-dfir/`

Other pages should **apply or reference** a concept, not reproduce its textbook explanation.

---

## 🧠 Learning Standard

For every major skill I work through:

1. **Definition** — What is it?
2. **Mechanism** — How does it actually work?
3. **Purpose** — Why does it exist?
4. **Security relevance** — How can it fail or be abused?
5. **Hands-on use** — Can I perform it in an authorized lab?
6. **Failure analysis** — What happens when it does not work?
7. **Troubleshooting** — Can I isolate the cause?
8. **Evidence** — Can I document what I did?
9. **Transfer** — Can I apply the concept in a new environment?

The target is not tool memorization. The target is **technical reasoning**.

---

## 🗺️ Learning Path

### Phase 1 — Foundations

- IPv4, subnetting, routing and switching
- TCP/IP, ports, sockets and common protocols
- Linux shell, permissions, processes, services and networking
- Windows administration, Event Logs, PowerShell and authentication
- Python fundamentals and security automation

→ Start with [`01-foundations`](01-foundations/README.md)

### Phase 2 — Practitioner Skills

- Reconnaissance
- Enumeration
- Web application security
- Privilege escalation
- Penetration-testing methodology

→ Continue with [`02-offensive-security`](02-offensive-security/README.md)

### Phase 3 — Defensive Capability

- Windows/Linux logging
- SIEM concepts
- Alert triage
- Authentication investigation
- Incident response
- Detection engineering

→ Continue with [`03-blue-team`](03-blue-team/README.md)

### Phase 4 — CTF & Problem Solving

Current OverTheWire Bandit milestone: **Level 20 reached; next 20 → 21**.

→ [`04-ctf-training`](04-ctf-training/README.md)

### Phase 5 — Evidence & Portfolio

Turn practical work into sanitized, reproducible evidence:

**Objective → Environment → Method → Evidence → Finding/Outcome → Troubleshooting → Security lesson → Remediation**

→ [`05-projects`](05-projects/README.md)

### Phase 6 — DFIR & Specialization

- Endpoint artifacts
- Event analysis
- Timeline construction
- Evidence integrity
- Incident investigation

→ [`07-dfir`](07-dfir/README.md)

---

## 🥷 Current CTF Progress

Bandit is being used to develop Linux fluency, command-line reasoning, protocol awareness, and problem-solving discipline.

The public write-up intentionally documents **techniques and reasoning, not passwords or secrets**.

→ [`Bandit tracker`](04-ctf-training/overthewire/bandit/README.md)

→ [`Levels 0–20`](04-ctf-training/overthewire/bandit/levels-0-20.md)

---

## 🧪 Current Portfolio Evidence

The repository is building toward several evidence categories:

- Authorized network enumeration
- Penetration-testing methodology and reporting
- Web-security analysis
- VMware/virtualization documentation
- CTF write-ups
- Python security automation
- Future SOC investigations
- Future DFIR investigations

A project is valuable when it demonstrates **reasoning and evidence**, not merely that a tool was executed.

---

## 🔐 Public-Safety Rules

This repository is public. Never publish:

- Passwords or hashes that provide unauthorized access
- API keys, tokens or private credentials
- Private customer/client information
- Confidential internship information
- Sensitive internal hostnames, IP ranges or topology
- Unapproved screenshots or production data
- Exploit instructions tied to real unauthorized targets

All offensive testing is limited to systems I own, training environments, or explicitly authorized assessments.

---

## 📈 Competency Gate

A topic is not considered complete because I read about it.

**Explain → Perform → Troubleshoot → Apply → Document → Teach**

The roadmap therefore measures **capability**, not time spent or the number of certificates collected.

---

## 📌 Current Mission

> **Deepen networking/Linux/Windows fundamentals, continue Bandit, build eJPT-level practical capability, develop SOC investigation skills, and continuously convert real work into high-quality evidence.**

**Learning principle:** Build it. Break it safely. Investigate it. Document it. Explain it.

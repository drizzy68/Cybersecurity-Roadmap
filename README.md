# 🛡️ Cybersecurity Career Roadmap

> **Evidence-backed cybersecurity learning journey toward eJPT readiness and junior SOC / security analyst capability.**

This repository is the public evidence layer of my cybersecurity career roadmap. It documents what I learn, what I build, how I troubleshoot, and how I apply security concepts in practical labs.

## 🎯 Career Direction

**Primary employability track:** Blue Team / SOC / Security Operations  
**Secondary track:** Offensive Security / Ethical Hacking  
**Long-term tracks:** Security Engineering, DFIR, Threat Intelligence, Cloud Security  
**Current certification target:** eJPT

The strategy is simple:

**Skills → Labs → Evidence → Targeted Certification → Portfolio → Employability**

Certificates validate capability; they do not replace it.

## 🧭 How I Learn

For every major topic I use four competency questions:

1. **Can I explain it?**
2. **Can I perform it?**
3. **Can I troubleshoot it?**
4. **Can I document and apply it elsewhere?**

My practical learning loop is:

**Learn → Lab → Investigate/Build → Document → Prove → Specialize**

I prioritize hands-on work, use walkthroughs only when needed, and turn important learning into reusable evidence.

## 🗂️ Repository Structure

```text
Cybersecurity-Roadmap/
├── 01-foundations/
│   ├── networking/
│   ├── linux/
│   └── windows/
├── 02-offensive-security/
│   ├── reconnaissance/
│   ├── enumeration/
│   ├── web-security/
│   ├── privilege-escalation/
│   └── pentesting-methodology/
├── 03-blue-team/
│   ├── logs/
│   ├── siem/
│   ├── incident-response/
│   └── detection/
├── 04-ctf-training/
│   └── overthewire/
│       └── bandit/
├── 05-projects/
├── 06-scripts/
├── 07-dfir/
├── labs/
├── notes/
└── scripts/
```

The existing `labs/`, `notes/`, and `scripts/` areas are retained while the repository grows into a more structured public portfolio.

## 🥷 Current CTF Progress

### OverTheWire Bandit

**Current milestone: Level 20 reached**  
**Next:** Level 20 → 21

Bandit is being used to strengthen Linux and security problem-solving rather than simply collect challenge completions.

Skills practiced include:

- Linux filesystem navigation
- Shell quoting and argument parsing
- `find` and metadata-based discovery
- `grep`, `sort`, `uniq`, `strings`, `tr`
- Pipelines and stdout/stderr handling
- Encoding and decoding
- Compression and binary-file inspection
- SSH and SSH keys
- TCP service interaction
- TLS with `openssl`
- Permissions and setuid concepts
- Troubleshooting command failures

See the [Bandit learning track](04-ctf-training/overthewire/bandit/README.md) and [Levels 0–20 write-up](04-ctf-training/overthewire/bandit/levels-0-20.md).

## 🔐 Offensive Security

The offensive track follows an authorized penetration-testing workflow:

**Scope → Recon → Enumeration → Validation → Exploitation → Privilege Escalation → Evidence → Remediation → Report**

Current areas include network enumeration, web application security, vulnerability analysis, privilege boundaries, and penetration-testing methodology.

All offensive testing documented here is intended for authorized labs, training environments, or explicitly authorized assessments.

## 🛡️ Blue Team / SOC

The blue-team track is focused on building employable security-operations fundamentals:

**Alert → Validate → Scope → Investigate → Correlate → Contain/Escalate → Document → Improve**

Upcoming practical areas include Windows Event Viewer, authentication events, PowerShell, SIEM fundamentals, log correlation, detection engineering, and incident investigation.

## 🧪 Portfolio Evidence

Projects are documented around evidence rather than completion badges. A strong artifact should show:

- Objective and scope
- Environment and assumptions
- Methodology
- Tools/commands or implementation
- Evidence and observations
- Findings or outcome
- Troubleshooting
- Security relevance
- Remediation or lessons learned

Current project themes include network enumeration, web-security analysis, penetration testing, virtualization, and future SOC investigations/security automation.

## 📚 Existing Learning Notes

The `notes/` directory contains dated learning records. For example, the September 15 Bandit session documents Levels 0–10 and the reasoning behind techniques such as `find`, `grep`, pipelines, shell literal handling, and stdout/stderr redirection. fileciteturn40file0

## 🚀 Roadmap

### Phase 1 — Foundations

- Networking
- Linux
- Windows
- Python

### Phase 2 — Practitioner Skills

- Reconnaissance
- Enumeration
- Web security
- Privilege escalation
- Security troubleshooting

### Phase 3 — eJPT Readiness

- Host/network auditing
- Host/network penetration testing
- Web application testing
- Structured reporting
- Repeated authorized hands-on labs

### Phase 4 — SOC Capability

- Windows/Linux logs
- SIEM
- Alert triage
- Authentication analysis
- Incident response
- Detection fundamentals

### Phase 5 — Portfolio & Employability

- 3–5 strong technical artifacts
- Sanitized internship evidence
- CTF write-ups
- Security scripts
- Technical interview stories
- Consistent GitHub documentation

### Phase 6 — Specialization

Depending on experience and career direction:

- Security Engineering
- DFIR
- Threat Intelligence
- Cloud Security
- Advanced Offensive Security

## 📈 Progress Philosophy

I treat roadmap phases as **competency gates, not calendar deadlines**.

I would rather be able to independently explain, execute, troubleshoot, and document a smaller number of skills than superficially recognize a large number of tools.

## 🔒 Security & Privacy

This is a public learning repository. Sensitive information must never be committed, including:

- Passwords
- API keys
- Tokens
- Private credentials
- Confidential client/internship information
- Sensitive production topology
- Unapproved internal host information

Public write-ups should demonstrate methodology without exposing secrets or creating unnecessary operational risk.

## 📌 Current Mission

> **Strengthen networking/Linux fundamentals, continue Bandit, build eJPT-style practical capability, start Windows security and SOC foundations, and turn real technical work into high-quality public evidence.**

---

**Learning principle:** Build it. Break it safely. Investigate it. Document it. Explain it.

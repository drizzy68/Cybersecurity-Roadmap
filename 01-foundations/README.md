# 01 — Foundations

This section contains the **canonical technical foundations** used everywhere else in the roadmap.

The purpose is not to collect definitions. It is to understand how computers, operating systems, networks and scripts behave well enough to troubleshoot them and recognize security consequences.

## Canonical topics

### 🌐 Networking

Core areas:

- IPv4 addressing and binary representation
- CIDR and subnetting
- TCP/IP models and encapsulation
- Ethernet, ARP and switching
- Routing tables and longest-prefix matching
- TCP, UDP, ports and sockets
- DNS and DHCP
- VLANs, trunks, NAT and segmentation
- HTTP/HTTPS, SSH, SMB, RDP, LDAP and Kerberos
- TLS and certificate trust
- Network troubleshooting and packet analysis

→ [`Networking`](networking/README.md)

### 🐧 Linux

Core areas:

- Shell and command execution
- Filesystem hierarchy
- Users, groups and permissions
- Processes, signals and services
- Package management
- Networking and sockets
- SSH
- Logs
- Bash scripting
- Linux security boundaries

→ [`Linux`](linux/README.md)

### 🪟 Windows

Core areas:

- Accounts and groups
- Processes and services
- NTFS and Windows filesystem concepts
- Event Viewer and Event Logs
- PowerShell
- Authentication
- DNS/DHCP dependencies
- Active Directory
- GPO
- Kerberos and LDAP
- Windows security monitoring

→ [`Windows`](windows/README.md)

### 🐍 Python

Core areas:

- Python language fundamentals
- Functions, modules and environments
- Files and structured data
- Exceptions and logging
- Regular expressions
- HTTP and sockets
- Subprocesses
- Security automation
- Safe handling of credentials and input

→ [`Python for Security`](python/README.md)

---

## How to study each foundation

Use the same investigation loop for every concept:

**Definition → mechanism → example → lab → failure → troubleshooting → security relevance → evidence**

### Foundation gate

A topic moves forward when I can:

- Explain it without reading notes.
- Perform the basic task independently.
- Diagnose a deliberately broken example.
- Explain common security failure modes.
- Produce a short technical write-up or lab artifact.

Detailed explanations live in the topic directories above. Other sections should link back here rather than duplicate them.

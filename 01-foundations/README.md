# 01 — Foundations

Cybersecurity capability depends on understanding the systems being tested, monitored and defended. This section builds the mental models required before relying on security tools.

## 1. Networking

### Core knowledge
- IPv4 addressing: network bits, host bits, private/public ranges
- CIDR and subnetting: network address, broadcast address, usable hosts, subnet boundaries
- TCP/IP model and encapsulation
- TCP vs UDP; three-way handshake; ports and sockets
- ARP, ICMP, DNS and DHCP
- Switching vs routing
- Default gateways, routing tables and longest-prefix matching
- VLANs, trunks, NAT and segmentation
- HTTP/HTTPS, SSH, SMB, RDP, LDAP and Kerberos at a conceptual level
- TLS fundamentals and certificate trust

### Security connection
Networking knowledge supports attack-surface discovery, firewall analysis, packet inspection, service enumeration, segmentation analysis, incident investigation and troubleshooting.

### Practical evidence
- Solve subnetting problems without a calculator.
- Draw a small network and explain every hop.
- Capture traffic in Wireshark and identify protocol behavior.
- Run an authorized service scan and explain what each result means rather than treating scanner output as truth.
- Troubleshoot a deliberately broken gateway, DNS or service connection.

## 2. Linux

### CLI progression
Start with `pwd`, `ls`, `cd`, `cat`, `less`, `head`, `tail`, `cp`, `mv`, `rm`, `mkdir`, and `touch`. Progress to `find`, `grep`, `sort`, `uniq`, `strings`, `cut`, `tr`, `awk`, `sed`, `xargs`, pipes and redirection.

### Administration progression
- users, groups, UID/GID
- ownership and permissions
- `chmod`, `chown`, `sudo`
- SUID/SGID and privilege boundaries
- processes, signals and jobs
- systemd/services
- listening sockets and resource usage
- SSH and key authentication
- package management
- configuration files and logs
- shell scripting

### Security connection
Linux administration is the foundation for understanding vulnerable services, privilege escalation, persistence, log investigation, SSH security and security tooling.

### Practical evidence
For each command or administration task, record the objective, syntax, expected output, actual output, failure mode, troubleshooting process and security relevance.

## 3. Windows

### Administration progression
1. Accounts and groups
2. Processes and services
3. Windows filesystem
4. Event Viewer and Windows Event Logs
5. PowerShell
6. Authentication concepts
7. DNS/DHCP dependencies
8. Active Directory
9. Users, groups, OUs and GPOs
10. Kerberos and LDAP concepts
11. Security monitoring and investigation

### Security connection
Windows knowledge is essential for SOC work because many enterprise alerts involve authentication, processes, services, PowerShell, endpoint activity and Active Directory.

### Practical evidence
Build a small isolated Windows lab. Generate normal authentication and process activity, inspect the resulting logs, identify what happened, and document the investigation. Then repeat with deliberately suspicious but safe lab activity.

## 4. Python

### Learning progression
- variables and data types
- conditions and loops
- functions
- modules and virtual environments
- files/directories
- exceptions and logging
- regex and text parsing
- JSON/CSV
- HTTP requests
- sockets
- subprocesses
- security automation

### Security projects
Examples include log parsers, IOC extractors, port/service inventory tools for authorized targets, hash utilities, HTTP response analyzers and report-generation helpers.

## Foundation learning loop

For every major concept:

**Definition → How it works → Why it matters → Lab → Failure → Troubleshooting → Security application → Documentation**

## Competency gate

A foundation topic is not complete because a definition is memorized. The target is independent performance: **explain → perform → troubleshoot → apply → document**.

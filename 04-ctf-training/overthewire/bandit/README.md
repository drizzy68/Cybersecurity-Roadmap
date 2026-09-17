# OverTheWire Bandit

## Purpose
Bandit is part of this roadmap because it turns Linux fundamentals into repeated hands-on problem solving. The goal is not to collect passwords; it is to understand the underlying commands, shell behavior, file handling, permissions, and network interactions.

## Progress

- [x] Levels 0 → 10
- [x] Levels 10 → 15
- [x] Levels 15 → 20
- [x] Level 20 reached
- [ ] Level 20 → 21

## Documentation standard

Every level is documented using:

**Objective → Method → Why it works → Security relevance → Lesson learned**

Passwords, private credentials, tokens, and other secrets are intentionally excluded.

## Skills developed

- Linux filesystem navigation
- Shell quoting and argument parsing
- Hidden files and awkward filenames
- `find` and metadata-based discovery
- `grep`, `sort`, `uniq`, `strings`, `tr`, and pipelines
- Encoding and decoding
- Compression and binary-file handling
- SSH and SSH keys
- TCP service interaction with `nc`
- TLS connections with `openssl`
- File permissions and setuid behavior
- Troubleshooting command failures

## Security connection

These skills support later work in reconnaissance, enumeration, privilege escalation, log analysis, forensic triage, and security automation. Bandit is therefore treated as a Linux-security fundamentals lab rather than a standalone CTF achievement.

## Next application

The next objective is to transfer the same reasoning into an authorized penetration-testing workflow:

**Recon → Enumeration → Service identification → Initial access → Privilege escalation → Evidence → Reporting**

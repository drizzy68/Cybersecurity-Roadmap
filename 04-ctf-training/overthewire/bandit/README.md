# OverTheWire Bandit — Deep Learning Track

Bandit is a deliberately constrained environment for building Linux and security problem-solving muscle. The valuable output is not the password for a level; it is the reasoning used to discover the next step.

## Progress

- [x] 0 → 10 — filesystem, shell parsing, search and text processing
- [x] 10 → 15 — encoding, compression and network interaction
- [x] 15 → 20 — TLS, service interaction, sessions and privilege boundaries
- [x] Level 20 reached
- [ ] 20 → 21 — current challenge

## How to study each level

For every challenge, answer these questions before looking for a walkthrough:

1. What exactly is the objective?
2. What information is already known?
3. What local files, permissions or services can I inspect?
4. Which command can reduce the uncertainty?
5. What does the output actually prove?
6. What assumption could be wrong?
7. How does the technique transfer to real security work?

## Evidence format

Each write-up should contain:

**Objective → Observations → Hypothesis → Command/Method → Output interpretation → Troubleshooting → Security relevance → Lesson learned**

Do not publish passwords, private keys, tokens or other secrets.

## Transferable skill map

| Bandit concept | Linux/security capability |
|---|---|
| Awkward filenames | Shell parsing and safe argument handling |
| Hidden files | Filesystem enumeration |
| `file` | Content identification independent of extension |
| `find` | Metadata-based discovery |
| `2>/dev/null` | stdout/stderr management |
| `grep` | Targeted text search |
| `sort | uniq` | Data normalization and deduplication |
| `strings` | Extracting readable content from binary data |
| Base64/encoding | Data representation and decoding |
| Compression | File-format identification and extraction |
| SSH keys | Authentication concepts |
| `nc` | TCP client/server interaction |
| `openssl` | TLS inspection and secure transport |
| `diff` | Comparing files/configuration |
| setuid | Privilege boundaries |

## Progression beyond Bandit

Bandit should eventually feed into three practical tracks:

### Offensive
Use Linux fluency during authorized reconnaissance, enumeration, service analysis and privilege-escalation labs.

### Defensive
Use the same command-line skills to inspect logs, processes, network connections and suspicious artifacts.

### Automation
Reproduce repetitive discovery and analysis tasks with Python or shell scripts.

## Current milestone

**Level 20 reached. Next: 20 → 21.**

The challenge should be approached as a reasoning exercise first and a command exercise second.

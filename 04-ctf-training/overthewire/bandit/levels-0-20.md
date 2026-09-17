# OverTheWire Bandit — Levels 0–20

## Why this lab matters

Bandit provides repeated practice with Linux command-line reasoning. The important outcome is transferable skill: understanding what a command is doing, why a command fails, how to troubleshoot it, and how the same technique applies to security work.

> No Bandit passwords are included in this public write-up.

## Level-by-level learning record

### 0 → 1 — Read a file
**Concept:** Basic file access

**Method:** Read the `readme` file with `cat`.

**Security relevance:** Security analysts constantly inspect configuration files, logs, scripts, and captured artifacts from the command line.

### 1 → 2 — Filename beginning with `-`
**Concept:** Argument parsing

**Method:** Reference the file as a path such as `./-` instead of passing a bare `-`.

**Why:** A bare `-` can be interpreted as standard input rather than a literal filename.

**Security relevance:** Correct path handling matters in administration, automation, and security tooling.

### 2 → 3 — Spaces and special characters
**Concept:** Shell tokenization

**Method:** Quote the filename and use `./` when appropriate.

**Why:** Quoting keeps spaces together as one argument, while a path prefix prevents a leading dash from being treated as an option.

**Security relevance:** Shell parsing mistakes can cause commands to target the wrong files or behave unexpectedly.

### 3 → 4 — Hidden files
**Concept:** Unix hidden-file convention

**Method:** Use `ls -a` to reveal entries beginning with `.` and then read the relevant file.

**Security relevance:** Hidden files can contain configuration, application metadata, credentials, or forensic clues. Hidden does not mean secure.

### 4 → 5 — Identify file type
**Concept:** Content versus filename

**Method:** Run `file` across the candidate files and identify the readable text file.

**Why:** `file` examines content characteristics rather than trusting an extension.

**Security relevance:** Analysts often need to identify unknown artifacts before processing them.

### 5 → 6 — Find by metadata
**Concept:** Filesystem search

**Method:** Use `find` with file type, exact size, and executable-state constraints.

**Security relevance:** Metadata-based discovery is useful when triaging large filesystems or looking for suspicious artifacts.

### 6 → 7 — Search the whole filesystem
**Concept:** Scope, ownership, groups, permissions, and stderr

**Method:** Search `/` using owner, group, and size criteria while redirecting permission errors with `2>/dev/null`.

**Why:** Searching from `/` crosses many directories where the current user may not have access.

**Security relevance:** Understanding stdout versus stderr and filesystem permissions is essential for both administration and privilege-escalation analysis.

### 7 → 8 — Search structured text
**Concept:** Pattern matching

**Method:** Use `grep` to locate the line containing the target marker in a large text file.

**Security relevance:** The same technique applies to logs, configuration files, command output, and forensic artifacts.

### 8 → 9 — Unique values in a dataset
**Concept:** Pipelines and data reduction

**Method:** Sort the data and then use `uniq -u` to isolate the non-repeated line.

**Why:** `uniq` operates on adjacent duplicates, so sorting first groups identical values together.

**Security relevance:** Similar pipelines can reduce noisy security data and help isolate anomalous values.

### 9 → 10 — Extract readable strings
**Concept:** Binary-data inspection

**Method:** Use `strings` to extract printable sequences and filter the result.

**Security relevance:** Analysts use string extraction during malware triage, binary inspection, and artifact analysis.

## Levels 10 → 15 — Encoding, transformation, and network interaction

The next section introduced progressively more security-relevant techniques:

- Base64 decoding and recognizing encoded data
- Character substitution and transformation
- Hex/binary inspection with tools such as `xxd`
- Working with compressed or transformed data
- Using SSH keys for authentication
- Interacting with TCP services using `nc`

**Core lesson:** Do not blindly run commands. First identify the data format, determine what transformation is expected, and validate the result.

## Levels 15 → 20 — TLS, enumeration, validation, and privilege boundaries

This section expanded the problem-solving model into network and operating-system concepts:

- Establishing encrypted connections with `openssl`
- Identifying and validating services rather than assuming a port means a particular service
- Comparing data with tools such as `diff`
- Understanding shell/session behavior
- Recognizing setuid and privilege-boundary concepts
- Combining multiple small tools to solve a larger problem

**Core lesson:** Security work is often a chain of observations and validations rather than one magical command.

## Current milestone

**Level 20 reached.**

Next target: **20 → 21**.

The next step is not just to solve the level. The goal is to document the underlying concept and connect it to a broader security competency.

## Transferable competency map

| Bandit skill | Broader cybersecurity use |
|---|---|
| Shell navigation | Linux administration and security tooling |
| `find` | Host/file enumeration and triage |
| `grep` / pipelines | Log analysis and investigation |
| `strings` | Binary and malware triage |
| Encoding/decoding | Protocol and artifact analysis |
| SSH | Secure remote administration |
| `nc` | TCP service understanding and troubleshooting |
| `openssl` | TLS inspection and secure communications |
| Permissions/setuid | Privilege boundaries and escalation analysis |
| Troubleshooting | Core SOC/pentest operational skill |

## Evidence standard

For each challenge, ask:

1. Can I explain the concept?
2. Can I perform it without a walkthrough?
3. Can I troubleshoot a failure?
4. Can I explain its security relevance?
5. Can I apply the technique somewhere outside Bandit?

That is the standard used throughout this cybersecurity roadmap.

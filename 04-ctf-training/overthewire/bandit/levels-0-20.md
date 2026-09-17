# OverTheWire Bandit — Levels 0–20

## Purpose of this write-up

This is the **deep challenge-by-challenge record** for my OverTheWire Bandit progression. It is intentionally more detailed than the canonical Linux notes because the value of a CTF write-up is not only the command that worked, but the reasoning that led to it, the failure modes to expect, and the security concept being exercised.

> **Public-safety rule:** no Bandit passwords, reusable credentials, private keys, tokens, or other challenge secrets are stored here.

For permanent Linux theory, see [`01-foundations/linux/README.md`](../../../01-foundations/linux/README.md). This file focuses on how those concepts were applied to individual challenges.

---

# How to study each level

For every challenge, use this loop:

**Read → identify constraints → form a hypothesis → inspect → test → validate → document → generalize**

A successful solve is not considered complete until I can answer:

- What information did the challenge give me?
- What was the actual obstacle?
- Why did the chosen command work?
- What would make the command fail?
- What security concept did I practice?
- Where could this technique be useful outside Bandit?

---

# Level 0 → 1 — Read a file

## Objective

The starting task is deliberately simple: access the supplied `readme` file and use its contents to continue.

## Concept

**Basic filesystem navigation and file reading.**

Linux treats files as the primary interface for much of the operating system. Before learning sophisticated security tools, an analyst needs to be comfortable locating and reading artifacts from a shell.

## Approach

First establish where you are and what is present:

```bash
pwd
ls
```

Then read the file:

```bash
cat readme
```

## Why it works

`cat` reads a file and writes its contents to standard output. The shell sends that output to the terminal because stdout is connected to the terminal by default.

## What I am actually learning

This level is really about the basic chain:

```text
Current directory → filename → filesystem object → stdout → terminal
```

## Security relevance

Security analysts routinely inspect:

- configuration files
- logs
- scripts
- evidence files
- service information
- captured text artifacts

## Failure modes

If `cat readme` fails, possible causes include:

- wrong current directory
- typo in the filename
- insufficient permissions
- the file is not a regular text file

The correct response is to inspect rather than guess.

---

# Level 1 → 2 — Filename beginning with `-`

## Objective

Read a file whose name begins with a dash.

## Concept

**Argument parsing and option ambiguity.**

Many Unix commands interpret arguments beginning with `-` as command-line options. Therefore a filename such as `-` can be interpreted differently from an ordinary filename.

## Approach

Instead of passing the ambiguous filename directly, explicitly identify it as a path:

```bash
cat ./-
```

## Why it works

`./-` means:

> Start in the current directory and access the entry literally named `-`.

The `./` changes the argument from an option-like token into an explicit filesystem path.

Another general technique is the end-of-options marker when supported:

```bash
command -- -filename
```

## Security relevance

Argument parsing mistakes matter in:

- shell automation
- backup scripts
- file-processing utilities
- CI/CD pipelines
- security tools

An unsafe script can accidentally interpret attacker-controlled filenames as options.

## Deeper lesson

A command does not necessarily know whether an argument is a filename or an option from your intention. **The parser decides based on syntax.**

---

# Level 2 → 3 — Filename containing spaces

## Objective

Read a file whose filename contains spaces.

## Concept

**Shell tokenization and quoting.**

The shell normally separates command arguments at whitespace. Therefore a filename containing spaces can unintentionally become multiple arguments.

## Approach

Quote the complete filename:

```bash
cat "spaces in this filename"
```

or escape the spaces:

```bash
cat spaces\ in\ this\ filename
```

## Why it works

Quoting tells the shell to treat the enclosed text as one argument rather than splitting it into multiple words.

For example, without quoting:

```text
cat file name.txt
```

may become three arguments:

```text
file
name.txt
```

With quoting:

```text
"file name.txt"
```

becomes one argument.

## Security relevance

Shell parsing is security-critical because input that crosses a shell boundary can change the meaning of a command. This is one reason security automation should avoid constructing shell commands from untrusted strings.

## Generalization

The important distinction is:

```text
Shell syntax ≠ filesystem naming
```

A filename may be perfectly valid to the filesystem while requiring special syntax for the shell.

---

# Level 3 → 4 — Hidden files

## Objective

Locate a hidden file inside the supplied directory.

## Concept

**Unix hidden-file convention.**

Unix-like systems commonly treat filenames beginning with `.` as hidden from ordinary directory listings.

## Approach

List all entries:

```bash
ls -la
```

or:

```bash
ls -a
```

Then inspect the relevant hidden file with `cat`.

## Why it works

`ls` normally suppresses dotfiles. The `-a` option tells it to include them. `-l` provides a detailed listing including permissions, ownership, size, and timestamps.

## Important distinction

A hidden file is **not** a protected file.

Hiddenness is a presentation convention, not an access-control mechanism.

## Security relevance

Dotfiles can contain:

- application configuration
- shell history
- development metadata
- environment settings
- credentials or tokens
- repository information

During incident response or web/server assessment, hidden does not mean irrelevant.

## Investigation habit

When examining a directory, consider both:

```bash
ls -la
find . -maxdepth 1 -type f -print
```

The first is useful for human inspection; the second is useful when building reproducible enumeration workflows.

---

# Level 4 → 5 — Identify the correct file type

## Objective

Among several files, identify the one containing readable text.

## Concept

**File content versus filename/extension.**

A filename extension is only a convention. The actual content may be binary, compressed, executable, text, or another format.

## Approach

Inspect the candidate files:

```bash
file ./*
```

Then read the candidate identified as ASCII/text.

## Why `file` matters

`file` examines characteristics of the data and uses signatures/magic information to classify it. This is more reliable than assuming:

```text
filename → extension → actual format
```

## Security relevance

This is a basic digital-forensics habit. Before opening, executing, decoding, or parsing an unknown artifact, identify what it actually is.

Examples include:

- suspicious attachments
- downloaded binaries
- malware samples
- forensic artifacts
- compressed evidence
- files with misleading extensions

## Deeper lesson

**Never trust a label when you can inspect the underlying data.**

---

# Level 5 → 6 — Find a file using metadata

## Objective

Locate a file matching specific filesystem characteristics, including size and executable state.

## Concept

**Metadata-driven filesystem enumeration.**

Instead of opening every file manually, express the conditions to `find`.

A representative pattern is:

```bash
find . -type f -size 1033c ! -executable
```

## Breaking the command down

- `find .` — start at the current directory
- `-type f` — restrict results to regular files
- `-size 1033c` — exact size in bytes (`c` means bytes)
- `! -executable` — exclude executable files

## Why this matters

The command converts a human description into machine-searchable predicates.

Instead of:

> Find the file that looks right.

we express:

```text
regular file AND exact size AND not executable
```

## Security relevance

Metadata filtering is useful for:

- malware triage
- suspicious-file hunting
- locating configuration artifacts
- incident-response collection
- filesystem investigations

## Important limitation

A metadata match does not prove that an artifact is malicious or trustworthy. It only narrows the candidate set.

That distinction—**discovery versus validation**—is fundamental to security work.

---

# Level 6 → 7 — Search the filesystem by owner, group, and size

## Objective

Find a file somewhere on the system matching ownership and size requirements.

## Concept

**Filesystem permissions, ownership, search scope, and stderr handling.**

## Approach

A representative search is:

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

## Command anatomy

- `/` — search from the filesystem root
- `-type f` — regular files only
- `-user bandit7` — owner condition
- `-group bandit6` — group condition
- `-size 33c` — exact size in bytes
- `2>/dev/null` — discard permission-related error output

## The important new concept: file descriptors

Unix processes commonly expose:

```text
0 = stdin
1 = stdout
2 = stderr
```

Therefore:

```bash
2>/dev/null
```

means:

> Send standard error to `/dev/null`.

It does not suppress normal command output.

## Why permission errors occur

Starting at `/` crosses directories that the current account may not be allowed to inspect. Those failures are reported through stderr.

## Security relevance

Understanding ownership and permissions is central to:

- Linux administration
- privilege escalation analysis
- incident response
- access-control auditing
- suspicious-file investigations

## Deeper lesson

The ability to search is itself constrained by the permission model. **Visibility is not automatically universal.**

---

# Level 7 → 8 — Search structured text with `grep`

## Objective

Find a specific value inside a large text file.

## Concept

**Pattern matching and targeted text search.**

A representative approach is:

```bash
grep millionth data.txt
```

## Why it works

`grep` reads input and prints lines matching a pattern. It is especially powerful when the file is too large to inspect manually.

## Security relevance

The same idea appears everywhere in security:

```bash
grep "Failed password" /var/log/auth.log
grep "ERROR" application.log
grep -i "password" config.txt
```

The exact commands depend on the environment, but the underlying skill is the same: **reduce a large dataset using a meaningful predicate.**

## Deeper lesson

Good analysts do not merely search for words. They understand what the search result means and whether the match is sufficient evidence.

A string match is an observation, not automatically a conclusion.

---

# Level 8 → 9 — Find the unique line

## Objective

Identify the line that occurs only once in a file containing repeated values.

## Concept

**Sorting, uniqueness, and Unix pipelines.**

Use:

```bash
sort data.txt | uniq -u
```

## Why sorting comes first

`uniq` compares adjacent lines. It does not perform a global frequency analysis on arbitrary unsorted input.

Therefore:

```text
raw data
   ↓
sort
   ↓
adjacent duplicates
   ↓
uniq -u
   ↓
unique line
```

## Security relevance

This is the beginning of command-line data analysis.

The same pipeline model can be used to reduce:

- IP-address lists
- usernames
- domains
- log entries
- DNS observations
- alert values

## Deeper lesson: composability

Unix tools are often deliberately small. Their strength comes from composition:

```bash
command1 | command2 | command3
```

This is highly relevant to security automation because analysts frequently need to transform one tool's output into another tool's input.

---

# Level 9 → 10 — Extract readable strings from binary data

## Objective

Find human-readable content embedded in a file that is not ordinary text.

## Concept

**Binary inspection and printable-string extraction.**

A common approach is:

```bash
strings data.bin | grep '='
```

## Why it works

`strings` scans binary data and extracts printable character sequences. Piping it to `grep` narrows the output.

## Why this is useful in security

Binary artifacts frequently contain useful strings such as:

- URLs
- filenames
- error messages
- protocol markers
- usernames
- configuration fragments
- debugging information

## Important limitation

`strings` does not decode the entire binary or prove what the extracted text means. It is a reconnaissance/triage technique.

## Security mindset

When a file is unfamiliar, use progressively stronger inspection:

```text
identify format → extract obvious metadata/strings → inspect structure → parse with the correct tool
```

---

# Level 10 → 11 — Base64 decoding

## Objective

Recognize that the supplied data is encoded and recover the underlying representation.

## Concept

**Encoding versus encryption.**

Base64 converts arbitrary bytes into a text-safe representation. It is an encoding scheme, not a confidentiality mechanism.

## Approach

Inspect the data and decode it with:

```bash
base64 -d data.txt
```

## Why it works

Base64 represents groups of bytes using a restricted alphabet. Decoding reverses that representation.

## Security relevance

Encoded values appear in:

- HTTP data
- authentication headers
- email
- configuration files
- malware samples
- API payloads
- forensic artifacts

## Critical distinction

```text
Encoding → representation change
Encryption → confidentiality using a key
Hashing → one-way integrity/password-verification primitive
```

Confusing these concepts is a common security mistake.

## Investigation habit

Before decoding, ask:

1. What makes me think this is Base64?
2. Does the decoded output have a sensible structure?
3. Could the result itself be another encoding or compression layer?

---

# Level 11 → 12 — Character substitution / ROT-style transformation

## Objective

Recover readable text from a string where characters have been systematically substituted.

## Concept

**Substitution transformations and character sets.**

A classic example is ROT13, where alphabetic characters are shifted by 13 positions.

## Approach

Use `tr` to map one character set to another:

```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt
```

## Why it works

`tr` performs character-by-character translation. It is useful when the transformation is a fixed substitution rather than a cryptographic operation.

## Security relevance

Analysts encounter simple transformations in:

- CTFs
- obfuscated scripts
- malware analysis
- puzzle-like encodings
- protocol artifacts

## Deeper lesson

Do not confuse **obfuscation** with strong protection. A reversible substitution with no secret key is not meaningful confidentiality.

---

# Level 12 → 13 — Reconstruct and inspect transformed data

## Objective

Work through a file that has been repeatedly transformed/compressed and recover the meaningful underlying data.

## Concept

**File identification, hex inspection, decompression, and iterative analysis.**

This is one of the first Bandit levels where the main challenge is not a single command but maintaining a correct model of the artifact as its format changes.

## Core workflow

Start by creating a working copy rather than repeatedly destroying the original:

```bash
mkdir /tmp/bandit12-work
cp data /tmp/bandit12-work/
cd /tmp/bandit12-work
```

Inspect the current representation:

```bash
file data
```

If the representation is presented as hexadecimal text, convert it back to bytes using an appropriate tool such as:

```bash
xxd -r data > decoded
```

Then identify the result again:

```bash
file decoded
```

If `file` reports compression or an archive format, rename the working artifact with the appropriate extension and use the corresponding decompressor. Repeat the cycle.

## The real skill

The process is:

```text
Observe format
    ↓
Choose parser/decoder
    ↓
Transform
    ↓
Identify new format
    ↓
Repeat
```

## Security relevance

This resembles real artifact analysis. A suspicious file may have several layers:

```text
container → compression → encoding → embedded object → payload
```

The correct response is not to guess the entire chain. **Measure the current state after every transformation.**

## Key lesson

`file` is a feedback mechanism, not just a one-time command.

---

# Level 13 → 14 — SSH key authentication

## Objective

Use the supplied private SSH key to authenticate to the next Bandit account.

## Concept

**Public-key authentication.**

SSH can authenticate using a key pair:

```text
Private key  → kept secret
Public key   → placed on the server
```

The private key proves possession of the corresponding key material.

## Approach

Use the provided private key with SSH:

```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```

The exact host/port should come from the challenge instructions.

## Why the `-i` option matters

`-i` specifies the identity/private-key file used by SSH.

## Important operational detail

Private-key permissions can matter. SSH may refuse to use a key that is accessible to other users. A common defensive permission is:

```bash
chmod 600 sshkey.private
```

## Security relevance

SSH keys are foundational for:

- secure administration
- cloud infrastructure
- Git authentication
- automation
- server-to-server access

## Deeper lesson

Authentication is not the same as authorization.

```text
Authentication → Who are you / can you prove possession?
Authorization  → What are you allowed to do?
```

Bandit deliberately makes these concepts concrete.

---

# Level 14 → 15 — Send data to a TCP service

## Objective

Provide the current credential to a local network service listening on a specified TCP port.

## Concept

**TCP sockets and application protocols.**

A port is an endpoint identifier associated with a transport-layer service. The application protocol defines what data must be exchanged.

## Approach

A simple client such as `nc` can connect to the service:

```bash
echo 'INPUT' | nc localhost PORT
```

The challenge-specific secret is intentionally omitted from this public write-up.

## Why it works

The pipeline is:

```text
echo
  ↓
stdin of nc
  ↓
TCP connection
  ↓
server process
  ↓
server response
```

## Security relevance

This develops the same conceptual foundation used when investigating:

- exposed services
- custom TCP protocols
- service banners
- socket behavior
- network troubleshooting

## Critical distinction

A TCP port being open does not tell you everything about the service. You still need to determine:

- what protocol it speaks
- what input it expects
- whether the service is authenticated
- how it responds to malformed input

---

# Level 15 → 16 — TLS-protected service

## Objective

Connect securely to a service that expects TLS rather than plain TCP.

## Concept

**TLS, certificates, encryption, and protocol layering.**

A TCP connection provides transport connectivity. TLS can then provide confidentiality and integrity for the application conversation.

## Approach

Use OpenSSL's client functionality:

```bash
openssl s_client -connect localhost:PORT
```

Then provide the expected challenge input through the established TLS session.

## Why `openssl s_client` is useful

It exposes TLS connection details that a generic TCP client does not necessarily provide, including certificate information and negotiated protocol details.

## Layer model

Think of the connection as:

```text
Application data
      ↓
     TLS
      ↓
     TCP
      ↓
      IP
```

## Security relevance

This is directly relevant to:

- HTTPS troubleshooting
- certificate inspection
- secure service validation
- encrypted protocol analysis
- SOC investigations involving TLS metadata

## Deeper lesson

Encryption changes what an observer can see, but it does not remove the need for authentication, authorization, secure application design, or endpoint security.

---

# Level 16 → 17 — Enumerate a range of local services

## Objective

Identify which service in a specified port range performs the required operation.

## Concept

**Service enumeration and validation.**

This is a miniature version of real network reconnaissance.

## Approach

A targeted connection scan can be performed with a tool such as Nmap in an authorized lab:

```bash
nmap -sV -p PORT_START-PORT_END localhost
```

Then inspect candidate services using the appropriate client, including TLS where required.

## Why `-sV` matters

An open port is only the beginning. Version/service detection attempts to determine what application is actually listening.

## Security relevance

This develops a crucial workflow:

```text
Host discovery
    ↓
Port discovery
    ↓
Service identification
    ↓
Protocol validation
    ↓
Application-specific testing
```

## Deeper lesson

**Scanner output is evidence, not absolute truth.**

If Nmap reports a service, validate it with a protocol-aware interaction where practical.

---

# Level 17 → 18 — Compare two files

## Objective

Determine what changed between two similar files.

## Concept

**Differential analysis.**

The challenge can be solved using:

```bash
diff passwords.old passwords.new
```

## Why this works

`diff` identifies line-level differences between files.

## Security relevance

Differential analysis is useful for:

- configuration review
- incident investigation
- malware-analysis snapshots
- version comparison
- detecting unauthorized changes

## Deeper lesson

Security analysis often becomes easier when you compare:

```text
known-good state
        vs
observed state
```

Rather than trying to understand every line independently, focus on what changed.

## Important caution

A difference is not automatically malicious. It is a lead that requires context.

---

# Level 18 → 19 — Understand remote shell/session behavior

## Objective

Deal with a restricted or unusual remote-shell environment where the normal interactive workflow is affected.

## Concept

**Remote command execution, shell behavior, and session assumptions.**

A common mistake is assuming that every SSH connection gives exactly the same interactive environment.

## Approach

First test simple command execution explicitly:

```bash
ssh user@host 'command'
```

This demonstrates an important distinction between:

```text
interactive login shell
```

and:

```text
remote command execution
```

## Why this matters

SSH can transport commands without requiring the same interactive terminal behavior you normally expect.

## Security relevance

This matters when troubleshooting:

- restricted shells
- forced commands
- automation accounts
- bastion hosts
- CI/CD runners
- remote administration

## Deeper lesson

When a tool behaves unexpectedly, question your assumptions about the environment:

- What shell is running?
- Is a TTY allocated?
- What environment variables exist?
- What command is actually being executed?
- Are login scripts changing behavior?

This is a general troubleshooting skill, not just a Bandit trick.

---

# Level 19 → 20 — Setuid and privilege boundaries

## Objective

Use a supplied setuid executable to perform an action with the executable owner's privileges.

## Concept

**Setuid and privilege boundaries.**

A setuid executable can execute with the effective user ID of its owner rather than simply the identity of the user launching it.

Inspecting permissions may show an `s` in the user-execute position, for example:

```text
-rwsr-xr-x
```

## Approach

First inspect the supplied binary:

```bash
ls -l ./bandit20-do
```

Then determine what it expects and invoke it only within the challenge environment.

## Why this matters

The important distinction is between:

```text
real/effective identity
```

and how an executable's privilege context can change what it is allowed to access.

## Security relevance

Privilege boundaries are central to:

- Linux privilege escalation
- local attack-surface analysis
- secure program design
- permissions auditing
- vulnerability research

## Defensive questions

When auditing a system, ask:

- Which binaries have special permission bits?
- Why do they need elevated privileges?
- Do they safely handle attacker-controlled input?
- Can a privileged process be influenced to perform an unintended action?

## Deeper lesson

A permission bit is not automatically a vulnerability. The security risk depends on **what privileged code does and what input it trusts**.

---

# Level 20 — Current milestone

**Level 20 reached.**

Next target: **20 → 21**.

The progression so far has moved from basic shell interaction into several security-relevant domains:

```text
Filesystem
   ↓
Shell parsing
   ↓
Metadata enumeration
   ↓
Text processing
   ↓
Binary inspection
   ↓
Encoding/transformation
   ↓
SSH authentication
   ↓
TCP services
   ↓
TLS
   ↓
Service enumeration
   ↓
Differential analysis
   ↓
Remote-shell behavior
   ↓
Privilege boundaries
```

That progression is more important than memorizing individual commands.

---

# Cross-level technical lessons

## 1. The shell is a programming environment

Bandit repeatedly demonstrates that the shell is not merely a place to type commands. It provides:

- variables
- processes
- streams
- redirection
- pipelines
- quoting rules
- globbing
- exit codes
- command substitution

Understanding these mechanisms makes security tooling much easier to use correctly.

## 2. Enumeration comes before conclusions

Several levels reinforce:

```text
observe → narrow candidates → validate → conclude
```

That is the same reasoning model used in penetration testing and SOC investigations.

## 3. Tool output needs interpretation

`file`, `grep`, `find`, `nmap`, `strings`, and `diff` produce observations. They do not replace analysis.

A mature workflow asks:

> What does this output prove, and what does it not prove?

## 4. Small Unix tools compose into workflows

Examples:

```bash
sort | uniq
strings | grep
find ... 2>/dev/null
```

This composability is one reason command-line fluency is valuable in cybersecurity.

## 5. Security is about boundaries

Bandit repeatedly exposes boundaries:

- filename versus option
- shell syntax versus data
- hidden versus protected
- file label versus actual format
- stdout versus stderr
- authenticated versus authorized
- TCP versus TLS
- open port versus identified service
- normal user versus privileged execution

Recognizing boundaries is a core security skill.

---

# Bandit competency map

| Bandit skill | Broader cybersecurity use |
|---|---|
| `pwd`, `ls`, `cat` | Linux administration and artifact inspection |
| Quoting and `./` | Secure shell usage and argument handling |
| Hidden-file discovery | Configuration and artifact enumeration |
| `file` | Forensic triage and file identification |
| `find` | Filesystem enumeration and hunting |
| stdout/stderr | Shell automation and troubleshooting |
| `grep` | Log analysis and IOC searching |
| `sort` / `uniq` | Data reduction and anomaly triage |
| `strings` | Binary/malware triage |
| Base64 decoding | Artifact and protocol analysis |
| `tr` | Transformation and obfuscation analysis |
| `xxd` | Hex/byte-level inspection |
| Compression handling | Artifact reconstruction |
| SSH keys | Secure authentication and administration |
| `nc` | TCP service understanding |
| `openssl s_client` | TLS/service troubleshooting |
| Nmap service detection | Authorized network enumeration |
| `diff` | Configuration and forensic comparison |
| SSH remote commands | Remote administration and restricted environments |
| SUID | Privilege-boundary analysis |

---

# What I should be able to do after Level 20

I should not define completion as:

> I remember the commands.

Instead, I should be able to:

### Explain
Describe the relevant Linux/network/security concept without a walkthrough.

### Perform
Reproduce the technique in an authorized lab.

### Troubleshoot
Diagnose why the expected output did not appear.

### Generalize
Apply the concept to a new problem rather than the exact Bandit challenge.

### Document
Write a concise technical record containing objective, observation, method, result, security relevance, and lesson learned.

---

# Connection to the Cybersecurity Roadmap

Bandit is evidence for the following competencies:

- Linux command-line fluency
- filesystem enumeration
- permissions and privilege boundaries
- shell troubleshooting
- text/data processing
- basic network-service interaction
- SSH authentication
- protocol awareness
- security-oriented problem solving

The next step is to deliberately transfer these skills into:

1. Linux administration labs
2. authorized network enumeration
3. eJPT-style penetration-testing labs
4. SOC/log-analysis exercises
5. small Python automation projects

That transfer is where CTF knowledge becomes professional capability.

---

# Public documentation rule

This repository records **learning and evidence**, not secrets.

Never publish:

- Bandit passwords
- private SSH keys
- API keys
- access tokens
- production credentials
- private IP/topology details that should remain confidential
- copied proprietary data

The public version should demonstrate reasoning and technical skill without creating a credential or information-disclosure problem.

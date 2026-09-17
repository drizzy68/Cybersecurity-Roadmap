# 🥷 OverTheWire Bandit

Bandit is my Linux/security problem-solving track. The objective is to become comfortable reading a problem, inspecting an unfamiliar environment, selecting the right command, interpreting failure and adapting the approach.

## Current progress

**Level 20 reached**  
**Next challenge: 20 → 21**

## Skills developed

### Linux and shell

- filesystem navigation
- hidden files
- filenames containing special characters
- permissions
- `find`
- pipelines
- stdout/stderr
- text processing

### Data handling

- `grep`
- `sort`
- `uniq`
- `strings`
- `tr`
- encoding/decoding
- compression
- binary-file identification

### Networking

- SSH
- TCP service interaction
- TLS with `openssl`
- reading service behavior

### Security reasoning

- setuid/privilege boundaries
- trust assumptions
- local enumeration
- protocol-specific interaction
- troubleshooting

## Documentation model

Each challenge is documented as:

```text
Objective
   ↓
Known information
   ↓
Hypothesis
   ↓
Command / technique
   ↓
Observed result
   ↓
Why it worked
   ↓
Security concept
   ↓
Transferable lesson
```

The detailed write-up is [`levels-0-20.md`](levels-0-20.md).

## What is intentionally not here

Challenge passwords and other reusable secrets are not part of the public repository.

The point of the write-up is to preserve the **reasoning**, not the secret answer.

## From CTF to real capability

Bandit concepts should feed the canonical Linux material under [`01-foundations/linux`](../../../01-foundations/linux/README.md), while challenge-specific observations stay here.

That separation prevents the CTF section from becoming a duplicate Linux command encyclopedia.

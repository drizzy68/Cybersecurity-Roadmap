# 04 — CTF Training

CTFs are used here to develop technical problem-solving, not just challenge completion.

## What a CTF should teach

A challenge should produce a transferable skill:

- command-line fluency
- protocol reasoning
- encoding/decoding
- enumeration
- debugging
- web-security reasoning
- binary analysis
- cryptographic reasoning
- privilege-boundary analysis

## Challenge workflow

```text
Read objective
   ↓
Identify known information
   ↓
Form hypothesis
   ↓
Test smallest useful idea
   ↓
Inspect output
   ↓
Revise hypothesis
   ↓
Solve
   ↓
Extract transferable lesson
   ↓
Document
```

## Current track

### OverTheWire — Bandit

Current milestone: **Level 20 reached**.

→ [`Bandit README`](overthewire/bandit/README.md)

→ [`Levels 0–20 write-up`](overthewire/bandit/levels-0-20.md)

## CTF documentation standard

For each challenge record:

1. Objective
2. What was known
3. Hypothesis
4. Commands/technique
5. Why it worked
6. Failure or dead end, if useful
7. Security concept
8. Transferable lesson

Never publish passwords, tokens or other challenge secrets when the same educational value can be shown without them.

## CTF-to-career mapping

CTF skill should feed the wider roadmap:

```text
CTF lesson
   ↓
Underlying technical concept
   ↓
Foundation / offensive / defensive topic
   ↓
Independent lab
   ↓
Portfolio evidence
```

This prevents the CTF section from becoming a disconnected collection of walkthroughs.

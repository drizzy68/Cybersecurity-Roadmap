# 07 — Digital Forensics & Incident Response

DFIR is a long-term specialization. It combines operating-system knowledge, networking, evidence handling, timeline analysis and incident-response reasoning.

## 1. Forensic mindset

The central question is not simply **"What happened?"** but:

**What evidence supports that conclusion, what alternative explanations exist, and what remains unknown?**

Preserve evidence, record provenance, normalize time, avoid unnecessary modification and distinguish facts from hypotheses.

## 2. Windows artifacts

Study the security value of:
- Windows Event Logs
- authentication records
- process/service activity
- scheduled tasks
- PowerShell activity
- browser/application artifacts
- filesystem metadata
- persistence-related locations
- Active Directory-related evidence

Learn what each artifact can and cannot prove.

## 3. Linux artifacts

Study:
- authentication logs
- system logs
- shell history
- scheduled jobs
- service configuration
- filesystem metadata
- SSH-related records
- process/network state

## 4. Evidence handling

For every evidence item, record:
- source
- acquisition time
- original state where known
- hash/integrity information where appropriate
- analyst action
- storage location
- transformation or parsing performed

Do not alter original evidence unnecessarily.

## 5. Timeline construction

A useful timeline combines multiple evidence sources.

Recommended fields:

`timestamp | source | host | user | process | action | artifact | interpretation | confidence`

Before correlating events, identify timezone, clock-skew and timestamp-format assumptions.

## 6. Investigation workflow

**Prepare → Acquire → Triage → Correlate → Build timeline → Form hypothesis → Test hypothesis → Determine scope → Report → Lessons learned**

A hypothesis should be revised when evidence contradicts it.

## 7. Example training case

Create a safe isolated scenario containing:
- a normal login
- a failed-login sequence
- a new process
- a network connection
- a modified file

Then investigate the case without being told the answer. Build a timeline and identify which observations are facts and which are interpretations.

## 8. Memory and disk concepts

Later study:
- volatile vs non-volatile evidence
- memory acquisition concepts
- process/network artifacts in memory
- disk images
- file carving concepts
- deleted-file recovery concepts
- filesystem metadata

Move into dedicated forensic tooling only after the underlying artifacts are understood.

## 9. Reporting

A DFIR report should communicate:
- incident/question
- scope
- evidence sources
- methodology
- timeline
- findings
- confidence/limitations
- impact
- recommended response
- unresolved questions

## Definition of done

A DFIR capability is mature when I can preserve relevant evidence, identify appropriate artifacts, build a defensible timeline, test competing explanations and communicate findings with explicit limitations.

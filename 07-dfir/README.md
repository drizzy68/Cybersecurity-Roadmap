# 07 — DFIR

Digital Forensics and Incident Response (DFIR) is a long-term specialization built on the foundations in networking, Linux, Windows and the SOC track.

The central discipline is **preserving evidence while reconstructing what happened**.

## DFIR mental model

```text
Question
  ↓
Identify relevant evidence
  ↓
Preserve / acquire safely
  ↓
Validate integrity and provenance
  ↓
Extract artifacts
  ↓
Normalize timestamps
  ↓
Build timeline
  ↓
Correlate evidence
  ↓
Form and test hypotheses
  ↓
Document findings and limitations
```

## Learning path

### 1. Operating-system artifacts

Start with Windows and Linux because endpoint artifacts are central to many investigations.

- Users and accounts
- Processes
- Services
- Filesystem metadata
- Authentication records
- Shell history
- Scheduled execution
- Network connections
- Application artifacts

### 2. Event and log analysis

Understand:

- What generated an event
- Which fields are important
- Timestamp semantics
- Host/user/process relationships
- Missing or incomplete telemetry
- Normal activity versus suspicious sequences

### 3. Evidence handling

Learn the concepts of:

- Acquisition
- Preservation
- Hashing/integrity
- Chain of custody
- Original evidence versus working copies
- Documentation of actions

### 4. Timeline analysis

A useful timeline answers:

- What happened first?
- What changed?
- Which account was involved?
- Which process created or modified the artifact?
- What network activity followed?
- What evidence supports each conclusion?

### 5. Incident investigation

Combine endpoint artifacts, logs and network evidence to investigate a bounded scenario.

## Investigation standard

Every conclusion should be classified as:

- **Observed** — directly supported by evidence.
- **Inferred** — strongly supported but not directly observed.
- **Possible** — plausible but insufficiently supported.
- **Unknown** — evidence is missing or contradictory.

This prevents overclaiming.

## Future portfolio artifacts

- Windows artifact investigation
- Authentication timeline
- Suspicious PowerShell investigation
- Endpoint/network correlation exercise
- Disk or memory forensics lab
- Full incident report

DFIR project pages should document actual investigations. The conceptual material belongs here so it does not get duplicated across project reports.

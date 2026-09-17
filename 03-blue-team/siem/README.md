# 📊 SIEM Fundamentals

A SIEM centralizes or analyzes security-relevant telemetry so analysts can search, correlate and investigate activity.

## Core concepts

### Event
A record of activity.

### Alert
A signal generated because activity matched a rule, threshold, analytic or other condition.

### Detection
Logic intended to identify a behavior or condition of security interest.

### Case
A collection of alerts, evidence, notes and actions around an investigation.

## Normalization

Different systems represent similar concepts differently. SIEM pipelines often parse and normalize fields such as:

- timestamp
- username
- source IP
- destination IP
- hostname
- process name
- event type
- action/result

Without normalization, correlation becomes difficult.

## Query thinking

A good investigation query answers a question.

Bad approach:

> Search everything and hope something interesting appears.

Better approach:

```text
Question
  ↓
Relevant entities
  ↓
Time window
  ↓
Relevant event sources
  ↓
Query
  ↓
Validate result
  ↓
Expand investigation
```

## Correlation

Useful correlations combine multiple weak signals into a stronger sequence.

Example reasoning:

```text
Unusual authentication
        +
New process on same host
        +
Unexpected outbound connection
        ↓
Investigate as one timeline
```

This does not automatically prove malicious activity. It creates a higher-value investigation hypothesis.

## False positives

A detection can fire on legitimate behavior.

Tuning should ask:

- Which condition creates noise?
- What context distinguishes benign from suspicious activity?
- Can the rule use identity, asset role or process context?
- What attacks could the tuning accidentally hide?

## Investigation record

Document:

- initial alert
- hypothesis
- queries
- evidence
- findings
- confidence
- containment/escalation decision
- next action

### Competency gate

I should be able to translate an alert into investigation questions, query relevant telemetry, correlate events, recognize false positives and document a defensible conclusion.

# 🚨 Incident Response

Incident response is a structured process for detecting, analyzing and managing security incidents while preserving evidence and restoring normal operations.

## Lifecycle

```text
Preparation
   ↓
Detection & Analysis
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Lessons Learned
```

Real incidents are iterative. Analysts may return to detection and analysis as new evidence appears.

## Triage

First establish:

- What happened?
- Which systems are affected?
- Which accounts are involved?
- When did it begin?
- Is activity ongoing?
- What evidence exists?
- What is the immediate risk?

## Scoping

Determine whether the activity is isolated or part of a broader sequence.

Look for relationships between:

- users
- endpoints
- processes
- IP addresses
- domains
- authentication events
- file changes
- persistence mechanisms

## Containment

Containment aims to limit further harm while preserving investigation value.

Examples may include isolation, credential controls, blocking indicators or restricting access, depending on incident context and authorization.

Avoid destructive actions that unnecessarily destroy evidence.

## Eradication and recovery

Remove the underlying cause, restore trusted systems, reset compromised credentials as appropriate, validate controls and monitor for recurrence.

## Documentation

Every major action should have:

- timestamp
- person/system performing it
- reason
- result
- evidence affected

## Lessons learned

After recovery ask:

- Why was the activity possible?
- Why did detection trigger or fail?
- Which control worked?
- Which control failed?
- What telemetry was missing?
- What should be changed?
- How will the change be validated?

### Competency gate

I should be able to triage a bounded incident, scope affected entities, preserve evidence, recommend containment, construct a timeline and write a clear incident report.

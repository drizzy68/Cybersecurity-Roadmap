# 🧠 Detection Engineering

Detection engineering converts security knowledge into repeatable signals that can identify behavior worth investigating.

## Start with behavior

A useful detection answers:

> **What behavior do I want to identify, and what observable evidence would demonstrate it?**

Avoid beginning with a tool-specific query before defining the behavior.

## Detection lifecycle

```text
Threat / risk
   ↓
Behavior hypothesis
   ↓
Available telemetry
   ↓
Detection logic
   ↓
Test with known scenarios
   ↓
Measure noise / coverage
   ↓
Tune
   ↓
Deploy
   ↓
Monitor
```

## Examples of detection objectives

- suspicious authentication patterns
- unusual privileged account activity
- unexpected process execution
- suspicious PowerShell behavior
- unexpected persistence mechanisms
- anomalous outbound network activity

These are objectives, not automatic conclusions of maliciousness.

## Detection quality

Evaluate:

- precision
- false-positive rate
- coverage
- context available to the analyst
- time to investigate
- resilience to small behavior changes
- telemetry dependencies

## Testing

A detection should be tested in an authorized lab using known benign and simulated suspicious activity.

Record:

- test scenario
- expected signal
- actual signal
- false positives
- missing telemetry
- tuning changes

## Analyst usability

A technically correct alert can still be operationally poor if the analyst receives no useful context.

A good alert should expose enough information to answer:

- what happened?
- where?
- when?
- who?
- what process or resource was involved?
- what should the analyst investigate next?

### Competency gate

I should be able to define a detection objective, identify required telemetry, build/test a simple detection, evaluate noise and document limitations.

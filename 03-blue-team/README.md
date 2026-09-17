# 03 — Blue Team / SOC

This section contains the canonical defensive-security knowledge used to investigate activity, triage alerts, detect threats and communicate incidents.

The SOC mindset is **evidence first**: establish what happened, when it happened, which systems/accounts were involved, what evidence supports the conclusion, and what action is justified.

## Investigation lifecycle

```text
Alert / Signal
      ↓
Validate
      ↓
Scope
      ↓
Collect Evidence
      ↓
Correlate
      ↓
Form Hypotheses
      ↓
Test Hypotheses
      ↓
Contain / Escalate
      ↓
Document
      ↓
Improve Detection
```

## Canonical topics

### 🧾 Logs

- Windows Event Logs
- Linux logs and journald
- Authentication events
- Process and service activity
- Network/security telemetry
- Log fields, timestamps and context
- Normal vs suspicious activity

→ [`Logs`](logs/README.md)

### 📊 SIEM

- Events vs alerts
- Parsing and normalization
- Search/query thinking
- Correlation
- Detection rules
- False positives and false negatives
- Investigation timelines

→ [`SIEM`](siem/README.md)

### 🚨 Incident Response

- Preparation
- Detection and analysis
- Triage
- Scoping
- Containment
- Eradication and recovery
- Evidence preservation
- Lessons learned

→ [`Incident Response`](incident-response/README.md)

### 🧠 Detection Engineering

- Detection objectives
- Observable behavior
- Authentication detections
- Process and PowerShell detections
- Network indicators
- Alert quality
- Validation and tuning

→ [`Detection`](detection/README.md)

---

## Core SOC questions

For every alert, ask:

1. **What exactly triggered the signal?**
2. **Is the event real, expected or ambiguous?**
3. **Which user, host, process, IP or application is involved?**
4. **What happened immediately before and after?**
5. **Is there evidence of persistence, privilege change or lateral movement?**
6. **What additional telemetry can confirm or reject the hypothesis?**
7. **What action is justified by the evidence?**
8. **What should be documented for another analyst?**

## SOC competency gate

A topic is not complete because I can identify an Event ID or write a query. I should be able to:

**Observe → Interpret → Correlate → Investigate → Explain → Document**

The detailed technical explanation belongs in the canonical topic pages. Project pages should contain the actual investigation evidence, not duplicate the textbook material.

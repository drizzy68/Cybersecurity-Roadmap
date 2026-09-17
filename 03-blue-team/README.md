# 03 — Blue Team / SOC

Blue Team / SOC is the primary employability direction of this roadmap. The objective is to become capable of receiving security telemetry, determining whether activity is benign or suspicious, investigating scope and cause, and communicating the result clearly.

## 1. SOC mental model

A SOC turns telemetry into decisions:

**Telemetry → Detection → Alert → Triage → Investigation → Scope → Response/Escalation → Recovery → Lessons learned**

A good analyst does not blindly trust an alert. The analyst validates the signal against evidence and context.

## 2. Windows security foundations

Study:
- Windows processes and services
- accounts and groups
- authentication concepts
- Event Viewer
- PowerShell
- scheduled tasks
- network connections
- endpoint security concepts
- Active Directory basics

### Investigation questions
- Which account acted?
- Which host was involved?
- What process or service generated the activity?
- When did it occur?
- What happened immediately before and after?
- Is the behavior expected for this user/host?
- What other systems or events are associated with it?

## 3. Linux telemetry

Learn:
- authentication logs
- system/service logs
- process activity
- SSH activity
- scheduled tasks
- file permissions
- network connections

Practice identifying normal administration versus anomalous behavior in a controlled lab.

## 4. SIEM fundamentals

Understand the pipeline:

**Source → Collection → Parsing → Normalization → Indexing → Query → Detection → Alert → Investigation**

Learn the difference between:
- raw event
- normalized field
- search/query
- detection rule
- alert
- incident

Practice filtering by time, host, user, source IP, destination IP, process and event type.

## 5. Alert triage

For every alert:

1. Read the detection logic.
2. Confirm the timestamp and affected asset.
3. Identify the user/process/network context.
4. Determine whether the activity is plausible.
5. Search surrounding events.
6. Correlate related hosts/accounts/IPs.
7. Decide whether to close, escalate or investigate further.
8. Document the reasoning.

The important evidence is not just the final disposition; it is why the disposition was reached.

## 6. Detection engineering fundamentals

Learn to distinguish:
- indicator vs behavior
- signature vs analytic detection
- high-fidelity vs noisy rules
- detection coverage vs alert volume
- false positive vs true positive

A useful detection should specify:
- data source
- event condition
- relevant fields
- threshold/time window where applicable
- expected false positives
- investigation steps
- response/escalation guidance

## 7. Incident response

Use a repeatable lifecycle:

**Preparation → Identification → Containment → Eradication → Recovery → Lessons learned**

For training cases, document what evidence justified each transition. Preserve evidence before changing the environment when practical.

## 8. Timeline analysis

Build timelines from multiple sources rather than relying on a single log.

Useful fields:
- timestamp
- host
- user
- process
- source/destination
- event type
- action
- evidence source
- confidence

Normalize timestamps and timezone assumptions before drawing conclusions.

## 9. Threat intelligence

Learn the distinction between:
- IOC: observable artifact such as a hash, domain or IP
- TTP: behavior or technique used by an adversary
- context: information that explains why an indicator matters

Avoid treating an IOC alone as proof of compromise. Correlate it with endpoint, network and authentication evidence.

## 10. Portfolio labs

Build progressively:

### Lab A — Windows authentication investigation
Generate normal and failed authentication activity in an isolated lab, identify relevant events, construct a timeline and explain the conclusion.

### Lab B — Suspicious PowerShell investigation
Generate safe test activity, inspect PowerShell and process telemetry, identify the parent process and user context, and document what evidence would distinguish benign administration from suspicious execution.

### Lab C — Network alert triage
Investigate a simulated connection alert using packet capture and host context.

### Lab D — Mini SOC case
Combine authentication, endpoint and network events into one incident narrative.

## Definition of done

A SOC topic is complete when I can **identify the relevant telemetry, form a hypothesis, query evidence, correlate events, explain uncertainty, reach a defensible disposition, and document the investigation**.

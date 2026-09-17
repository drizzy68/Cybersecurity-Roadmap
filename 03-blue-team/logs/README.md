# 🧾 Logs & Telemetry

Logs are records of system or application activity. Security analysis depends on understanding what generated an event, what fields mean and how events relate across time.

## Event anatomy

For each event identify:

- timestamp
- host
- user/account
- process/service
- action
- source/destination
- result
- event identifier/type
- surrounding context

## Windows

Important sources include:

- Security
- System
- Application
- PowerShell telemetry
- Task Scheduler/service-related logs

Do not memorize Event IDs in isolation. Understand the activity represented by the event and correlate it with other telemetry.

## Linux

Depending on distribution and configuration, useful sources include:

- `/var/log/auth.log` or equivalent
- `/var/log/syslog` or equivalent
- systemd journal
- service-specific logs
- application logs

Useful inspection:

```bash
journalctl -b
journalctl -u <service>
```

## Normal versus suspicious

A security analyst needs a baseline.

The same event can be:

- normal administrative activity
- expected automation
- unusual but legitimate
- suspicious
- clearly malicious

Context changes interpretation.

## Timeline reasoning

Build a sequence rather than isolated facts:

```text
Authentication
   ↓
Process creation
   ↓
File/configuration change
   ↓
Network connection
   ↓
Persistence / privilege change
```

Not every incident follows this exact sequence. It is a reasoning model, not a rigid template.

## Common mistakes

- Treating a single event as proof of compromise
- Ignoring time zones
- Ignoring clock skew
- Ignoring service accounts
- Ignoring scheduled automation
- Failing to preserve original evidence
- Searching only for known attack names instead of behavior

### Competency gate

I should be able to locate relevant logs, explain their fields, establish a timeline, distinguish evidence from interpretation and identify what additional telemetry is required when the evidence is incomplete.

# ⬆️ Privilege Escalation

Privilege escalation is the process of obtaining capabilities beyond the privileges initially granted to an account or process.

The correct mindset is **enumerate → identify a trust boundary → form a hypothesis → validate safely**.

## Linux methodology

Start with:

```bash
id
uname -a
sudo -l
ps aux
ss -tulpn
find / -perm -4000 -type f 2>/dev/null
```

Then investigate:

- sudo permissions
- SUID/SGID programs
- writable files/scripts executed by privileged users
- services and startup mechanisms
- scheduled tasks
- environment/configuration mistakes
- credentials exposed in authorized lab artifacts
- kernel/software versions only when there is a justified hypothesis

The goal is not to run every possible privilege-escalation script. The goal is to understand **why a boundary is weak**.

## Windows methodology

Establish:

- current identity
- group memberships
- privileges
- running services
- scheduled tasks
- installed software
- writable locations
- service configurations
- registry/configuration exposure
- credential material in authorized labs

Useful inspection commands include:

```powershell
whoami /all
Get-Process
Get-Service
Get-ScheduledTask
```

## Trust-boundary questions

For any candidate:

1. Who owns the resource?
2. Who can modify it?
3. Who executes it?
4. Under which identity does it execute?
5. Can a lower-privileged identity influence its behavior?
6. Is the behavior deterministic and reproducible?
7. What is the security consequence?

## Common root-cause classes

- Excessive permissions
- Unsafe service configuration
- Writable privileged execution path
- Weak scheduled-task permissions
- Credential exposure
- Dangerous interpreter configuration
- Vulnerable software
- Misconfigured administrative delegation

## Evidence

Document the minimum evidence necessary to demonstrate the boundary failure. Avoid unnecessary destructive actions.

A strong finding explains:

```text
Initial privilege
      ↓
Weak boundary
      ↓
Controlled validation
      ↓
Higher privilege demonstrated
      ↓
Root cause
      ↓
Remediation
```

### Competency gate

I should be able to enumerate local privilege boundaries on Linux and Windows, identify plausible escalation paths, validate them safely in an authorized lab, explain the root cause and propose a concrete fix.

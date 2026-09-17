# 🪟 Windows Fundamentals for Cybersecurity

Windows is central to enterprise security operations. The goal is to understand the operating system well enough to administer it, interpret its telemetry and investigate security events.

## 1. Accounts and security principals

Understand:

- Local users
- Local groups
- Administrators
- Standard users
- Service accounts
- Security identifiers (SIDs)
- Access tokens

A security investigation often starts by asking **which identity performed an action** and what privileges that identity had.

Useful commands:

```powershell
whoami
whoami /all
whoami /groups
Get-LocalUser
Get-LocalGroup
```

## 2. Processes and services

Processes represent executing programs. Services provide background functionality and may start automatically.

Useful PowerShell commands:

```powershell
Get-Process
Get-Service
Get-CimInstance Win32_Service
```

Security questions:

- Which process started?
- Which account owns it?
- What command line launched it?
- Which service configured the startup?
- What network connections does it make?

## 3. Filesystem and NTFS concepts

Understand:

- Volumes and drive letters
- NTFS permissions
- ACLs
- File ownership
- Alternate data streams as a forensic concept
- Timestamps and metadata

Permissions should be analyzed as an access-control model, not merely as a list of checkboxes.

## 4. Event Logs

Windows records many security-relevant activities in Event Logs.

Important channels include:

- Security
- System
- Application
- PowerShell-related logs
- Task Scheduler and service-related telemetry

The important skill is correlation. One event rarely tells the complete story.

Example investigation questions:

```text
Who authenticated?
From where?
When?
Was the authentication successful?
What happened immediately afterward?
Did a process or privilege change follow?
```

## 5. PowerShell

PowerShell is both an administration platform and a security telemetry source.

Core concepts:

- Objects rather than plain text pipelines
- Cmdlets
- Parameters
- Providers
- Modules
- Remoting
- Execution policy concepts
- Logging and telemetry

Useful commands:

```powershell
Get-Help Get-Process
Get-Command
Get-Process | Sort-Object CPU -Descending
Get-WinEvent -LogName Security -MaxEvents 20
```

PowerShell commands should be treated as code: understand them before executing them.

## 6. Authentication

At a high level, authentication establishes identity; authorization determines what that identity is allowed to do.

Understand:

- Password authentication
- NTLM concepts
- Kerberos concepts
- MFA
- Account lockout
- Service accounts
- Credential storage risks

## 7. Active Directory

AD is a directory and identity platform used in Windows domains.

Core concepts:

- Domain
- Domain controller
- Users
- Groups
- Organizational Units (OUs)
- Group Policy Objects (GPOs)
- DNS dependency
- Kerberos
- LDAP
- Trust relationships

The key security idea is that identity and administrative delegation create a graph of privilege relationships.

## 8. GPO

Group Policy allows administrators to centrally apply configuration and security settings.

Security questions include:

- Who can modify the policy?
- Which computers/users receive it?
- What settings does it enforce?
- Could a misconfiguration grant excessive privilege?

## 9. Kerberos and LDAP

Kerberos provides ticket-based authentication in Active Directory environments. LDAP provides directory access and query functionality.

Do not reduce either protocol to a port number. Understand the identities, tickets, directory objects and trust relationships involved.

## 10. Windows security investigation

A useful investigation sequence is:

```text
Identity
  ↓
Authentication
  ↓
Process / service activity
  ↓
File or registry change
  ↓
Network activity
  ↓
Persistence / privilege change
```

The exact sequence varies by incident. The model prevents tunnel vision around a single event.

## 11. Troubleshooting model

When a Windows service or application fails:

1. Confirm the symptom.
2. Check service/process state.
3. Check local configuration.
4. Check DNS/network dependencies.
5. Check permissions and identity.
6. Inspect relevant Event Logs.
7. Reproduce safely.
8. Change one variable at a time.
9. Record the root cause and fix.

### Competency gate

I should be able to administer a small Windows environment, use PowerShell for inspection, interpret authentication/process/service logs, explain AD fundamentals, and investigate a bounded suspicious activity scenario.

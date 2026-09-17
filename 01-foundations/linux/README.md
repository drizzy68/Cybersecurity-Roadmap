# 🐧 Linux Fundamentals for Cybersecurity

Linux knowledge is a prerequisite for understanding security tooling, servers, containers, privilege boundaries and many CTF environments.

## 1. Shell fundamentals

The shell is a command interpreter. It reads commands, expands them, launches programs and connects their input/output streams.

Core commands:

```bash
pwd
ls -la
cd /path
cat file
less file
head file
tail file
mkdir dir
cp source destination
mv source destination
rm file
```

The important skill is not memorizing syntax. It is understanding **what program receives what arguments and where its output goes**.

## 2. Pipes and redirection

Standard streams:

- stdin: input
- stdout: normal output
- stderr: error/diagnostic output

Examples:

```bash
command > output.txt
command >> output.txt
command 2> errors.txt
command > output.txt 2>&1
command1 | command2
```

A pipeline sends stdout from one command to stdin of another.

## 3. Filesystem model

Important directories include:

- `/etc` — configuration
- `/var/log` — logs
- `/home` — user home directories
- `/tmp` — temporary files
- `/usr/bin` — many user commands
- `/bin` — essential commands on many systems
- `/proc` — process/kernel information interface
- `/sys` — kernel/device information interface

The filesystem is part of the security model. Configuration, logs, credentials and executables all have different access requirements.

## 4. Users, groups and permissions

Linux permissions are represented for owner, group and others.

Example:

```text
-rwxr-x---
```

Conceptually:

```text
owner  → rwx
 group → r-x
other  → ---
```

Important commands:

```bash
id
whoami
ls -l
chmod
chown
chgrp
sudo
```

### Security relevance

Privilege escalation frequently involves discovering where a lower-privileged identity can influence something executed with higher privileges.

## 5. SUID and privilege boundaries

A SUID executable can run with the file owner's effective identity. This is a legitimate Unix mechanism but becomes security-sensitive when a privileged executable is incorrectly configured or exposes an unintended execution path.

Inspect authorized lab systems with:

```bash
find / -perm -4000 -type f 2>/dev/null
```

The output is only a starting point. Each candidate must be understood in context.

## 6. Processes and services

Processes represent running programs. Services are long-running processes managed by mechanisms such as systemd.

Useful commands:

```bash
ps aux
top
pgrep <name>
kill <PID>
systemctl status <service>
systemctl list-units --type=service
```

Security questions include:

- What is running?
- Which user owns it?
- What files does it access?
- What ports does it expose?
- How does it start?
- What configuration controls it?

## 7. Network visibility

Useful commands:

```bash
ip addr
ip route
ss -tulpn
ip neigh
```

`ss` is particularly useful for mapping listening sockets to local services.

## 8. SSH

SSH provides encrypted remote administration.

Important concepts:

- Host keys
- User authentication
- Public/private key pairs
- `authorized_keys`
- File permissions
- Agent forwarding
- Configuration and logging

Never place private keys or passwords in a public repository.

## 9. Package management

Use the package manager appropriate to the distribution. On Debian-based systems:

```bash
apt update
apt upgrade
apt install <package>
apt remove <package>
```

Security reasoning includes understanding package sources, update state, dependency changes and whether software is actually required.

## 10. Logs

Linux logging commonly involves files under `/var/log` and systemd's journal on systems using systemd.

Useful commands:

```bash
journalctl
journalctl -b
journalctl -u <service>
```

Logs should be interpreted with timestamps, process/service context and the surrounding event sequence.

## 11. Bash scripting

A useful security script should have:

- clear input expectations
- predictable output
- error handling
- safe quoting
- logging where appropriate
- least-privilege assumptions
- a clear failure mode

Example pattern:

```bash
#!/usr/bin/env bash
set -euo pipefail

file="${1:-}"
if [[ -z "$file" || ! -f "$file" ]]; then
    echo "Usage: $0 <file>" >&2
    exit 1
fi

grep -n "ERROR" -- "$file"
```

## 12. Troubleshooting model

When a command fails:

1. Read the error literally.
2. Check syntax and arguments.
3. Confirm the file/path exists.
4. Check permissions.
5. Check environment variables/PATH.
6. Check process/service state.
7. Check network dependencies.
8. Search relevant logs.
9. Reproduce in the smallest safe test.
10. Record the root cause.

### Competency gate

I should be able to navigate a Linux system, inspect users/processes/services/network sockets, explain permissions and SUID, read logs, troubleshoot common failures, and write small safe shell scripts without relying on copy/paste.

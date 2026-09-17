# 🧭 Enumeration

Enumeration is the process of turning reachable assets into detailed knowledge about services, applications, identities and behavior.

## 1. Host discovery

Determine which authorized systems respond to appropriate discovery methods.

Do not assume:

- a non-response means a host does not exist
- a response means the host is safe
- a scanner has perfect visibility

Firewalls, filtering, routing and host configuration affect results.

## 2. Port discovery

Port scanning asks which transport endpoints appear reachable.

Interpret results as observations:

- open: a service appears to be accepting connections
- closed: the host responded but no service accepted the connection
- filtered: filtering prevented a clear conclusion

The exact scanner state terminology depends on the tool and scan method.

## 3. Service identification

A port number is only a clue. Identify the application through authorized protocol interaction and version information where available.

Questions:

- What service is actually present?
- Is it expected?
- What version/configuration is visible?
- Is encryption used?
- What authentication is required?
- What information is unnecessarily exposed?

## 4. Service-specific enumeration

Once a service is identified, use its protocol knowledge.

Examples:

- DNS → records and zone behavior within scope
- SMB → shares and security configuration
- HTTP → paths, methods, headers, authentication and application behavior
- SSH → authentication configuration and exposed metadata
- LDAP → directory structure and access controls in an authorized lab

## 5. Web enumeration

A web application should be mapped by functionality rather than only by URL count.

Record:

```text
Endpoint
Method
Parameters
Authentication state
Authorization context
Response
Observed behavior
Security question
```

Compare behavior as different authorized users when testing access control.

## 6. Validation

Enumeration creates hypotheses. Validate important observations.

For example:

```text
Scanner says port 443 is open
        ↓
Connect using a protocol-aware client
        ↓
Inspect TLS/certificate
        ↓
Identify HTTP behavior
        ↓
Confirm application
```

This avoids treating automated fingerprints as ground truth.

## 7. Enumeration notebook

For every finding, preserve:

- target
- time
- technique
- result
- confidence
- next action

### Competency gate

I should be able to discover authorized hosts, identify services, perform service-specific enumeration, validate automated results and turn observations into useful attack-surface hypotheses.

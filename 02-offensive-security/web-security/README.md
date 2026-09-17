# 🌐 Web Application Security

Web security is primarily about understanding how an application handles **identity, input, state, data and authorization**.

## Request/response model

A browser or client sends a request. The server processes it and returns a response.

Understand:

- method
- URL/path
- query parameters
- headers
- cookies
- body
- status code
- response headers
- response body

Before testing a vulnerability, learn what normal behavior looks like.

## Authentication vs authorization

**Authentication:** who are you?

**Authorization:** what are you allowed to do?

Many serious web vulnerabilities occur when the application authenticates correctly but fails to enforce authorization consistently.

## Sessions

Understand how the application maintains state between requests.

Security questions:

- How is a session established?
- Where is the session identifier stored?
- Does logout invalidate it?
- Are session cookies protected appropriately?
- Can one user access another user's state?

## Input handling

Applications should treat external input as untrusted data and apply context-appropriate validation/encoding.

### XSS

Cross-site scripting occurs when attacker-controlled content is interpreted as executable browser-side script in an unsafe context.

Think in terms of:

```text
Source of input → Processing → Output context → Browser interpretation
```

The exact remediation depends on context, commonly including output encoding, safe templating and appropriate Content Security Policy controls.

### Injection

Injection occurs when untrusted input changes the structure or meaning of an interpreter command/query.

Examples include SQL, OS command, LDAP and template injection.

The root-cause question is:

> Can data become code because the application constructs an interpreter statement unsafely?

Parameterized queries and context-appropriate APIs are common defenses.

## Access-control testing

In an authorized lab, compare the same resource under different legitimate roles.

Test:

- horizontal access control: user A accessing user B's data
- vertical access control: lower-privileged user reaching administrative functionality
- object-level authorization
- function-level authorization

Document the expected and actual authorization decisions.

## SSRF

Server-side request forgery occurs when an application can be induced to make unintended server-side requests.

Analysis should identify:

- controllable input
- destination restrictions
- protocol handling
- redirect behavior
- reachable trust boundaries
- returned data

The key risk is not simply "the server made a request"; it is **what privileged network position the server can reach on behalf of the requester**.

## Path traversal

Path traversal occurs when user-controlled path components escape the intended directory boundary.

Defenses include:

- safe path handling
- canonicalization
- allowlisted resources
- operating-system permissions
- avoiding direct concatenation of untrusted path fragments

## File upload

Analyze:

- filename handling
- content-type validation
- file-content validation
- storage location
- execution permissions
- retrieval path
- size/resource limits

Never rely on a client-supplied MIME type alone.

## CSRF

Cross-site request forgery abuses an authenticated browser's authority to perform an unwanted state-changing action.

Defenses commonly include appropriate anti-CSRF tokens, SameSite cookie controls and origin validation where applicable.

## Security headers

Understand the purpose of controls such as:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- frame-ancestors / clickjacking protections

A missing header is not automatically a vulnerability; assess the application context and impact.

## Testing workflow

```text
Map normal behavior
      ↓
Identify trust boundary
      ↓
Form vulnerability hypothesis
      ↓
Change one variable
      ↓
Observe response
      ↓
Validate reproducibility
      ↓
Assess impact
      ↓
Document root cause + remediation
```

### Competency gate

I should be able to explain HTTP state and trust boundaries, test authentication/authorization behavior, recognize major input-handling vulnerability classes, validate findings safely and produce evidence-based remediation advice.

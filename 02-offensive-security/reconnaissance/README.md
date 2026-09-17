# 🔎 Reconnaissance

Reconnaissance converts an authorized scope into an understanding of the target's attack surface.

## Scope comes first

Before collecting information, establish:

- authorized assets
- excluded assets
- permitted techniques
- testing windows
- rate limits
- emergency contacts
- evidence requirements

Reconnaissance outside authorization is not a professional shortcut; it is a scope failure.

## Passive reconnaissance

Passive methods gather information without directly interacting with the target infrastructure where possible.

Examples:

- organization-provided documentation
- DNS information from permitted sources
- certificate transparency research
- public technology information
- known asset inventories

The objective is to reduce uncertainty before active testing.

## Active reconnaissance

Active reconnaissance interacts with authorized systems.

Examples include:

- host discovery
- port discovery
- service identification
- web endpoint discovery
- protocol probing

The more intrusive the activity, the more important scope, rate and operational safety become.

## Attack-surface map

For each asset, record:

```text
Asset
├── IP / hostname
├── Network location
├── Exposed ports
├── Services
├── Technologies
├── Authentication surface
├── Data/functionality
└── Potential security questions
```

## Hypothesis-driven reconnaissance

Do not collect information without a purpose.

Instead:

```text
Observation → Question → Test → Result → Next question
```

Example:

> Observation: a web service is exposed.
>
> Question: what application is behind it?
>
> Test: inspect headers, responses and permitted technology fingerprints.
>
> Result: application framework identified.
>
> Next question: which authentication and authorization boundaries exist?

## Evidence discipline

Record:

- timestamp
- target
- command/tool
- relevant output
- interpretation
- confidence

Scanner output is evidence to analyze, not automatically a finding.

### Competency gate

I should be able to define scope, build an attack-surface map, distinguish passive from active collection, form testable hypotheses and document reconnaissance without exposing sensitive information.

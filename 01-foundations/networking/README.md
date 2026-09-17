# 🌐 Networking Fundamentals

Networking is the foundation for both offensive and defensive security. Security tools report network facts, but the analyst must understand what those facts mean.

## 1. Addressing

An IPv4 address is 32 bits divided into a network portion and a host portion according to the prefix length.

Example:

```text
192.168.10.25/24
```

`/24` means the first 24 bits identify the network. The remaining 8 bits identify hosts within that subnet.

For a normal `/24`:

- Network: `192.168.10.0`
- Usable host range: `192.168.10.1`–`192.168.10.254`
- Broadcast: `192.168.10.255`
- Total addresses: 256
- Traditional usable hosts: 254

Do not memorize only the numbers. Understand the binary boundary created by the prefix.

## 2. CIDR and subnetting

CIDR notation expresses the number of network bits. The host-bit count is:

```text
host bits = 32 - prefix length
```

For a basic IPv4 subnet:

```text
addresses = 2^(host bits)
hosts ≈ 2^(host bits) - 2
```

The two traditional exclusions are the network and broadcast addresses. Modern networking can have exceptions, so always interpret the address type in context.

### Security relevance

Subnetting determines:

- Which hosts are local.
- Which destinations require a gateway.
- How scanners should scope targets.
- How segmentation limits lateral movement.
- Which firewall rules are likely to apply.

## 3. Ethernet, ARP and switching

At the local-link layer, hosts use MAC addresses to deliver Ethernet frames. ARP maps IPv4 addresses to MAC addresses on IPv4 LANs.

A simplified flow:

```text
Application data
      ↓
Transport segment
      ↓
IP packet
      ↓
Ethernet frame
      ↓
Physical/link transmission
```

A switch primarily forwards frames using its MAC address table. A router forwards packets between IP networks using routing information.

### Security relevance

ARP behavior matters when investigating:

- Duplicate IP symptoms
- Unexpected MAC changes
- ARP spoofing indicators
- Local-segment connectivity failures

## 4. Routing

A host normally checks whether a destination is local. If it is not, the host sends traffic toward a configured gateway.

Routers select routes using the routing table. When multiple routes match, the **longest-prefix match** is generally preferred because it is the most specific matching network.

Example:

```text
10.0.0.0/8       → Router A
10.10.0.0/16     → Router B
10.10.20.0/24    → Router C
```

Traffic to `10.10.20.50` matches all three, but `/24` is the most specific route.

## 5. TCP, UDP, ports and sockets

TCP provides connection-oriented, ordered and reliable delivery. A typical connection begins with the three-way handshake:

```text
Client → SYN → Server
Client ← SYN/ACK ← Server
Client → ACK → Server
```

UDP is connectionless and does not provide TCP's delivery guarantees.

A **port** identifies a transport-layer service endpoint. A **socket** represents an endpoint of network communication, commonly described by IP address, transport protocol and port.

### Security relevance

Enumeration asks:

- Is the host reachable?
- Which ports respond?
- Which service is behind the port?
- Is the service expected?
- What version/configuration is exposed?
- Does the result make sense when validated independently?

A port number alone does not prove what software is running.

## 6. DNS and DHCP

DNS maps names to records such as IPv4/IPv6 addresses. DHCP can provide hosts with addressing and other network configuration.

Typical DHCP acquisition:

```text
Discover → Offer → Request → Acknowledge
```

### Security relevance

DNS and DHCP are both dependencies worth understanding during troubleshooting and investigations. Unexpected DNS answers, rogue DHCP behavior, or unusual resolver traffic can become security signals, but require validation rather than assumptions.

## 7. VLANs, NAT and segmentation

A VLAN provides logical Layer-2 separation on supporting network infrastructure. Routing or other controlled mechanisms are normally required for communication between different IP networks/VLANs.

NAT translates address information between network domains. NAT is not a substitute for a firewall or segmentation policy.

Segmentation reduces unnecessary reachability. From a defensive perspective, the question is not simply "can an attacker scan?" but "which security boundaries prevent the scan from becoming lateral movement?"

## 8. Application protocols

Understand the purpose and normal behavior of common protocols:

| Protocol | Typical role | Security questions |
|---|---|---|
| HTTP/HTTPS | Web | Authentication, authorization, TLS, input handling |
| SSH | Remote administration | Keys, authentication, exposure, logging |
| SMB | File/printer sharing | Authentication, signing, exposure, permissions |
| RDP | Remote desktop | Exposure, authentication, MFA, logging |
| LDAP | Directory access | Authentication, authorization, directory exposure |
| Kerberos | Authentication in AD | Tickets, time synchronization, identity context |

## 9. TLS

TLS protects application traffic by providing confidentiality, integrity and server/client authentication depending on configuration.

The analyst should understand:

- Certificates
- Certificate authorities
- Hostname validation
- Key exchange
- Encryption versus authentication
- Certificate expiry/trust failures

## 10. Troubleshooting methodology

When connectivity fails, do not jump directly to a security conclusion.

Use a layered process:

```text
1. Interface/link
2. Local IP configuration
3. Routing table
4. ARP/local neighbor resolution
5. Gateway reachability
6. DNS resolution
7. TCP port reachability
8. Application protocol
9. Authentication/authorization
10. Application behavior
```

Useful Linux commands include:

```bash
ip addr
ip route
ip neigh
ping <host>
getent hosts <name>
ss -tulpn
curl -I http://<host>
```

Use packet capture when the existing evidence cannot explain the behavior.

## 11. Security workflow

Networking knowledge becomes operational security skill when I can move from:

**IP → route → port → service → protocol → behavior → security consequence**

### Competency gate

I should be able to subnet manually, explain packet movement through a small network, interpret a routing table, identify TCP/UDP behavior, troubleshoot DNS/connectivity, and validate service-enumeration results.

#!/usr/bin/env python3
"""subnet_calc.py — quick subnet breakdown for a given IP/CIDR.

Usage:
    python3 subnet_calc.py 192.168.1.10/24
    python3 subnet_calc.py 10.0.5.33/27

Built on the standard-library `ipaddress` module (no pip installs).
Practice goal: understand network / broadcast / host range by hand,
then use this to check your answer.
"""
import sys
import ipaddress


def describe(cidr: str) -> None:
    # strict=False lets us pass a host address (e.g. .10) with the prefix
    # and still resolve the containing network.
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = list(net.hosts())

    print(f"Input          : {cidr}")
    print(f"Network        : {net.network_address}")
    print(f"Netmask        : {net.netmask}")
    print(f"CIDR prefix    : /{net.prefixlen}")
    print(f"Broadcast      : {net.broadcast_address}")
    print(f"Total addresses: {net.num_addresses}")

    if hosts:
        print(f"Usable hosts   : {len(hosts)}  ({hosts[0]} – {hosts[-1]})")
    else:
        # /31 and /32 have no conventional usable-host range
        print("Usable hosts   : 0 (point-to-point or single host)")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 subnet_calc.py <IP/CIDR>")
        return 1
    try:
        describe(sys.argv[1])
    except ValueError as err:
        print(f"Invalid input: {err}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

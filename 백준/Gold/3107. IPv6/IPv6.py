import sys
import ipaddress

addr = ipaddress.ip_address(sys.stdin.readline().rstrip())

print(addr.exploded)
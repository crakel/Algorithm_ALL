import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())

print((a*a + b*b + c*c + d*d + e*e) % 10)
import sys

n, m = map(int, sys.stdin.readline().split())
sites = {}

for _ in range(n):
    site, pw = sys.stdin.readline().split()
    sites[site] = pw

for _ in range(m):
    find = sys.stdin.readline().strip()
    print(sites[find])
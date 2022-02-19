import sys
import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent ,a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().strip().split())
parent = [0] * (v + 1)
edges = []
res = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(edges, (c, a, b))

for _ in range(e):
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)
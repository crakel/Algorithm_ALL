import sys
import heapq
import math

n = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
vertex = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().strip().split())
    vertex.append((x, y))

for i in range(n-1):
    for j in range(i, n):
        if i == j:
            continue
        dist = math.sqrt((vertex[i][0] - vertex[j][0]) ** 2 + (vertex[i][1] - vertex[j][1]) ** 2)
        graph[i].append((dist, j))
        graph[j].append((dist, i))

edges = []
res = 0
def prim():
    global res
    heapq.heappush(edges, (0, 0))
    visited = [0 for _ in range(n)]
    while edges:
        dist, nxt = heapq.heappop(edges)
        if visited[nxt] == 1:
            continue
        res += dist
        visited[nxt] = 1
        for dist, nxt in graph[nxt]:
            heapq.heappush(edges, (dist, nxt))

prim()
print(round(res, 2))
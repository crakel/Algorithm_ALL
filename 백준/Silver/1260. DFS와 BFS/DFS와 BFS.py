import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for value in graph.values():
    value.sort()


def dfs(v):
    if len(visited) == n:
        return

    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w)


def bfs(v):
    visited.append(v)
    q = deque([v])
    while q:
        cur = q.popleft()
        for w in graph[cur]:
            if w not in visited:
                visited.append(w)
                q.append(w)


visited = []
dfs(v)
for n in visited:
    print(n, end=" ")

print()

visited = []
bfs(v)
for n in visited:
    print(n, end=" ")
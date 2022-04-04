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
    visited[v] = 1
    print(v, end=' ')
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


def bfs(v):
    visited[v] = 1
    q = deque([v])
    while q:
        cur = q.popleft()
        print(cur, end =' ')
        for w in graph[cur]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)


visited = [0] * (n+1)
dfs(v)
print()

visited = [0] * (n+1)
bfs(v)
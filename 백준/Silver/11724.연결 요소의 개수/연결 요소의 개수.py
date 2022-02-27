import sys

n, m = map(int, sys.stdin.readline().split())

graph = {}
for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

found = []


def dfs(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in found:
            found.append(v)
            for w in graph[v]:
                stack.append(w)


count = 0
for i in range(1, n + 1):
    if i not in found:
        dfs(i)
        count += 1
print(count)
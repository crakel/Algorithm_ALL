import sys

v = int(sys.stdin.readline())
w = int(sys.stdin.readline())
graph = {}

for i in range(1, v+1):
    graph[i] = []

for _ in range(w):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

found = []
stack = []


def dfs(n):
    stack.append(n)
    while stack:
        v = stack.pop()
        if v not in found:
            found.append(v)
            for w in graph[v]:
                stack.append(w)


dfs(1)
print(len(found)-1)
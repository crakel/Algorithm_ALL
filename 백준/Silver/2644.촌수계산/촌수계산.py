import sys
from collections import deque
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

g = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
route = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x][y] = g[y][x] = 1

def bfs(start, end):
    visit = [0 for _ in range(n+1)]
    visit[start] = 1

    q = deque()
    q.append(start)
    while q:
        cur_vertex = q.popleft()
        if g[cur_vertex][end] == 1:
            route[end] = route[cur_vertex] + 1
            return route[end]

        for i in range(1, n+1):
            if visit[i] == 0 and g[cur_vertex][i] == 1:
                q.append(i)
                visit[i] = 1
                route[i] = route[cur_vertex] + 1
    return -1

print(bfs(a,b))

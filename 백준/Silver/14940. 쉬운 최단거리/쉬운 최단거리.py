import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

field = []
for i in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dist = [[0] * m for _ in range(n)]

def bfs(r, c):
    visited[r][c] = 1
    q = deque([[r, c, 0]])
    while q:
        cr, cc, cd = q.popleft()
        visited[cr][cc] = 1
        for d in dir:
            nr, nc = cr + d[0], cc + d[1]

            if 0 <= nr < n and 0 <= nc < m and field[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                dist[nr][nc] = cd + 1
                q.append([nr, nc, cd + 1])


visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if field[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if field[i][j] == 1 and not visited[i][j]:
            dist[i][j] = - 1

for d in dist:
    print(*d)
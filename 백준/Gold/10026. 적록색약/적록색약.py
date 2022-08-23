import sys
from collections import deque

n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().strip())

# 상 하 좌 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(color):
    cnt = 0
    q = deque()
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] in color and not visited[i][j]:
                q.append([i, j])
                cnt += 1
                visited[i][j] = 1

            while q:
                ci, cj = q.popleft()

                for d in dir:
                    ni, nj = ci + d[0], cj + d[1]

                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] in color and not visited[ni][nj]:
                            q.append([ni, nj])
                            visited[ni][nj] = 1
    return cnt


normal = bfs('R') + bfs('G') + bfs('B')
weak = bfs('RG') + bfs('B')

print(normal, weak)
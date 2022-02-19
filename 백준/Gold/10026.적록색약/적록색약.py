import sys
from collections import deque

n = int(sys.stdin.readline())
grid = []
for _ in range(n):
    grid.append(sys.stdin.readline().strip())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(color):
    area_cnt = 0
    q = deque()
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] in color and visit[i][j] == 0:
                q.append([i, j])
                area_cnt += 1
                visit[i][j] = 1

            while q:
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    ni = cur_i + di[d]
                    nj = cur_j + dj[d]
                    # 벽 탐색 방지
                    if ni < 0 or ni >= n or nj < 0 or nj >= n:
                        continue

                    if grid[ni][nj] in color and visit[ni][nj] == 0:
                        q.append([ni, nj])
                        visit[ni][nj] = 1
    return area_cnt


normal = bfs('R') + bfs('G') + bfs('B')
weak = bfs('RG') + bfs('B')

print(normal, weak)
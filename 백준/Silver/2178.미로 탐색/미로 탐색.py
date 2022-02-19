import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []

for _ in range(n):
    maze.append(sys.stdin.readline().strip())

cnt = [[0] * m for _ in range(n)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs():
    q = deque()
    i = 0
    j = 0
    cnt[i][j] += 1
    q.append([i, j])

    while q:
        cur_i, cur_j = q.popleft()
        if cur_i == n-1 and cur_j == m-1:
            return cnt[cur_i][cur_j]

        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]
            # 벽 탐색 방지
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if maze[ni][nj] == '1' and cnt[ni][nj] == 0:
                q.append([ni, nj])
                cnt[ni][nj] = cnt[cur_i][cur_j] + 1


print(bfs())
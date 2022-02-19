import sys
from collections import deque

n = int(sys.stdin.readline())
area = []
for _ in range(n):
    area.append(list(map(int, sys.stdin.readline().strip().split())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(height):
    area_cnt = 0
    q = deque()
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and visit[i][j] == 0:
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
                    if area[ni][nj] > height and visit[ni][nj] == 0:
                        q.append([ni, nj])
                        visit[ni][nj] = 1
    return area_cnt


max_height = 0
for i in range(n):
    for j in range(n):
        if area[i][j] > max_height:
            max_height = area[i][j]

max_area = 1 # 아무것도 잠기지않으면 1
for h in range(1, max_height+1):
    if bfs(h) > max_area:
        max_area = bfs(h)


print(max_area)
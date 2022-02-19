# n m이 작고 시간제한이 2초니까 벽 3개를 무작정 구해봐도 되지않을까?
import sys
from collections import deque
from itertools import combinations
import copy

n, m = map(int, sys.stdin.readline().strip().split())

lab = []
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().strip().split())))

# 0의 좌표값을 반환
def find_area(lab):
    safe_area = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                safe_area.append([i, j])
    return safe_area

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(lab):
    q = deque()
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2 and visit[i][j] == 0: # 아직 퍼지지않은 바이러스
                q.append([i, j])
                visit[i][j] = 1

            while q:
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    ni = cur_i + di[d]
                    nj = cur_j + dj[d]
                    # 벽 탐색 방지
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        continue
                    if lab[ni][nj] == 0 and visit[ni][nj] == 0: # 바이러스 퍼짐
                        q.append([ni, nj])
                        visit[ni][nj] = 1
                        lab[ni][nj] = 2

zeros = find_area(lab)
combi = list(combinations(zeros, 3))

max_area = 0

for x in combi:
    tmp_lab = copy.deepcopy(lab)
    for i in range(3):
        tmp_lab[x[i][0]][x[i][1]] = 1
    # for y in tmp_lab:
    #     print(*y)
    # print("\n")
    bfs(tmp_lab)

    area_cnt = len(find_area(tmp_lab))
    if area_cnt > max_area:
        max_area = area_cnt

print(max_area)
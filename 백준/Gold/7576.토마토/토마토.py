import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tmt = []

for _ in range(n):
    tmt.append(list(map(int, sys.stdin.readline().strip().split())))

q = deque()
tmt_cnt = 0
for i in range(n):
    for j in range(m):
        if tmt[i][j] == 1:
            q.append([i, j])
        elif tmt[i][j] == 0:
            tmt_cnt += 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    global tmt_cnt
    MAX = 0
    while q and tmt_cnt > 0:
        cur_i, cur_j = q.popleft()

        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]
            # 벽 탐색 방지
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if tmt[ni][nj] == -1:
                continue

            if tmt[ni][nj] == 0:
                q.append([ni, nj])
                tmt_cnt -= 1
                tmt[ni][nj] = tmt[cur_i][cur_j] + 1
                if tmt[ni][nj] > MAX:
                    MAX = tmt[cur_i][cur_j]
    if tmt_cnt > 0:
        return -1
    return MAX

print(bfs())


import sys
from collections import deque

n = int(sys.stdin.readline())

jido = []

for _ in range(n):
    jido.append(list(map(int, sys.stdin.readline().strip())))

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

house = []
danji = 0
def bfs():
    global danji
    house_cnt = 0
    q = deque()
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if jido[i][j] == 1 and visit[i][j] == 0:
                q.append([i, j])
                house_cnt += 1
                visit[i][j] = 1
                danji += 1

            while q:
                cur_i, cur_j = q.popleft()

                for d in range(4):
                    ni = cur_i + di[d]
                    nj = cur_j + dj[d]
                    # 벽 탐색 방지
                    if ni < 0 or ni >= n or nj < 0 or nj >= n:
                        continue

                    if jido[ni][nj] == 1 and visit[ni][nj] == 0:
                        q.append([ni, nj])
                        visit[ni][nj] = 1
                        house_cnt += 1
            if house_cnt != 0:
                house.append(house_cnt)
                house_cnt = 0

bfs()
print(danji)
for x in sorted(house):
    print(x)
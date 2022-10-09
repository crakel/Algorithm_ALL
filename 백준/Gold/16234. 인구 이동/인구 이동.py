import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().split())

# 상 하 좌 우
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
field = []
for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

def bfs(r, c):
    union_tmp = []
    visited[r][c] = 1
    union_tmp.append((r, c))
    q = deque([(r, c)])
    while q:
        cr, cc = q.popleft()
        for d in ds:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                dif = abs(field[cr][cc] - field[nr][nc])
                if L <= dif <= R:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    union_tmp.append((nr, nc))
    if union_tmp:
        union.append(union_tmp)


def move():
    for u in union:
        pop = 0
        for r, c in u:
            pop += field[r][c]

        n_pop = pop // len(u)
        for r, c in u:
            field[r][c] = n_pop

day = 0
while True:
    # print("day : ", day)
    # for f in field:
    #     print(*f)
    union = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    # print(union)
    if len(union) == n*n:
        break
    else:
        day += 1
        move()
print(day)
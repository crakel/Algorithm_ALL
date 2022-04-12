import sys

n, m = map(int, sys.stdin.readline().split())

field = []

for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

visit = [[0]*m for _ in range(n)]
_max = 0
max_field = max(map(max, field))

# 좌 상 우 하
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, depth, total):
    global _max
    if _max >= total + max_field * (4 - depth):
        return
    if depth == 4:
        if total > _max:
            _max = total
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not visit[nx][ny]:
                if depth == 2:
                    visit[nx][ny] = 1
                    dfs(x, y, depth + 1, total + field[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, depth+1, total + field[nx][ny])
                visit[nx][ny] = 0


for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, field[i][j])
        visit[i][j] = 0

print(_max)
import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if field[nx][ny] == 1 and visit[nx][ny] == 0:
            dfs(nx, ny)



for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    field = [[0] * m for p in range(n)]
    for __ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        field[y][x] = 1
    visit = [[0] * m for q in range(n)]
    worm = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                worm += 1
    print(worm)
import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
S = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

for x in range(1, n+1):
    for y in range(1, n+1):
        S[x][y] = S[x - 1][y] + S[x][y - 1] - S[x - 1][y - 1] + lst[x-1][y-1]

for _ in range(m):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    print(S[ex][ey] - S[ex][sy-1] - S[sx-1][ey] + S[sx-1][sy-1])
import sys

n, m = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

field = []
for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 북 동 남 서

cnt = 0
visited = [[0] * m for _ in range(n)]


def process():
    global cnt, r, c, d

    visited[r][c] = 1
    cnt += 1

    while True:
        flag = 0
        for _ in range(4):
            # 왼쪽 칸
            if d == 0:
                ld = 3

            else:
                ld = d - 1

            lr, lc = r + dir[ld][0], c + dir[ld][1]
            d = ld
            if 0 <= lr < n and 0 <= lc < m and field[lr][lc] != 1 and not visited[lr][lc]:
                visited[lr][lc] = 1
                r, c = lr, lc
                cnt += 1
                flag = 1
                break

        if flag == 0:
            # 바로 뒤 칸
            bd = (d + 2) % 4
            br, bc = r + dir[bd][0], c + dir[bd][1]

            if field[br][bc] == 1:
                print(cnt)
                break

            else:
                r, c = br, bc


process()
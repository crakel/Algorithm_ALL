import sys

r, c, n = map(int, sys.stdin.readline().split())

field = []

for _ in range(r):
    row = list(map(int, sys.stdin.readline().replace('O', '2').replace('.', '0').rstrip()))
    field.append(row)

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

def time_flies():
    exp = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if field[i][j] == 0:
                if not field[i][j]:
                    for d in dir:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < r and 0 <= nj < c:
                            exp[ni][nj] = 1

    # 폭발
    for i in range(r):
        for j in range(c):
            if exp[i][j]:
                field[i][j] = 0


def plant():
    for i in range(r):
        for j in range(c):
            if not field[i][j]:
                field[i][j] = 3
            else:
                field[i][j] -= 1


def explosion(i, j):
    for d in dir:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < r and 0 <= nj < c:
            field[ni][nj] = 0

for t in range(2, n+1):
    plant()
    time_flies()
    # print("t = ", t)
    # for f in field:
    #     print(f)
    # print()

for i in range(r):
    for j in range(c):
        if not field[i][j]:
            field[i][j] = '.'
        else:
            field[i][j] = 'O'

for f in field:
    print(''.join(f))


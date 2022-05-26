import sys

field = []

for _ in range(9):
    field.append(list(map(int, sys.stdin.readline().rstrip())))

blank = [(i, j) for i in range(9) for j in range(9) if not field[i][j]]
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


# 백트래킹 구현
def bt(depth):
    if depth == len(blank):
        for f in field:
            print(*f, sep="")
        exit(0)

    r, c = blank[depth]
    mr, mc = (r // 3) * 3 + 1, (c // 3) * 3 + 1

    able = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 가로 세로 체크
    for i in range(9):
        if field[r][i] in able:
            able.remove(field[r][i])
        if field[i][c] in able:
            able.remove(field[i][c])

    # 영역 체크
    if field[mr][mc] in able:
        able.remove(field[mr][mc])

    for d in dir:
        nr, nc = mr + d[0], mc + d[1]
        if field[nr][nc] in able:
            able.remove(field[nr][nc])

    for a in list(able):
        field[r][c] = a
        bt(depth+1)
    field[r][c] = 0


bt(0)

# 시간 초과
# while True:
#     if not sum(f.count(0) for f in field):
#         for f in field:
#             print(*f, sep="")
#         break
#
#     else:
#         for i in range(9):
#             for j in range(9):
#                 if not field[i][j]:
#                     able = find_num(i, j)
#                     if len(able) == 1:
#                         field[i][j] = able.pop()


import sys

n = int(sys.stdin.readline())

field = []
loc = (n//2, n//2)

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# rain []
# 0 1 2 3 4 5 6 7 8
# 1 1 2 2 5 7 7 10 10
# 좌 하 우 상
for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))


def torn_move(r, c, N):
    #print("torn_move r, c: ", r, c)

    nr = r
    nc = c
    # 홀수 N : 좌 하
    if N % 2 == 1:
        # 좌 d = 0
        for _ in range(N):
            if nr == 0 and nc == 0:
                return
            sand_rain(nr, nc, 0)
            nr = nr + dir[0][0]
            nc = nc + dir[0][1]
        # 하 d = 1
        for _ in range(N):
            if nr == 0 and nc == 0:
                return
            sand_rain(nr, nc, 1)
            nr = nr + dir[1][0]
            nc = nc + dir[1][1]

    # 짝수 N : 우 상
    else:
        # 우 d = 2
        for _ in range(N):
            if nr == 0 and nc == 0:
                return
            sand_rain(nr, nc, 2)
            nr = nr + dir[2][0]
            nc = nc + dir[2][1]
        # 상 d = 3
        for _ in range(N):
            if nr == 0 and nc == 0:
                return
            sand_rain(nr, nc, 3)
            nr = nr + dir[3][0]
            nc = nc + dir[3][1]

    torn_move(nr, nc, N+1)


def is_out(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True

    else:
        return False


out = 0
def sand_rain(r, c, d):
    global out
    # for f in field:
    #     print(f)
    # print()
    y = (r + dir[d][0], c + dir[d][1])
    sand = field[y[0]][y[1]]
    sand_left = sand

    a = (r + 2*dir[d][0], c + 2*dir[d][1])
    rain = []
    if d == 0:
        rain.append((y[0]-1, y[1]+1))
        rain.append((y[0]+1, y[1]+1))
        rain.append((y[0]-2, y[1]))
        rain.append((y[0]+2, y[1]))
        rain.append((y[0], y[1]-2))
        rain.append((y[0]-1, y[1]))
        rain.append((y[0]+1, y[1]))
        rain.append((y[0]-1, y[1]-1))
        rain.append((y[0]+1, y[1]-1))

    elif d == 1:
        rain.append((y[0]-1, y[1]-1))
        rain.append((y[0]-1, y[1]+1))
        rain.append((y[0], y[1]-2))
        rain.append((y[0], y[1]+2))
        rain.append((y[0]+2, y[1]))
        rain.append((y[0], y[1]-1))
        rain.append((y[0], y[1]+1))
        rain.append((y[0]+1, y[1]-1))
        rain.append((y[0]+1, y[1]+1))

    elif d == 2:
        rain.append((y[0]-1, y[1]-1))
        rain.append((y[0]+1, y[1]-1))
        rain.append((y[0]-2, y[1]))
        rain.append((y[0]+2, y[1]))
        rain.append((y[0], y[1]+2))
        rain.append((y[0]-1, y[1]))
        rain.append((y[0]+1, y[1]))
        rain.append((y[0]-1, y[1]+1))
        rain.append((y[0]+1, y[1]+1))

    elif d == 3:
        rain.append((y[0]+1, y[1]-1))
        rain.append((y[0]+1, y[1]+1))
        rain.append((y[0], y[1]-2))
        rain.append((y[0], y[1]+2))
        rain.append((y[0]-2, y[1]))
        rain.append((y[0], y[1]-1))
        rain.append((y[0], y[1]+1))
        rain.append((y[0]-1, y[1]-1))
        rain.append((y[0]-1, y[1]+1))

    #print("rain : ",rain)
    for i, r in enumerate(rain):
        if i in [0, 1]:
            n_sand = int(sand * 0.01)
        elif i in [2, 3]:
            n_sand = int(sand * 0.02)
        elif i == 4:
            n_sand = int(sand * 0.05)
        elif i in [5, 6]:
            n_sand = int(sand * 0.07)
        elif i in [7, 8]:
            n_sand = int(sand * 0.1)

        if is_out(r[0], r[1]):
            out += n_sand

        else:
            field[r[0]][r[1]] += n_sand

        sand_left -= n_sand

    # a로 이동
    if is_out(a[0], a[1]):
        out += sand_left
    else:
        field[a[0]][a[1]] += sand_left

    # y 모래 0
    field[y[0]][y[1]] = 0
    #print("out : ", out)



torn_move(n//2, n//2, 1)
print(out)
# for f in field:
#     print(f)
# print()
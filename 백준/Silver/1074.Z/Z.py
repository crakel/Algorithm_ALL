import sys

N, r, c = map(int, sys.stdin.readline().split())

cur = -1


def z(n, x, y):
    global cur

    if n > 2:
        # 해당하는 2x2에 r,c 없다면 skip
        if not (x <= r < x + n and y <= c < y + n):
            cur += n * n
            return

        for i in range(x, x + n, n // 2):
            for j in range(y, y + n, n // 2):
                z(n // 2, i, j)
        # 줄이기
        # z(n//2, x, y)
        # z(n//2, x, y+(n//2))
        # z(n//2, x+(n//2), y)
        # z(n//2, x+(n//2), y+(n//2))
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            cur += 1
            if i == r and j == c:
                print(cur)
                exit(0)

    # 줄이기
    # if x == r and y == c:
    #     print(cur)
    #     exit(0)
    # cur += 1
    #
    # if x == r and y+1 == c:
    #     print(cur)
    #     exit(0)
    # cur += 1
    #
    # if x+1 == r and y == c:
    #     print(cur)
    #     exit(0)
    # cur += 1
    #
    # if x+1 == r and y+1 == c:
    #     print(cur)
    #     exit(0)
    # cur += 1


z(2 ** N, 0, 0)
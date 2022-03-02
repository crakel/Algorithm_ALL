import sys

t = int(sys.stdin.readline())


for _ in range(t):
    count = 0
    M, N, x, y = map(int, sys.stdin.readline().split())

    while x <= M * N:
        if (x-y) % N == 0:
            print(x)
            break
        x += M
    if x > M * N:
        print(-1)




    # 시간 초과 (첫 접근)
    # while True:
    #     if i + j == M + N:
    #         if i != x and j != y:
    #             print(-1)
    #             break
    #
    #     count += 1
    #     if i == x and j == y:
    #         print(count)
    #         break
    #
    #     if i < M:
    #         i += 1
    #     else:
    #         i = 1
    #
    #     if j < N:
    #         j += 1
    #     else:
    #         j = 1
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

field = []
move = deque([])
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
d = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
#      X        ←         ↖        ↑        ↗        →       ↘       ↓       ↙
# 대각선 -> d[2], d[4], d[6], d[8]

for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    move.append(list(map(int, sys.stdin.readline().split())))

# for f in field:
#     print(f)
# print()

def water_copy(r, c):
    cnt = 0
    for i in range(2, 9, 2):
        if 0 <= r + d[i][0] < n and 0 <= c + d[i][1] < n and field[r + d[i][0]][c + d[i][1]] > 0:
            cnt += 1

    field[r][c] += cnt


while move:
    cur_move = move.popleft()
    is_cloud = [[0] * n for _ in range(n)]
    for c in cloud:
        c[0] += d[cur_move[0]][0] * cur_move[1]
        c[1] += d[cur_move[0]][1] * cur_move[1]
        c[0] %= n
        c[1] %= n
        field[c[0]][c[1]] += 1
        is_cloud[c[0]][c[1]] = 1

    for c in cloud:
        water_copy(c[0], c[1])

    new_cloud = []
    for i in range(n):
        for j in range(n):
            if field[i][j] >= 2 and not is_cloud[i][j]:
                field[i][j] -= 2
                new_cloud.append([i, j])
    # print(cloud)
    cloud = new_cloud
    # print(cloud)
    # for f in field:
    #     print(f)
    # print()

sum_field = 0
for i in range(n):
    for j in range(n):
        sum_field += field[i][j]
print(sum_field)
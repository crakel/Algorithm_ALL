import sys

n = int(sys.stdin.readline())

dic = {}
for _ in range(n**2):
    lst = (list(map(int, sys.stdin.readline().split())))
    dic[lst[0]] = lst[1:]

sit = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


for key, value in dic.items():
    stu = key
    stu_like = value
    max_like = -1e9
    max_blank = -1e9
    for i in range(n):
        for j in range(n):
            like_cnt = 0
            blank_cnt = 0
            if sit[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if sit[nx][ny] in stu_like:
                            like_cnt += 1
                        if sit[nx][ny] == 0:
                            blank_cnt += 1

                if max_like < like_cnt or (max_like == like_cnt and max_blank < blank_cnt):
                    max_index = (i, j)
                    max_like = like_cnt
                    max_blank = blank_cnt
                # nx, ny range(4)를 통해 코드 줄일 수 있다.
                # left = (i, j+dx[0])
                # up = (i+dy[1], j)
                # right = (i, j+dx[2])
                # down = (i+dy[3], j)
                #
                # if j + dx[0] >= 0:
                #     if sit[left[0]][left[1]] in stu_like:
                #         like_cnt += 1
                #     if sit[left[0]][left[1]] == 0:
                #         blank_cnt += 1
                #
                # if i + dy[1] >= 0:
                #     if sit[up[0]][up[1]] in stu_like:
                #         like_cnt += 1
                #     if sit[up[0]][up[1]] == 0:
                #         blank_cnt += 1
                #
                # if j + dx[2] < n:
                #     if sit[right[0]][right[1]] in stu_like:
                #         like_cnt += 1
                #     if sit[right[0]][right[1]] == 0:
                #         blank_cnt += 1
                #
                # if i + dy[3] < n:
                #     if sit[down[0]][down[1]] in stu_like:
                #         like_cnt += 1
                #     if sit[down[0]][down[1]] == 0:
                #         blank_cnt += 1

    sit[max_index[0]][max_index[1]] = stu

res = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if sit[nx][ny] in dic[sit[i][j]]:
                    cnt += 1
        if cnt != 0:
            res += 10 ** (cnt-1)
print(res)

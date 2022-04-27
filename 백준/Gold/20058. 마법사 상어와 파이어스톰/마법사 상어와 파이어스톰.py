import sys
from collections import deque

n, q = map(int, sys.stdin.readline().split())
ice = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
#     상  하  좌  우

for _ in range(2**n):
    ice.append(list(map(int, sys.stdin.readline().split())))

len_ice = len(ice)

level = deque(list(map(int, sys.stdin.readline().split())))

def rot_ice(sr, sc, length): #얼음 회전
    area = [i[:] for i in ice[:]]
    er = sr + length
    ec = sc + length

    for r in range(sr, er):
        for c in range(sc, ec):
            # print("r: ", r)
            # print("c: ", c)
            # print(area[r][c])
            ice[sr+(c%length)][ec-1-(r%length)] = area[r][c]

def pro_ice(): # 얼음 프로세스
    for _ in range(q):
        n_level = level.popleft()
        for r in range(0, len_ice, 2**n_level):
            for c in range(0, len_ice, 2**n_level):
                # print("r: ", r)
                # print("c: ", c)
                rot_ice(r, c, 2**n_level)
        dec_ice()


def dec_ice(): # 얼음 제거
    cnt = [[0] * len_ice for _ in range(len_ice)]
    for r in range(len_ice):
        for c in range(len_ice):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < len_ice and 0 <= nc < len_ice and ice[nr][nc] > 0:
                    cnt[r][c] += 1

    for r in range(len_ice):
        for c in range(len_ice):
            if ice[r][c] > 0 and cnt[r][c] < 3:
                ice[r][c] -= 1


def bfs_ice():
    visited = [[0] * len_ice for _ in range(len_ice)]
    max_cnt = 0
    sum_ice = 0
    for r in range(len_ice):
        for c in range(len_ice):
            ice_cnt = 0

            if visited[r][c] or ice[r][c] == 0:
                continue

            visited[r][c] = 1
            sum_ice += ice[r][c]
            q = deque([(r, c)])
            while q:
                cur = q.popleft()
                ice_cnt += 1
                for k in range(4):
                    nr = cur[0] + dr[k]
                    nc = cur[1] + dc[k]
                    if 0 <= nr < len_ice and 0 <= nc < len_ice and not visited[nr][nc] and ice[nr][nc] > 0:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        sum_ice += ice[nr][nc]

            max_cnt = max(max_cnt, ice_cnt)
    return sum_ice, max_cnt


pro_ice()
sum_ice, max_cnt = bfs_ice()
print(sum_ice)
print(max_cnt)
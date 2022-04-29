import sys
from collections import deque

# 초기 모든칸 블록 1개
# 검은색 -1 / 무지개 0 / 일반 M이하 자연수 (M가지 색)
# 상하좌우 인접
#
# 그룹 -> 연결된 블록 >=2
# 일반블록>=1 모두 같은 색 / 검은색 블록 X / 무지개 블록 O
# * 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서
# 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다
# 블록그룹에 기준 블록이 존재 (무지개x 중 r의 번호가 가장작 / c의번호가 가장 작)
# lambda로 조건 2개 sort?
# -2 를 비어있는 블록으로 정의
n, m = map(int, sys.stdin.readline().split())
grid = []

for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우


def bfs_grid(r, c):
    tmp = [(r, c, 0)]
    color = grid[r][c]
    visited[r][c] = 1
    q = deque([(r, c)])
    while q:
        cr, cc = q.popleft()
        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]
            if not 0 <= nr < n or not 0 <= nc < n or grid[nr][nc] == -2 or grid[nr][nc] == -1:
                continue

            if not visited[nr][nc] and (grid[nr][nc] == 0 or grid[nr][nc] == color):
                visited[nr][nc] = 1
                if grid[nr][nc] == color:
                    rainbow = 0
                else:
                    rainbow = 1
                tmp.append((nr, nc, rainbow))
                q.append((nr, nc))

    if len(tmp) >= 2:
        group.append(tmp)


def sort_group():
    for g in group:
        g.sort(key=lambda x: (x[2], x[0], x[1]))


def find_large_group():
    for i, g in enumerate(group):
        rainbow_cnt = 0
        for k in g:
            if k[2] == 1:
                rainbow_cnt += 1
        std_r = g[0][0]
        std_c = g[0][1]
        group_score.append((std_r, std_c, rainbow_cnt, len(g), i))

    group_score.sort(key=lambda x: (x[3], x[2], x[0], x[1]), reverse=True)


def get_score():
    global score
    group_idx = group_score[0][4]
    #group_cnt = len(group[group_idx])
    for g in group[group_idx]:
        grid[g[0]][g[1]] = -2

    #print(group[group_idx][3])
    #print("점수 추가 : ", group_score[0][3] ** 2)
    score += (group_score[0][3] ** 2)


def grav_grid():
    for i in range(n-1, -1, -1):
        for j in range(n):
            if grid[i][j] == -2:
                # move x = j
                # move y = i
                ni, nj = i, j
                while 0 <= ni-1 and grid[ni-1][nj] != -1:
                    ni -= 1
                    if grid[ni][nj] >= 0:
                        break
                if ni != i:
                    grid[i][j] = grid[ni][j]
                    grid[ni][j] = -2




def rot_grid():
    global grid
    grid = list(map(list, reversed(tuple(zip(*grid)))))


score = 0
while True:
    group = []
    group_score = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                visited = [[0] * n for _ in range(n)]
                bfs_grid(i, j)

    if len(group) == 0:
        break

    # print("그룹: ", group)
    sort_group()
    # print("그룹: ", group)
    find_large_group()
    # print("그룹스코어: ", group_score)
    get_score()
    # print("중력1전")
    # for g in grid:
    #     print(g)
    # print()
    grav_grid()
    # print("중력1후")
    # for g in grid:
    #     print(g)
    # print()
    rot_grid()
    # print("회전후")
    # for g in grid:
    #     print(g)
    # print()
    grav_grid()
    # print("중력2후")
    # for g in grid:
    #     print(g)
    # print()

print(score)
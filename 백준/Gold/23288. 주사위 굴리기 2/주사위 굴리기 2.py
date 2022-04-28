import sys

n, m, k = map(int, sys.stdin.readline().split())

field = []
for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

nd = 0
# 이동 (r, c)
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 동 남 서 북

dice = {
    'up': 1,
    'down': 6,
    'l_side': 4,
    'r_side': 3,
    'u_side': 2,
    'd_side': 5
}

def dice_roll(dir):
    # 0 1 2 3
    # 동 남 서 북
    if dir == 0: # 동
        tmp = dice['l_side']
        dice['l_side'] = dice['down']
        dice['down'] = dice['r_side']
        dice['r_side'] = dice['up']
        dice['up'] = tmp

    elif dir == 1: # 남
        tmp = dice['u_side']
        dice['u_side'] = dice['down']
        dice['down'] = dice['d_side']
        dice['d_side'] = dice['up']
        dice['up'] = tmp

    elif dir == 2: # 서
        tmp = dice['l_side']
        dice['l_side'] = dice['up']
        dice['up'] = dice['r_side']
        dice['r_side'] = dice['down']
        dice['down'] = tmp

    elif dir == 3: # 북
        tmp = dice['u_side']
        dice['u_side'] = dice['up']
        dice['up'] = dice['d_side']
        dice['d_side'] = dice['down']
        dice['down'] = tmp



score = 0
def dice_move(r, c, dir):
    global score
    global move_cnt
    global nd
    global dice_r
    global dice_c

    n_dir = dir
    nr, nc = r + d[n_dir][0], c + d[n_dir][1]
    # print("r, c : ", nr, nc)
    # print("dir : ", n_dir)
    # 이동 방향에 칸 없는 경우
    if not 0 <= nr < n or not 0 <= nc < m:
        # print("칸 없어용")
        n_dir = (n_dir + 2) % 4
        nr, nc = r + d[n_dir][0], c + d[n_dir][1]
        # print("바뀐r,c : ", nr, nc)
        # print("바뀐dir : ", n_dir)

    # 주사위 굴리기
    dice_roll(n_dir)

    # 점수 획득
    B = field[nr][nc]
    visited = [[0] * m for _ in range(n)]
    move_cnt = 0
    dfs_field(nr, nc, field[nr][nc], visited)
    C = move_cnt
    # print("plus score : ", B*C)
    # print()
    score += (B * C)
    # 이동 방향
    A = dice['down']
    if A > B:
        n_dir = (n_dir + 1) % 4

    elif A < B:
        if n_dir == 0:
            n_dir = 3
        else:
            n_dir -= 1

    nd = n_dir
    dice_r, dice_c = nr, nc


def dfs_field(r, c, value, visited):
    global move_cnt
    visited[r][c] = 1

    if field[r][c] == value:
        move_cnt += 1
        for a in d:
            nr, nc = r + a[0], c + a[1]
            if not 0 <= nr < n or not 0 <= nc < m:
                continue

            if not visited[nr][nc]:
                dfs_field(nr, nc, value, visited)


dice_r = 0
dice_c = 0
for i in range(k):
    move_cnt = 0
    dice_move(dice_r, dice_c, nd)

print(score)

# 지도의 좌표는 (r,c)
# r -> 북쪽으로부터 떨어진 칸
# c -> 서쪽으로부터 떨어진 칸
# field 위에 주사위 1개 ( 각면(지도한칸) 1~6 )
#   2
# 4 1 3 (1좌표 - (1,1))
#   5
#   6
# 최초에 동쪽으로 이동
# 1. 이후 이동 방향 1칸, 칸이없다면 이동 방향 반대로 1칸
# 2. 도착한 칸 (x, y) 점수 획득
# 3. (x, y) 와 아랫면의 정수 A 비교해 다음 이동 방향
# field[r][c]
# A > B 90도 시계
# A < B 90도 반시계
# A = B 방향 그대로
# 점수 : field[r][c](not 0) * 동서남북 연속이동가능칸수
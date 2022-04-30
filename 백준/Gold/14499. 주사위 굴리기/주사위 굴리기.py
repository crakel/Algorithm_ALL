import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())

field = []
for _ in range(n):
    field.append(list(map(int, sys.stdin.readline().split())))

moves = list(map(int, sys.stdin.readline().split()))

# 이동 (r, c)
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# 동 서 북 남

dice = {
    'up': 0,
    'down': 0,
    'l_side': 0,
    'r_side': 0,
    'u_side': 0,
    'd_side': 0
}


def dice_roll(dir):
    # 1 2 3 4
    # 동 서 북 남
    if dir == 1: # 동
        tmp = dice['l_side']
        dice['l_side'] = dice['down']
        dice['down'] = dice['r_side']
        dice['r_side'] = dice['up']
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

    elif dir == 4: # 남
        tmp = dice['u_side']
        dice['u_side'] = dice['down']
        dice['down'] = dice['d_side']
        dice['d_side'] = dice['up']
        dice['up'] = tmp


def dice_move(r, c, dir):
    global dice_r, dice_c

    nr, nc = r + d[dir-1][0], c + d[dir-1][1]

    # 이동 방향에 칸 없는 경우
    if not 0 <= nr < n or not 0 <= nc < m:
        return

    dice_roll(dir)
    # 이동한 칸 0 : 주사위 바닥 복사 -> 칸
    if field[nr][nc] == 0:
        field[nr][nc] = dice['down']

    else:
        dice['down'] = field[nr][nc]
        field[nr][nc] = 0

    print(dice['up'])
    dice_r, dice_c = nr, nc


dice_r, dice_c = x, y
for move in moves:
    dice_move(dice_r, dice_c, move)

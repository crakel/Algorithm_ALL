import sys
from collections import deque

# 12시 방향 부터 시계 방향 8개
gear = {}
for i in range(1, 5):
    gear[i] = deque(list(map(int, sys.stdin.readline().rstrip())))

k = int(sys.stdin.readline())
rot = []
for _ in range(k):
    rot.append(list(map(int, sys.stdin.readline().split())))

# (회전시킨 톱니바퀴 번호, 방향 1(시계) -1(반시계))

# 맞닿는 부분 idx -> 오른쪽 2 왼쪽 6
def rot_right(i, n):
    if i > 4 or (gear[i-1][2] == gear[i][6]):
        return

    rot_right(i+1, -n)
    gear[i].rotate(n)

def rot_left(i, n):
    if i < 1 or (gear[i][2] == gear[i+1][6]):
        return

    rot_left(i-1, -n)
    gear[i].rotate(n)

for r in rot:
    i, n = r[0], r[1]
    rot_right(i+1, -n)
    rot_left(i-1, -n)
    gear[i].rotate(n)

score = 0
for i in range(1, 5):
    score += gear[i][0] * (2**(i-1))

print(score)
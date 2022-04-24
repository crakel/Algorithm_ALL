import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
belt = deque((map(int, sys.stdin.readline().split()))) # 벨트와 내구도
robot = deque([0 for _ in range(n)])


def rot(): # 1.회전
    belt.rotate()
    robot.rotate()
    robot[n-1] = 0


def mov(): # 2.로봇 이동
    for i in range(n-2, -1, -1): # 가장 먼저 올라온 벨트 (역순)
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] = robot[i]
            robot[i] = 0
            belt[i+1] -= 1
    robot[n-1] = 0


def put(): # 3.로봇 올리기
    if robot[0] == 0 and belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1


def stop(): # 4. 종료 조건
    if belt.count(0) >= k:
        return True
    else:
        return False


cnt = 0
while not stop():
    cnt += 1
    rot()
    mov()
    put()

print(cnt)
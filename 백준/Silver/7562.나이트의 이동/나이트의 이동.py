import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(x, y):
    if st[0] == ed[0] and st[1] == ed[1]:
        return 0

    q = deque()
    q.append([x, y])
    cnt[x][y] = 0

    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == ed[0] and cur_y == ed[1]:
            return cnt[cur_x][cur_y]

        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if cnt[nx][ny] == 0:
                q.append([nx, ny])
                cnt[nx][ny] = cnt[cur_x][cur_y] + 1


for _ in range(t):
    l = int(sys.stdin.readline())
    st = list(map(int, sys.stdin.readline().strip().split()))
    ed = list(map(int, sys.stdin.readline().strip().split()))
    cnt = [[0] * l for i in range(l)] # bfs 여태 온 경로 횟수 저장
    print(bfs(st[0], st[1]))
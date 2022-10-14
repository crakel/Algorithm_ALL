import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())


def bfs():
    visited = [0] * (f + 1)
    visited[s] = 1
    cnt = 0
    q = deque([s])

    while q:
        for _ in range(len(q)):
            cur = q.popleft()

            if cur == g:
                print(cnt)
                return

            if cur + u <= f and not visited[cur + u]:
                q.append(cur + u)
                visited[cur + u] = 1

            if cur - d > 0 and not visited[cur - d]:
                q.append(cur - d)
                visited[cur - d] = 1

        cnt += 1
    print("use the stairs")

bfs()
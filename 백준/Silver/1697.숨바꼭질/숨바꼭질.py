import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
if n >= k:
    print(n-k)
    exit(0)

dp = [0] * 2 * k


def bfs(start, end):
    q = deque([start])
    while q:
        v = q.popleft()
        if v == end:
            print(dp[v])
            break
        for path in [v-1, v+1, v*2]:
            if 0 <= path <= 2 * end and not dp[path]:
                dp[path] = dp[v] + 1
                q.append(path)


bfs(n, k)
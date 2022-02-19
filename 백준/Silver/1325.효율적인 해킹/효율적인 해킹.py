import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
trust = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    trust[b].append(a)

def bfs(x):
    visit = [0 for _ in range(n+1)]
    visit[x] = 1
    cnt = 1

    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        for i in trust[cur]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

MAX = 0
res = []
for i in range(1, n+1):
    cur_cnt = bfs(i)
    if MAX == cur_cnt:
        res.append(i)

    elif MAX < cur_cnt:
        MAX = cur_cnt
        res = []
        res.append(i)

print(*res)

import sys

n = int(sys.stdin.readline())

s = []

visit = [0] * n
_min = sys.maxsize


def dfs(idx, cnt):
    global _min

    if cnt == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start += s[i][j]

                elif not visit[i] and not visit[j]:
                    link += s[i][j]
        _min = min(_min, abs(start - link))

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = 1
            dfs(i+1, cnt+1)
            visit[i] = 0


for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

dfs(0, 0)
print(_min)
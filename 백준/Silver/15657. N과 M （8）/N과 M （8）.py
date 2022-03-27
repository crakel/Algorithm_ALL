import sys

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
res = []


def dfs(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, n):
        res.append(lst[i])
        dfs(i)
        res.pop()


dfs(0)

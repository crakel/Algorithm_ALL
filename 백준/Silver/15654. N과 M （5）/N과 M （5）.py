import sys

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
res = []


def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(n):
        if lst[i] not in res:
            res.append(lst[i])
            dfs()
            res.pop()


dfs()
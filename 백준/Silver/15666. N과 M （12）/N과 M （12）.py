import sys

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
stack = []
record = {}


def dfs(start):
    if len(stack) == m:
        res = ' '.join(map(str, stack))
        if res not in record:
            print(res)
            record[res] = 1
        return

    for i in range(start, n):
        stack.append(lst[i])
        dfs(i)
        stack.pop()


dfs(0)
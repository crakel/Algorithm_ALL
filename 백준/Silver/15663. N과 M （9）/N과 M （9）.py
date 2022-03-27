import sys

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0] * n
temp = []
record = {}


def dfs():
    if len(temp) == m:
        res = ' '.join(map(str, temp))
        if res not in record:
            print(res)
            record[res] = 1


        return

    for i in range(n):
        if not visited[i]:
            temp.append(lst[i])
            visited[i] = 1
            dfs()
            temp.pop()
            visited[i] = 0


dfs()
import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0] * n
res = []

# 백트래킹 구현
def bt(start):
    if len(res) == m:
        print(*res)
        return

    prev = 0
    for i in range(start, n):
        if not visited[i] and prev is not lst[i]:
            visited[i] = 1
            res.append(lst[i])
            prev = lst[i]
            bt(i+1)
            visited[i] = 0
            res.pop()

#bt(0)

# 조합 풀이
for l in itertools.combinations(lst, m):
    if not res:
        res.append(l)
    elif l not in res:
        res.append(l)

for r in res:
    print(*r)
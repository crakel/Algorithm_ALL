import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))
# 백트래킹 풀이
res = []
def bt(idx):
    if len(res) == m:
        print(*res)
        return

    for i in range(idx, n):
        if lst[i] not in res:
            res.append(lst[i])
            bt(i+1)
            res.pop()

bt(0)

# 조합 풀이
# for k in itertools.combinations(lst, m):
#     print(*k)
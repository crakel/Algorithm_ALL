import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))

# 조합 풀이
for k in itertools.combinations(lst, m):
    print(*k)
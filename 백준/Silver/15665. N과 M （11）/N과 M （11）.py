import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(set(map(int, sys.stdin.readline().split()))))
visited = [0] * n
res = []

# 조합 풀이
for l in itertools.product(lst, repeat=m):
    print(*l)
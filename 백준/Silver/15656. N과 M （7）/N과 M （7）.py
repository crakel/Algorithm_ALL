import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))

# 중복조합 풀이
for k in list(itertools.product(lst, repeat=m)):
    print(*k)
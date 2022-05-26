import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, n+1)]

# 중복조합 풀이
for k in list(itertools.product(lst, repeat=m)):
    print(*k)
import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

lst = [i for i in range(1, n+1)]


for k in list(itertools.permutations(lst, m)):
    print(*k)
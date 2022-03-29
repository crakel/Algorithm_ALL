import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    lst[i] = lst[i-1] + lst[i]


m = int(sys.stdin.readline())

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if s == 1:
        print(lst[e-1])
    else:
        print(lst[e-1] - lst[s-2])

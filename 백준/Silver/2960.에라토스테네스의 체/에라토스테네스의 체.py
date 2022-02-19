import sys

n, k = map(int, sys.stdin.readline().split())

lst = [i for i in range(2, n+1)]

s = 0
while lst:
    s += 1
    p = lst.pop(0)

    if s == k:
        print(p)
        exit(0)

    for i, n in enumerate(lst):
        if n % p == 0:
            s += 1
            if s == k:
                print(n)
                exit(0)
            lst.pop(i)

print(lst)

import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dic = defaultdict(list)

    if n == 0:
        print(0)
        continue

    for __ in range(n):
        a, b = sys.stdin.readline().split()
        dic[b].append(a)

    temp = 1
    for key, value in dic.items():
        temp *= (len(value)+1)
    temp -= 1
    print(temp)
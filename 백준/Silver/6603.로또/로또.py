import sys
from itertools import combinations

while True:
    s = list(map(int, sys.stdin.readline().strip().split()))
    k = s[0]
    if k == 0:
        break
    del s[0]

    pick = list(combinations(s, 6))
    for x in pick:
        print(*x)
    print()
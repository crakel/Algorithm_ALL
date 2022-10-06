import sys
from itertools import *


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card = []
for _ in range(n):
    card.append(sys.stdin.readline().rstrip())

able = {}
for c in permutations(card, k):
    num = ''.join(c)
    if num not in able:
        able[num] = 1

print(len(able.keys()))
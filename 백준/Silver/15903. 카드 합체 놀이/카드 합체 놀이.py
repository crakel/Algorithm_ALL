import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

# heapq.heapify(card)
card.sort()

for _ in range(m):
    x, y = card[0], card[1]
    card[0] = x + y
    card[1] = x + y
    card.sort()
    # heapq.heapify(card)

print(sum(card))
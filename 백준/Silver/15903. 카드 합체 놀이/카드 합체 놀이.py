import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

heapq.heapify(card)

for _ in range(m):
    x, y = heapq.heappop(card), heapq.heappop(card)
    heapq.heappush(card, x + y)
    heapq.heappush(card, x + y)

print(sum(card))
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))

    if not heap:
        for num in row:
            heapq.heappush(heap, num)

    else:
        for num in row:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])
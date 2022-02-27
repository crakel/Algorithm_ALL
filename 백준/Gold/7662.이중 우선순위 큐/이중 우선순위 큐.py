import sys
import heapq

# 최대힙, 최소힙 두 가지를 같이 돌린다
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    deleted = [1] * k
    min_h = []
    max_h = []
    for i in range(k):
        s, n = sys.stdin.readline().split()
        n = int(n)
        if s == 'I':
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
            deleted[i] = 0
        elif s == 'D':
            if n == -1:
                while min_h and deleted[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    deleted[min_h[0][1]] = 1
                    heapq.heappop(min_h)
            elif n == 1:
                while max_h and deleted[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    deleted[max_h[0][1]] = 1
                    heapq.heappop(max_h)



    while min_h and deleted[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and deleted[max_h[0][1]]:
        heapq.heappop(max_h)

    if not min_h and not max_h:
        print('EMPTY')

    else:
        print(-max_h[0][0], min_h[0][0])
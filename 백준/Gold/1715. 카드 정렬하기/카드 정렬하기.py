import sys
import heapq

n = int(sys.stdin.readline())

hq = []
for _ in range(n):
    heapq.heappush(hq, int(sys.stdin.readline()))

cnt = 0
if n == 1:
    print(0)

elif n == 2:
    print(hq[0] + hq[1])

else:
    while len(hq) != 1:
        # print("hq: ",hq)
        # print("cnt: ", cnt)
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        cnt += a + b
        heapq.heappush(hq, a+b)
    print(cnt)
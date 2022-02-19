import sys
import heapq

INF = float('INF')
n, m = map(int, sys.stdin.readline().strip().split())

farm = [[] for _ in range(n+1)]
dist = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    farm[a].append((b, 1))
    farm[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cur_dist, cur = heapq.heappop(q)
        if dist[cur] < cur_dist:
            continue
        for i in farm[cur]:
            cost = cur_dist + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

hide_dist = 0
for x in dist:
    if x != INF and x > hide_dist:
        hide_dist = x
hide = dist.index(hide_dist)
hide_count = dist.count(hide_dist)

print(hide, hide_dist, hide_count)
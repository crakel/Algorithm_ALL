import sys
import heapq

INF = float('INF')

v, e = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
dist = [INF] * (v + 1)
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if dist[cur] < cur_dist:
            continue
        for x in graph[cur]:
            cost = cur_dist + x[1]
            if cost < dist[x[0]]:
                dist[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))

dijkstra(k)
for i in range(1, v+1):
    if dist[i] == INF:
        print('INF')
    else: print(dist[i])


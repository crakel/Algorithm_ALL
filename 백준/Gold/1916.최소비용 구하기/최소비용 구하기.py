import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = float('inf')

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().strip().split())

def dijkstra(start):
    queue = []
    dist[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        cur_dist, cur = heapq.heappop(queue)
        if cur_dist > dist[cur]:
            continue
        for x in graph[cur]:
            cost = cur_dist + x[1]
            if cost < dist[x[0]]:
                dist[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))

dijkstra(start)
print(dist[end])
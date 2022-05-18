import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for i in range(V + 1)]

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

queue = []
distances = [float('inf') for i in range(V + 1)]
distances[K] = 0
heapq.heappush(queue, (0, K))

while queue:
    dist, node = heapq.heappop(queue)
    if distances[node] < dist:
        continue

    for adj, adj_dist in graph[node]:
        tmp = dist + adj_dist
        if distances[adj] > tmp:
            distances[adj] = tmp
            heapq.heappush(queue, (tmp, adj))

for i in distances[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)

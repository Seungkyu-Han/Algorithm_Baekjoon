import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for i in range(N + 1)]

for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())

distances = [float('inf') for i in range(N + 1)]
distances[start] = 0
queue = []
heapq.heappush(queue, (0, start))

while queue:
    dist, node = heapq.heappop(queue)

    if dist > distances[node]:
        continue

    for adj, adj_dist in graph[node]:
        tmp = distances[node] + adj_dist
        if tmp < distances[adj]:
            distances[adj] = tmp
            heapq.heappush(queue, (tmp, adj))

print(distances[end])

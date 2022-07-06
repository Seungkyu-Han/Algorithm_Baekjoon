import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(N+1)}

for i in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])

result = [0] * (N + 1)

for i in range(1, N + 1):
    if N == X:
        continue
    dijk = [float('inf')] * (N + 1)
    dijk[i] = 0
    need_visit = []
    heapq.heappush(need_visit, [0, i]) # dist, node
    while need_visit:

        cur_dist, cur_node = heapq.heappop(need_visit)

        if cur_dist > dijk[cur_node]:
            continue

        for end_node, dist in graph[cur_node]:
            distance = dist + cur_dist
            if distance < dijk[end_node]:
                dijk[end_node] = distance
                heapq.heappush(need_visit, [distance, end_node])

    result[i] = dijk[X]

dijk = [float('inf')] * (N + 1)
dijk[X] = 0
need_visit = []
heapq.heappush(need_visit, [0, X])
while need_visit:
    cur_dist, cur_node = heapq.heappop(need_visit)

    if cur_dist > dijk[cur_node]:
        continue

    for end_node, dist in graph[cur_node]:
        distance = dist + cur_dist
        if distance < dijk[end_node]:
            dijk[end_node] = distance
            heapq.heappush(need_visit, [distance, end_node])

for i in range(1, N + 1):
    result[i] += dijk[i]
    
print(max(result))

import heapq
import sys

ver = int(sys.stdin.readline())
bus_cnt = int(sys.stdin.readline())

graph = {i + 1: [] for i in range(ver)}

for i in range(bus_cnt):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((weight, end))

start_node, end_node = map(int, sys.stdin.readline().split())

weight_result = [float('inf')] * (ver + 1)
way_result = [list() for i in range(ver + 1)]
way_result[start_node].append(start_node)
weight_result[start_node] = 0
need_visit = []
heapq.heappush(need_visit, [0, start_node])

while need_visit:
    cur_weight, cur_node = heapq.heappop(need_visit)
    if cur_weight > weight_result[cur_node]:
        continue
    for weight, end in graph[cur_node]:
        if weight_result[end] > weight_result[cur_node] + weight:
            weight_result[end] = weight_result[cur_node] + weight
            way_result[end] = way_result[cur_node] + [end]
            heapq.heappush(need_visit, [weight_result[end], end])

print(weight_result[end_node])
print(len(way_result[end_node]))
print(*way_result[end_node])

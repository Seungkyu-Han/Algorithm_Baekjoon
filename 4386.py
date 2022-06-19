import sys
import heapq

num = int(sys.stdin.readline())

star = []

for i in range(num):
    star1, star2 = map(float, sys.stdin.readline().split())
    star.append((star1, star2))

graph = {i: [] for i in range(num)}

for i in range(num):
    for t in range(num):
        distance = ((star[i][0] - star[t][0]) ** 2 + (star[i][1] - star[t][1]) ** 2) ** 0.5
        graph[i].append((distance, t))


visited = set()
visited.add(0)

need_visit = graph[0]
heapq.heapify(need_visit)

result = 0

while need_visit:
    cur_dis, cur_node = heapq.heappop(need_visit)
    if cur_node in visited:
        continue

    visited.add(cur_node)
    result += cur_dis

    for di, node in graph[cur_node]:
        if node not in visited:
            heapq.heappush(need_visit, (di, node))

print(result)

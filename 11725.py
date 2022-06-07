from collections import deque
import sys

num = int(sys.stdin.readline())

graph = {i + 1: [] for i in range(num)}

for i in range(num - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

result = [0] * (num + 1)
need_visit = deque()
need_visit.append(1)

while need_visit:
    cur = need_visit.popleft()
    target_list = graph[cur]
    for i in graph[cur]:
        if result[i] != 0:
            continue
        result[i] = cur
        need_visit.append(i)

for i in result[2:]:
    print(i)

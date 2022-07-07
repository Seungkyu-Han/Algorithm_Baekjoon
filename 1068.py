import sys
from collections import deque

N = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

graph = {i: [] for i in range(N)}
graph[-1] = []

for i in range(N):
    graph[parent[i]].append(i)

need_visit = deque()
need_visit.append(target)

while need_visit:
    cur = need_visit.popleft()

    for i in graph[cur]:
        need_visit.append(i)

    graph.pop(cur)

keys = graph.keys()

result = 0

graph[parent[target]].remove(target)

for i in keys:
    if len(graph[i]) == 0 and i != -1:
        result += 1

print(result)

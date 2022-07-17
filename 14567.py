from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N + 1)
graph = {i+1: [] for i in range(N)}
result = [1] * (N + 1)
need_visit = deque()

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    indegree[end] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        need_visit.append(i)

while need_visit:
    cur_node = need_visit.popleft()

    for i in graph[cur_node]:
        indegree[i] -= 1
        result[i] = max(result[cur_node] + 1, result[i])
        if indegree[i] == 0:
            need_visit.append(i)

print(*result[1:])

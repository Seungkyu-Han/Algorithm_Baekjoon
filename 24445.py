import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = dict()

for i in range(1, N + 1):
    graph[i] = deque()

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i], reverse=True)

need_visit = deque()
need_visit.append(R)
visited = [True for i in range(N)]
result = [0 for i in range(N)]
ptr = 1

while need_visit:
    data = need_visit.popleft()
    if visited[data - 1]:
        need_visit.extend(graph[data])
        visited[data - 1] = False
        result[data - 1] = ptr
        ptr += 1

for i in result:
    print(i)

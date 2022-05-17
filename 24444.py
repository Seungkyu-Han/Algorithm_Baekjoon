import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = dict()

for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i+1] = sorted(graph[i+1])

need_visit = deque()
need_visit.append(R)
visited = [True for i in range(N)]
result = [0 for i in range(N)]
cnt = 1
while need_visit:
    data = need_visit.popleft()
    if visited[data - 1]:
        need_visit.extend(graph[data])
        visited[data - 1] = False
        result[data - 1] = cnt
        cnt += 1


for i in result:
    print(i)

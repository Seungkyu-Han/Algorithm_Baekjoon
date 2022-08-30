from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N + 1)
indegree[0] = -1
graph = {i + 1: [] for i in range(N)}

for i in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))

    for index in range(1, tmp[0]):
        graph[tmp[index]].append(tmp[index + 1])
        indegree[tmp[index + 1]] += 1

visited = [True] * (N + 1)
visited[0] = False
result = []

while 0 in indegree:

    for i in range(1, N + 1):
        if indegree[i] == 0:
            visited[i] = False
            indegree[i] = -1
            result.append(i)
            for index in graph[i]:
                indegree[index] -= 1

if True in visited:
    print(0)
else:
    for i in result:
        print(i)

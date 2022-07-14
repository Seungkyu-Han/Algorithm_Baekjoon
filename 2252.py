from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N + 1)
graph = {i + 1: [] for i in range(N)}

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    indegree[end] += 1


def jammin():
    result = deque()
    queue = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)


    while queue:
        cur = queue.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

jammin()

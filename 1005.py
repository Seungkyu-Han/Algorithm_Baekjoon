from collections import deque
import sys

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    N, K = map(int, sys.stdin.readline().split())
    need_time = list(map(int, sys.stdin.readline().split()))

    building = []
    result = [0] + list(need_time)
    indegree = [0] * (N + 1)
    graph = {i + 1: [] for i in range(N)}
    need_visit = deque()

    for i in range(K):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        indegree[end] += 1

    go = int(sys.stdin.readline())

    for i in range(1, N + 1):
        if indegree[i] == 0:
            need_visit.append(i)

    while need_visit:
        cur = need_visit.popleft()

        for i in graph[cur]:
            result[i] = max(result[i], result[cur] + need_time[i-1])
            indegree[i] -= 1
            if indegree[i] == 0:
                need_visit.append(i)

    print(result[go])

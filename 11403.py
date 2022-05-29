from collections import deque
import sys

num = int(sys.stdin.readline())

graph = dict()

for i in range(num):
    graph[i] = []
    tmp_list = list(map(int, sys.stdin.readline().split()))
    for t in range(num):
        if tmp_list[t] == 1:
            graph[i].append(t)\

result = []

for i in range(num):
    need_visit = deque()
    need_visit.extend(graph[i])
    visited = set()
    visited = visited.union(set(graph[i]))
    while need_visit:
        cur = need_visit.popleft()
        for t in graph[cur]:
            if t not in visited:
                need_visit.append(t)
                visited.add(t)
    tmp_result = []
    for t in range(num):
        if t in visited:
            tmp_result.append(1)
        else:
            tmp_result.append(0)
    result.append(tmp_result)

for i in range(num):
    print(*result[i])

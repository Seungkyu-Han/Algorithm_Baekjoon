import sys


def fs(graph_dict, start_node):
    need_visit = [start_node]
    visited = []
    while need_visit:
        tmp = need_visit.pop()
        if tmp not in visited:
            visited.append(tmp)
            need_visit.extend(graph_dict[tmp])
    return visited


N, M = map(int, sys.stdin.readline().split())

graph = dict()

for i in range(N):
    graph[i+1] = []

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

result_visited = []
total = 0

for i in range(1, N + 1):
    if i not in result_visited:
        total += 1
        result_visited.extend(fs(graph, i))

print(total)

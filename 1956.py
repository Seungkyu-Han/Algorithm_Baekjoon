import sys

V, E = map(int, sys.stdin.readline().split())

graph = [[1e9] * (V + 1) for i in range(V + 1)]

for i in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start][end] = weight


for i in range(1, V + 1):
    for t in range(1, V + 1):
        for k in range(1, V + 1):
            graph[t][k] = min(graph[t][k], graph[t][i] + graph[i][k])

result = 1e9

for i in range(1, V + 1):
    result = min(result, graph[i][i])

if result == 1e9:
    print(-1)
else:
    print(result)

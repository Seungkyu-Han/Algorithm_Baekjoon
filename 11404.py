import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[float('inf')] * (n + 1) for i in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for i in range(1, n + 1):
    for t in range(1, n + 1):
        for k in range(1, n + 1):
            graph[t][k] = min(graph[t][k], graph[t][i] + graph[i][k])

for i in range(1, n + 1):
    for t in range(1, n + 1):
        if graph[i][t] == float('inf'):
            print(0, end = ' ')
        else:
            print(graph[i][t], end = ' ')
    print()

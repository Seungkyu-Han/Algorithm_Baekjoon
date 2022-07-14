import sys

n, m, r = map(int, sys.stdin.readline().split())

item = list(map(int, sys.stdin.readline().split()))

flow = [[float('inf')] * n for i in range(n)]
for i in range(n):
    flow[i][i] = 0

for i in range(r):
    start, end, t = map(int, sys.stdin.readline().split())
    flow[start-1][end-1] = min(flow[start-1][end-1], t)
    flow[end-1][start-1] = min(flow[end-1][start-1], t)

for i in range(n):
    for t in range(n):
        for k in range(n):
            flow[t][k] = min(flow[t][k], flow[t][i] + flow[i][k])

result = 0

for i in range(n):
    tmp = 0
    for t in range(n):
        if flow[i][t] <= m:
            tmp += item[t]
    result = max(result, tmp)

print(result)

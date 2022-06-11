from collections import deque
import sys

V = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, sys.stdin.readline().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

def bfs(target):
    weight = [-1] * (V + 1)
    weight[target] = 0
    need_visit = deque()
    need_visit.append(target)
    result = [0, 0]

    while need_visit:
        cur = need_visit.popleft()
        for v, w in graph[cur]:
            if weight[v] == -1:
                weight[v] = weight[cur] + w
                need_visit.append(v)
                if result[0] < weight[v]:
                    result = [weight[v], v]

    return result


print(bfs(bfs(1)[1])[0])

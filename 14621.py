import sys

N, M = map(int, sys.stdin.readline().split())

univ = list(sys.stdin.readline().split())

graph = []

for i in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())

    if ord(univ[start-1]) - ord(univ[end-1]) == 0:
        continue

    graph.append((weight, start, end))

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = parent[root1]

    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = parent[root2]


graph.sort()

total = 0

for weight, start, end in graph:
    if find(start) != find(end):
        union(start, end)
        total += weight


target = find(1)
flag = True

for i in range(2, N + 1):
    if find(i) != target:
        flag = False
        break

if flag:
    print(total)
else:
    print(-1)

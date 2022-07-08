import heapq
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = []

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(graph, [c, a, b])

rank = [0] * (N + 1)
parent = [i for i in range(N + 1)]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


result = 0

while graph:
    cur_dist, cur_node1, cur_node2 = heapq.heappop(graph)

    if find(cur_node1) == find(cur_node2):
        continue

    union(cur_node1, cur_node2)
    result += cur_dist

print(result)

import sys

N, M = map(int, sys.stdin.readline().split())

graph = []

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append([C, A, B])

graph.sort(reverse=True)

result = 0
cnt = 0

rank = [0 for i in range(N + 1)]
parent = [i for i in range(N + 1)]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = root2


def find(target_node):
    if parent[target_node] != target_node:
        parent[target_node] = find(parent[target_node])
    return parent[target_node]


while cnt < N - 2:
    cur_dist, cur_node1, cur_node2 = graph.pop()
    if find(cur_node1) != find(cur_node2):
        union(cur_node1, cur_node2)
        result += cur_dist
        cnt += 1


print(result)

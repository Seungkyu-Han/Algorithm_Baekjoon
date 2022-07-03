import sys

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


for i in range(m):
    ans, a, b = map(int, sys.stdin.readline().split())
    if ans == 0:
        if find(a) != find(b):
            union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

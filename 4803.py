import sys

cnt = 1

while True:
    n, m = map(int, sys.stdin.readline().split())
    tree = 0

    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    rank[0] = 600


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
            if rank[root1] == rank[root2]:
                rank[root2] += 1
            parent[root1] = root2

    for i in range(m):
        ver1, ver2 = map(int, sys.stdin.readline().split())
        if find(ver1) == find(ver2):
            union(0, ver1)
            union(0, ver2)
        else:
            union(ver1, ver2)

    result = [False] * (n + 1)
    for i in range(1, n + 1):
        result[find(i)] = True
    result[0] = False
    go = result.count(True)
    if go <= 0:
        print(f"Case {cnt}: No trees.")
    elif go == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: A forest of {go} trees.")
    cnt += 1

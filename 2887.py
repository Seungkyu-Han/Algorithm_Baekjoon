import sys
import heapq

N = int(sys.stdin.readline())

star = []

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    star.append([a, b, c, i])

parent = [i for i in range(N)]
rank = [0] * N

dist = []
result = 0


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = parent[node1]
    root2 = parent[node2]

    if rank[root1] > rank[root2]:
        parent[root2] = parent[root1]
    else:
        if rank[root1] == rank[root2]:
            rank[root2] += 1
        parent[root1] = parent[root2]


for i in range(3):
    star.sort(key=lambda x: x[i])
    for t in range(N - 1):
        heapq.heappush(dist, [star[t+1][i] - star[t][i], star[t][3], star[t+1][3]])

while dist:
    length, ver1, ver2 = heapq.heappop(dist)
    if find(ver1) == find(ver2):
        continue

    union(ver1, ver2)
    result += length

print(result)

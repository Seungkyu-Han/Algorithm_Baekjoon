from collections import deque
import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

ver = []
line = []

for i in range(N):
    ver.append(list(map(int, sys.stdin.readline().split())))

for i in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))

graph = []

for i in range(N):
    for t in range(N):
        if i < t:
            dist = ((ver[i][0] - ver[t][0]) ** 2 + (ver[i][1] - ver[t][1]) ** 2) ** 0.5
            graph.append([dist, i, t])

for start, end in line:
    graph.append([0, start - 1, end - 1])

graph.sort()

rank = dict()
parent = dict()

for i in range(N):
    rank[i] = 0
    parent[i] = i


# 부모노드를 찾아줌
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


def kruskal(edges):
    result = 0
    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            result += weight
            union(node1, node2)
    return result


print(f'{kruskal(graph):.2f}')

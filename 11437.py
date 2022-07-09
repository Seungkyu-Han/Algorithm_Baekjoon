import sys
from collections import deque

N = int(sys.stdin.readline())

parent = [i for i in range(N + 1)]
root = [i for i in range(N + 1)]
rank = [0] * (N + 1)


def find(node):
    if root[node] != 1 and root[node] != node:
        root[node] = find(root[node])
    return root[node]


def union(node1, node2):
    if find(node1) == 1:
        parent[node2] = node1
        root[node2] = 1
    else:
        parent[node1] = node2
        root[node1] = 1


need_visit = deque()

for i in range(N - 1):
    first, second = map(int, sys.stdin.readline().split())
    if find(first) == 1:
        union(first, second)
        rank[second] = rank[first] + 1
    elif find(second) == 1:
        union(first, second)
        rank[first] = rank[second] + 1
    else:
        need_visit.append([first, second])

while need_visit:
    first, second = need_visit.popleft()
    if find(first) == 1:
        union(first, second)
        rank[second] = rank[first] + 1
    elif find(second) == 1:
        union(first, second)
        rank[first] = rank[second] + 1
    else:
        need_visit.append([first, second])

find_cnt = int(sys.stdin.readline())


result = []

for i in range(find_cnt):
    first, second = map(int, sys.stdin.readline().split())
    if rank[first] > rank[second]:
        while rank[first] != rank[second]:
            first = parent[first]
    elif rank[second] > rank[first]:
        while rank[first] != rank[second]:
            second = parent[second]

    while first != second:
        first = parent[first]
        second = parent[second]

    result.append(first)

for i in result:
    print(i)

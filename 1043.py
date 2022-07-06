import sys

N, M = map(int, sys.stdin.readline().split())

truth = list(map(int, sys.stdin.readline().split()))

fact = [False] * (N + 1)

for i in truth[1:]:
    fact[i] = True

party = []

for i in range(M):
    party.append(list(map(int, sys.stdin.readline().split())))

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


for i in range(M):
    if party[i][0] < 2:
        continue
    target = party[i][1]
    for t in party[i][2:]:
        union(target, t)

if truth[0] > 0:
    for i in truth[1:]:
        fact[find(i)] = True

result = 0

for i in range(M):
    if not fact[find(party[i][1])]:
        result += 1

print(result)

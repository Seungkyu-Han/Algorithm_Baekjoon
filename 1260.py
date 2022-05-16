import sys

N, M, V = map(int, sys.stdin.readline().split())

mydict = dict()
for i in range(N):
    mydict[i + 1] = []

for i in range(M):
    a, b = map(int, input().split())
    mydict[a].append(b)
    mydict[b].append(a)

for_dfs = dict(mydict)
dfs = []
dfs_need_visit = [V]
dfs_visited = []

for_bfs = dict(mydict)
bfs = []
bfs_need_visit = [V]
bfs_visited = []


while dfs_need_visit:
    data = dfs_need_visit.pop()
    if data not in dfs_visited:
        dfs_need_visit.extend(reversed(sorted(for_dfs[data])))
        dfs_visited.append(data)

while bfs_need_visit:
    data = bfs_need_visit.pop(0)
    if data not in bfs_visited:
        bfs_need_visit.extend(sorted(for_bfs[data]))
        bfs_visited.append(data)

for i in dfs_visited:
    print(i, end=' ')

print()

for i in bfs_visited:
    print(i, end=' ')

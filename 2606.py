cnt = int(input())

num = int(input())

graph = dict()

for i in range(cnt):
    graph[i+1] = []

for i in range(num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

need_visit = [1]
visited = []

while need_visit:
    data = need_visit.pop()
    if data not in visited:
        need_visit.extend(graph[data])
        visited.append(data)

print(len(visited) - 1)

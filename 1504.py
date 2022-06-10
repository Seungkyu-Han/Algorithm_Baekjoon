from collections import deque
import sys

N, E = map(int, sys.stdin.readline().split())

graph = {i+1: [] for i in range(N)}

for i in range(E):
    start, end, length = map(int, sys.stdin.readline().split())
    graph[start].append((end, length))
    graph[end].append((start, length))

node1, node2 = map(int, sys.stdin.readline().split())

start_length = [float('inf')] * (N + 1)
start_length[1] = 0
node1_length = [float('inf')] * (N + 1)
node1_length[node1] = 0
node2_length = [float('inf')] * (N + 1)
node2_length[node2] = 0

need_visit = deque()
need_visit.append(1)

while need_visit:
    cur = need_visit.popleft()
    cur_list = graph[cur]
    cur_length = start_length[cur]
    for i in cur_list:
        if start_length[i[0]] > cur_length + i[1]:
            start_length[i[0]] = cur_length + i[1]
            need_visit.append(i[0])

need_visit.clear()
need_visit.append(node1)

while need_visit:
    cur = need_visit.popleft()
    cur_list = graph[cur]
    cur_length = node1_length[cur]
    for i in cur_list:
        if node1_length[i[0]] > cur_length + i[1]:
            node1_length[i[0]] = cur_length + i[1]
            need_visit.append(i[0])

need_visit.clear()
need_visit.append(node2)

while need_visit:
    cur = need_visit.popleft()
    cur_list = graph[cur]
    cur_length = node2_length[cur]
    for i in cur_list:
        if node2_length[i[0]] > cur_length + i[1]:
            node2_length[i[0]] = cur_length + i[1]
            need_visit.append(i[0])

case1 = start_length[node1] + node1_length[node2] + node2_length[N]
case2 = start_length[node2] + node2_length[node1] + node1_length[N]

if case1 == float('inf') and case2 == float('inf'):
    print(-1)
else:
    print(min(case1, case2))

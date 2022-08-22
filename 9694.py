import sys
import heapq

TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())

    graph = {i: [] for i in range(M)}

    for i in range(N):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    need_visit = []
    visited = [1e9] * M
    visited[0] = 0
    way = [[i] for i in range(M)]
    heapq.heappush(need_visit, (0, 0))  # weight, node

    while need_visit:

        cur_weight, cur_node = heapq.heappop(need_visit)

        if cur_weight > visited[cur_node]:
            continue

        for go_node, go_weight in graph[cur_node]:
            if visited[go_node] > cur_weight + go_weight:
                visited[go_node] = cur_weight + go_weight
                heapq.heappush(need_visit, (cur_weight + go_weight, go_node))
                way[go_node] = way[cur_node] + [go_node]

    if visited[-1] != 1e9:
        print(f'Case #{_ + 1}: ', end='')
        print(*way[-1])
    else:
        print(f'Case #{_ + 1}: ', end='')
        print(-1)

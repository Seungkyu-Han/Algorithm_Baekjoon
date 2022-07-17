import heapq
import sys


def dijkstra(start_point):
    need_visit = []
    heapq.heappush(need_visit, [0, start_point])
    visited = [100000000] * (n + 1)
    visited[start_point] = 0
    while need_visit:

        cur_weight, cur_node = heapq.heappop(need_visit)

        if cur_weight > visited[cur_node]:
            continue

        for node, weight in graph[cur_node]:
            distance = weight + cur_weight
            if visited[node] > distance:
                visited[node] = distance
                heapq.heappush(need_visit, [distance, node])
    return visited


T = int(sys.stdin.readline())

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = {i + 1: [] for i in range(n)}
    de = []

    for i in range(m):
        start, end, length = map(int, sys.stdin.readline().split())
        graph[start].append([end, length])
        graph[end].append([start, length])

    for i in range(t):
        de.append(int(sys.stdin.readline()))

    s_list = dijkstra(s)
    g_list = dijkstra(g)
    h_list = dijkstra(h)

    ans = []

    for i in de:
        if s_list[g] + g_list[h] + h_list[i] == s_list[i] or s_list[h] + h_list[g] + g_list[i] == s_list[i]:
            ans.append(i)

    ans.sort()

    print(*ans)

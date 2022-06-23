import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

if N >= K:
    print(N - K)
else:
    need_visit = []
    visited = [float('inf')] * 100001
    heapq.heappush(need_visit, [0, N])
    while visited[K] == float('inf'):
        time, cur = heapq.heappop(need_visit)

        if visited[cur] < time:
            continue
        if 0 <= cur - 1 <= 100000:
            if visited[cur - 1] > time + 1:
                visited[cur - 1] = time + 1
                heapq.heappush(need_visit, [time + 1, cur - 1])
        if 0 <= cur + 1 <= 100000:
            if visited[cur + 1] > time + 1:
                visited[cur + 1] = time + 1
                heapq.heappush(need_visit, [time + 1, cur + 1])
        if 0 <= cur * 2 <= 100000:
            if visited[cur * 2] > time:
                visited[cur * 2] = time
                heapq.heappush(need_visit, [time, cur * 2])

    print(visited[K])

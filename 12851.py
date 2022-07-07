import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

if N >= K:
    print(N - K)
    print(1)
else:
    visited = [float('inf')] * (K + 1)
    visited[N] = 0
    need_visit = []
    heapq.heappush(need_visit, [0, N])
    result = 0

    while need_visit:

        cur_cnt, loc = heapq.heappop(need_visit)

        if visited[K] < cur_cnt:
            break

        if visited[loc] < cur_cnt:
            continue

        for go in (loc - 1, loc + 1, loc * 2):
            if go < 0:
                continue
            elif 0 <= go < K:
                if cur_cnt + 1 <= visited[go]:
                    visited[go] = cur_cnt + 1
                    heapq.heappush(need_visit, [cur_cnt + 1, go])
            elif go == K:
                if visited[go] > cur_cnt + 1:
                    visited[go] = cur_cnt + 1
                    result = 1
                elif visited[go] == cur_cnt + 1:
                    result += 1
            else:
                time = go - K + (cur_cnt + 1)
                if visited[K] > time:
                    result = 1
                    visited[K] = time
                elif visited[K] == time:
                    result += 1

    print(visited[-1])
    print(result)

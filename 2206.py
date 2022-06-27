from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

miro = []

for i in range(N):
    miro.append(list(sys.stdin.readline().strip()))

visited = [[float('inf')] * M for i in range(N)]
visited[0][0] = 1
broken = [[float('inf')] * M for i in range(N)]
need_visit = deque()
need_visit.appendleft([0, 0, False])  # n, m, broken_status

while visited[N - 1][M - 1] == float('inf') and broken[N - 1][M - 1] == float('inf') and need_visit:
    n, m, broken_status = need_visit.pop()

    if not broken_status:
        for go_n, go_m in ((n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)):
            if 0 <= go_n < N and 0 <= go_m < M:
                if miro[go_n][go_m] == '0':
                    if visited[go_n][go_m] > visited[n][m] + 1:
                        visited[go_n][go_m] = visited[n][m] + 1
                        need_visit.appendleft([go_n, go_m, False])
                else:
                    if broken[go_n][go_m] > visited[n][m] + 1:
                        broken[go_n][go_m] = visited[n][m] + 1
                        need_visit.appendleft([go_n, go_m, True])
    else:
        for go_n, go_m in ((n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)):
            if 0 <= go_n < N and 0 <= go_m < M:
                if miro[go_n][go_m] == '0':
                    if broken[go_n][go_m] > broken[n][m] + 1:
                        broken[go_n][go_m] = broken[n][m] + 1
                        need_visit.appendleft([go_n, go_m, True])

target1 = visited[-1][-1]
target2 = broken[-1][-1]

if target1 == float('inf') and target2 == float('inf'):
    print(-1)
elif target2 == float('inf'):
    print(target1)
elif target1 == float('inf'):
    print(target2)
else:
    print(min(target1, target2))

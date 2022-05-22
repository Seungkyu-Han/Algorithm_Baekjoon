from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

miro = [list(sys.stdin.readline().strip()) for i in range(N)]

visited = [[0] * M for t in range(N)]

need_visit = deque()
need_visit.append((0, 0))

visited[0][0] = 1

while need_visit:
    n, m = need_visit.popleft()

    if n == N - 1 and m == M - 1:
        print(visited[n][m])
        break

    for n_ptr, m_ptr in ((n - 1, m), (n + 1, m), (n, m - 1), (n, m + 1)):
        if 0 <= n_ptr < N and 0 <= m_ptr < M and visited[n_ptr][m_ptr] == 0 and miro[n_ptr][m_ptr] == '1':
            visited[n_ptr][m_ptr] = visited[n][m] + 1
            need_visit.append((n_ptr, m_ptr))

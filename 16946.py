from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

miro = []

for i in range(N):
    miro.append(list(map(int, sys.stdin.readline().strip())))

visited = [[0] * M for i in range(N)]
visited_index = [0]
cur_index = 1

for i in range(N):
    for t in range(M):
        if miro[i][t] == 0 and visited[i][t] == 0:

            need_visit = deque()
            need_visit.append((i, t))
            visited[i][t] = cur_index
            cur_cnt = 1

            while need_visit:

                n, m = need_visit.popleft()

                for n_ptr, m_ptr in ((n-1, m), (n+1, m), (n, m-1), (n, m+1)):
                    if 0 <= n_ptr < N and 0 <= m_ptr < M and miro[n_ptr][m_ptr] == 0 and visited[n_ptr][m_ptr] == 0:
                        cur_cnt += 1
                        visited[n_ptr][m_ptr] = cur_index
                        need_visit.append((n_ptr, m_ptr))

            cur_index += 1
            visited_index.append(cur_cnt)


for i in range(N):
    for t in range(M):
        if miro[i][t] == 0:
            print(0, end='')
        else:
            tmp = set()
            result = 1

            for n_ptr, m_ptr in ((i-1, t), (i+1, t), (i, t-1), (i, t+1)):
                if 0 <= n_ptr < N and 0 <= m_ptr < M and miro[n_ptr][m_ptr] == 0 and visited[n_ptr][m_ptr] not in tmp:
                    result += visited_index[visited[n_ptr][m_ptr]]
                    tmp.add(visited[n_ptr][m_ptr])
            print(result % 10, end='')
    print()

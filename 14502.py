from collections import deque
import sys
import copy

N, M = map(int, sys.stdin.readline().split())

lab = []
virus = []

for i in range(N):
    lab.append(list(map(int, sys.stdin.readline().split())))
    for t in range(M):
        if lab[-1][t] == 2:
            virus.append((i, t))

result = 0


def bfs():
    tmp = copy.deepcopy(lab)
    for n, m in virus:

        need_visit = deque()
        need_visit.append((n, m))

        while need_visit:

            cur_n, cur_m = need_visit.popleft()

            tmp[cur_n][cur_m] = 2

            for n_ptr, m_ptr in ((cur_n + 1, cur_m), (cur_n-1, cur_m), (cur_n, cur_m-1), (cur_n, cur_m+1)):
                if 0 <= n_ptr < N and 0 <= m_ptr < M and tmp[n_ptr][m_ptr] == 0:
                    tmp[n_ptr][m_ptr] = 2
                    need_visit.append((n_ptr, m_ptr))

    cur = 0
    for q in range(N):
        for k in range(M):
            if tmp[q][k] == 0:
                cur += 1

    global result
    result = max(result, cur)


def solve(n):
    if n == 3:
        bfs()
        return

    for q in range(N):
        for k in range(M):
            if lab[q][k] == 0:
                lab[q][k] = 1
                solve(n+1)
                lab[q][k] = 0


solve(0)

print(result)

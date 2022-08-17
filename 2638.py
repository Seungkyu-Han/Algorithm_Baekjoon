from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

cheese = []

for i in range(N):
    cheese.append(list(map(int, sys.stdin.readline().split())))


def solve():
    tmp = [[0] * M for _ in range(N)]

    tmp[0][0] = -1
    plus = []

    need_visit = deque()
    need_visit.append((0, 0))

    while need_visit:
        n, m = need_visit.popleft()

        for n_ptr, m_ptr in ((n+1, m), (n-1, m), (n, m+1), (n, m-1)):
            if 0 <= n_ptr < N and 0 <= m_ptr < M:
                if tmp[n_ptr][m_ptr] == -1:
                    continue
                elif tmp[n_ptr][m_ptr] == 1:
                    plus.append((n_ptr, m_ptr))
                else:
                    if cheese[n_ptr][m_ptr] == 0:
                        tmp[n_ptr][m_ptr] = -1
                        need_visit.append((n_ptr, m_ptr))
                    else:
                        tmp[n_ptr][m_ptr] += 1

    if not plus:
        return False

    for n_ptr, m_ptr in plus:
        cheese[n_ptr][m_ptr] = 0

    return True


cur = 0

while solve():
    cur += 1
    
print(cur)

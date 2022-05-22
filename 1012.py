import sys
from collections import deque

rep_cnt = int(sys.stdin.readline())
for rep in range(rep_cnt):
    M, N, K = map(int, sys.stdin.readline().split())

    total_veg = [[False] * M for i in range(N)]
    veg = deque()

    for i in range(K):
        m, n = map(int, sys.stdin.readline().split())
        veg.append([n, m])
        total_veg[n][m] = True

    cnt = 0

    while veg:
        tn, tm = veg.popleft()
        if not(total_veg[tn][tm]):
            continue
        need_visit = deque()
        need_visit.append([tn, tm])
        total_veg[tn][tm] = False
        while need_visit:
            n, m = need_visit.popleft()
            for n_ptr, m_ptr in ((n - 1, m), (n + 1, m), (n, m - 1), (n, m + 1)):
                if 0 <= n_ptr < N and 0 <= m_ptr < M and total_veg[n_ptr][m_ptr]:
                    need_visit.append([n_ptr, m_ptr])
                    total_veg[n_ptr][m_ptr] = False
        cnt += 1
    print(cnt)

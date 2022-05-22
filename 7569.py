from collections import deque
import sys
import itertools

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[None] * N for i in range(H)]

need_visit = deque()
end_cnt = 0

for i in range(N * H):
    tmp_ans = list(map(int, sys.stdin.readline().split()))
    for t in range(M):
        if tmp_ans[t] == 1:
            need_visit.append((i // N, i % N, t))
        elif tmp_ans[t] == 0:
            end_cnt += 1
    tomato[i // N][i % N] = tmp_ans

cnt = 0

while need_visit:
    tmp_deque = deque(need_visit)
    to_change = deque()
    while tmp_deque:
        h, n, m = tmp_deque.pop()
        for h_ptr, n_ptr, m_ptr in ((h + 1, n, m), (h - 1, n, m), (h, n + 1, m), (h, n - 1, m), (h, n, m + 1), (h, n, m - 1)):
            if 0 <= h_ptr < H and 0 <= n_ptr < N and 0 <= m_ptr < M and tomato[h_ptr][n_ptr][m_ptr] == 0:
                to_change.append((h_ptr, n_ptr, m_ptr))
                tomato[h_ptr][n_ptr][m_ptr] = 1
    cnt += 1
    need_visit = deque(to_change)

flat = list(itertools.chain(*list(itertools.chain(*tomato))))

if end_cnt == 0:
    print(0)
elif 0 in flat:
    print(-1)
else:
    print(cnt-1)

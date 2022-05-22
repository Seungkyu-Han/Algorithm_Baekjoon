from collections import deque
import sys
import itertools

M, N = map(int, sys.stdin.readline().split())

tomato = [[None]] * N

end_cnt = 0
cnt = 0

need_visit = deque()

for i in range(N):
    tmp_ans = list(map(int, sys.stdin.readline().split()))
    for t in range(M):
        if tmp_ans[t] == 0:
            end_cnt += 1
        elif tmp_ans[t] == 1:
            need_visit.append((i, t))
    tomato[i] = tmp_ans

while need_visit:
    tmp_need_visit = deque()
    while need_visit:
        n, m = need_visit.pop()
        for n_ptr, m_ptr in ((n - 1, m), (n + 1, m), (n, m - 1), (n, m + 1)):
            if 0 <= n_ptr < N and 0 <= m_ptr < M and tomato[n_ptr][m_ptr] == 0:
                tomato[n_ptr][m_ptr] = 1
                tmp_need_visit.append((n_ptr, m_ptr))
    need_visit = deque(tmp_need_visit)
    cnt += 1

flat = list(itertools.chain(list(itertools.chain(*tomato))))

if end_cnt == 0:
    print(0)
elif 0 in flat:
    print(-1)
else:
    print(cnt-1)

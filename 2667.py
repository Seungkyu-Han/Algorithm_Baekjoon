import sys

N = int(sys.stdin.readline())

apt = []

cnt_list = []

for i in range(N):
    tmp_ans = list(sys.stdin.readline().strip())
    apt.append(tmp_ans)

for i in range(N):
    for t in range(N):
        if apt[i][t] == '0':
            continue
        need_visit = [(i, t)]
        apt[i][t] = '0'
        cnt = 1
        while need_visit:
            n, m = need_visit.pop()
            for n_ptr, m_ptr in ((n - 1, m), (n + 1, m), (n, m - 1), (n, m + 1)):
                if 0 <= n_ptr < N and 0 <= m_ptr < N and apt[n_ptr][m_ptr] == '1':
                    need_visit.append((n_ptr, m_ptr))
                    apt[n_ptr][m_ptr] = '0'
                    cnt += 1
        cnt_list.append(cnt)

print(len(cnt_list))
for i in sorted(cnt_list):
    print(i)

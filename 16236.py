from collections import deque
import sys

num = int(sys.stdin.readline())

bowl = []

for i in range(num):
    bowl.append(list(map(int, sys.stdin.readline().split())))

cur = [0, 0, 0]

for n in range(num):
    for m in range(num):
        if bowl[n][m] == 9:
            cur = [0, n, m]
            bowl[n][m] = 0

fish_size = 2
eat_cnt = 0
cnt = 0

while True:
    need_visit = deque()
    visited = [[True] * num for i in range(num)]
    visited[cur[1]][cur[2]] = False
    need_visit.append(cur)
    result = []
    while need_visit:
        cur_cnt, n, m = need_visit.popleft()
        for n_ptr, m_ptr in ((n - 1, m), (n, m - 1), (n, m + 1), (n + 1, m)):
            if 0 <= n_ptr < num and 0 <= m_ptr < num and visited[n_ptr][m_ptr]:
                if bowl[n_ptr][m_ptr] == 0:
                    visited[n_ptr][m_ptr] = False
                    need_visit.append([cur_cnt + 1, n_ptr, m_ptr])
                elif bowl[n_ptr][m_ptr] < fish_size:
                    result.append([cur_cnt + 1, n_ptr, m_ptr])
                    visited[n_ptr][m_ptr] = False
                elif bowl[n_ptr][m_ptr] == fish_size:
                    visited[n_ptr][m_ptr] = False
                    need_visit.append([cur_cnt + 1, n_ptr, m_ptr])
                else:
                    visited[n_ptr][m_ptr] = False
    if result:
        result.sort()
        result_cnt, result_n, result_m = result[0]
        bowl[result_n][result_m] = 0
        cnt += result_cnt
        eat_cnt += 1
        if fish_size < 7 and eat_cnt >= fish_size:
            eat_cnt = 0
            fish_size += 1
        cur = [0, result_n, result_m]
    else:
        break

print(cnt)

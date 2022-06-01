from collections import deque
import sys

num = int(sys.stdin.readline())

RGB = []

for i in range(num):
    RGB.append(list(sys.stdin.readline().strip()))

target = (0, 0)
first_visited = [[True] * num for i in range(num)]
first_visited[0][0] = False
first_cnt = 0

while target:
    first_cnt += 1
    need_visit = deque()
    need_visit.append(target)
    first_visited[target[0]][target[1]] = False
    target_color = RGB[target[0]][target[1]]
    while need_visit:
        n, m = need_visit.popleft()
        for n_ptr, m_ptr in ((n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)):
            if 0 <= n_ptr < num and 0 <= m_ptr < num and first_visited[n_ptr][m_ptr] and RGB[n_ptr][m_ptr] == target_color:
                first_visited[n_ptr][m_ptr] = False
                need_visit.append((n_ptr, m_ptr))
    cnt = 0
    while cnt < num * num and first_visited[cnt // num][cnt % num] is False:
        cnt += 1
    if cnt >= num * num:
        target = False
    else:
        target = (cnt // num, cnt % num)

for i in range(num):
    for t in range(num):
        if RGB[i][t] == 'R':
            RGB[i][t] = 'G'

target = (0, 0)
second_visited = [[True] * num for i in range(num)]
second_visited[0][0] = False
second_cnt = 0

while target:
    second_cnt += 1
    need_visit = deque()
    need_visit.append(target)
    second_visited[target[0]][target[1]] = False
    target_color = RGB[target[0]][target[1]]
    while need_visit:
        n, m = need_visit.popleft()
        for n_ptr, m_ptr in ((n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)):
            if 0 <= n_ptr < num and 0 <= m_ptr < num and second_visited[n_ptr][m_ptr] and RGB[n_ptr][m_ptr] == target_color:
                second_visited[n_ptr][m_ptr] = False
                need_visit.append((n_ptr, m_ptr))
    cnt = 0
    while cnt < num * num and second_visited[cnt // num][cnt % num] is False:
        cnt += 1
    if cnt >= num * num:
        target = False
    else:
        target = (cnt // num, cnt % num)

print(first_cnt, second_cnt)

import sys
from collections import deque

K, N = map(int, sys.stdin.readline().split())

num = list(map(str, sys.stdin.readline().split()))
target = ''.join(sorted(num))
limit = K ** 2

visited = set(''.join(num))
need_visit = deque()
need_visit.append((0, num))
result = -1

while need_visit:

    cur_cnt, cur_list = need_visit.popleft()

    if ''.join(cur_list) == target:
        result = cur_cnt
        break

    for i in range(K - N + 1):
        tmp = cur_list[:i] + list(reversed(cur_list[i:i + N])) + cur_list[i + N:]
        if ''.join(tmp) not in visited:
            visited.add(''.join(tmp))
            need_visit.append((cur_cnt + 1, tmp))


print(result)

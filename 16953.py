import sys
from collections import deque

start, end = map(int, sys.stdin.readline().split())

need_visit = deque()
need_visit.append([1, start])
result = -1
visited = set()

while need_visit:
    cur_cnt, cur = need_visit.popleft()
    if cur == end:
        result = cur_cnt
        break
    case1 = cur * 2
    case2 = int(str(cur) + '1')
    if case1 <= 1000000000 and case1 not in visited:
        visited.add(case1)
        need_visit.append([cur_cnt + 1, case1])
    if case2 <= 1000000000 and case2 not in visited:
        visited.add(case2)
        need_visit.append([cur_cnt + 1, case2])

print(result)

from collections import deque
import sys


def find_result(start_num, end_num):

    res = [True for k in range(10001)]
    need_visit = deque()
    need_visit.append((start_num, ''))
    while need_visit:
        cur, cur_str = need_visit.popleft()
        d = (cur * 2) % 10000
        s = (cur - 1) if cur != 0 else 9999
        t_l = (cur % 1000 * 10) + (cur // 1000)
        r = (cur % 10) * 1000 + (cur // 10)
        if d == end_num:
            return cur_str + 'D'
        elif res[d]:
            res[d] = False
            need_visit.append((d, cur_str + 'D'))
        if s == end_num:
            return cur_str + 'S'
        elif res[s]:
            res[s] = False
            need_visit.append((s, cur_str + 'S'))
        if t_l == end_num:
            return cur_str + 'L'
        elif res[t_l]:
            res[t_l] = False
            need_visit.append((t_l, cur_str + 'L'))
        if r == end_num:
            return cur_str + 'R'
        elif res[r]:
            res[r] = False
            need_visit.append((r, cur_str + 'R'))


cnt = int(sys.stdin.readline())

for i in range(cnt):
    start, end = map(int, sys.stdin.readline().split())
    print(find_result(start, end))

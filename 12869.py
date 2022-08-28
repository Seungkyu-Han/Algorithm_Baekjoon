from collections import deque
import sys

N = int(sys.stdin.readline())

scv = list(map(int, sys.stdin.readline().split()))

for i in range(3 - N):
    scv.append(0)

attack = [9, 3, 1]
visited = set()

need_visit = deque()

need_visit.append((0, scv))
result = 1e9

while need_visit:

    cur_cnt, cur_list = need_visit.popleft()
    if cur_list[0] <= 0 and cur_list[1] <= 0 and cur_list[2] <= 0:
        result = cur_cnt
        break

    make = []

    for i in range(3):
        for t in range(3):
            for k in range(3):
                if i != t and t != k and k != i:
                    make.append((cur_list[0] - attack[i], cur_list[1] - attack[t], cur_list[2] - attack[k]))

    for i in range(6):
        one = make[i][0] if make[i][0] > 0 else 0
        two = make[i][1] if make[i][1] > 0 else 0
        three = make[i][2] if make[i][2] > 0 else 0
        if (one, two, three) not in visited:
            visited.add((one, two, three))
            need_visit.append((cur_cnt + 1, (one, two, three)))

print(result)

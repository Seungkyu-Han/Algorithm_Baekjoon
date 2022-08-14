from collections import deque
import sys

n = int(sys.stdin.readline())

nature = [-1] * (n + 1)

need_visit = deque()
need_visit.append(n)
nature[n] = 0

while need_visit:

    cur = need_visit.popleft()

    if cur % 3 == 0 and nature[cur // 3] == -1:
        nature[cur // 3] = cur
        need_visit.append(cur // 3)

    if cur % 2 == 0 and nature[cur // 2] == -1:
        nature[cur // 2] = cur
        need_visit.append(cur // 2)

    if nature[cur-1] == -1:
        nature[cur - 1] = cur
        need_visit.append(cur - 1)

    if nature[1] != -1:
        break

result = deque()
cur = 1

while nature[cur] != 0:
    result.appendleft(cur)
    cur = nature[cur]

result.appendleft(cur)

print(len(result) - 1)
print(*result)

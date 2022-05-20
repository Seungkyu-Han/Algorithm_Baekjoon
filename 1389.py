import sys
from collections import deque


def kevin(friend_dict, target, length):
    result = {node: float('inf') for node in friend_dict}
    result[target] = 0
    need_visit = deque()
    need_visit.append((0, target))

    while need_visit:
        cnt, node = need_visit.popleft()

        for t in friend_dict[node]:
            if result[t] > cnt + 1:
                result[t] = cnt + 1
                need_visit.append((cnt + 1, t))

    total = 0
    for t in range(1, length + 1):
        total += result[t]

    return total


N, M = map(int, sys.stdin.readline().split())

friend = {node: [] for node in range(N + 1)}

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    friend[A].append(B)
    friend[B].append(A)

kevin_cnt = []

for i in range(N):
    kevin_cnt.append(kevin(friend, i + 1, N))

print(kevin_cnt.index(min(kevin_cnt)) + 1)

import sys

N, S, M = map(int, sys.stdin.readline().split())

diff = list(map(int, sys.stdin.readline().split()))

vol = [False] * (M + 1)
vol[S] = True

for i in range(N):
    tmp = [False] * (M + 1)
    for t in range(M + 1):
        if vol[t]:
            if t - diff[i] >= 0:
                tmp[t - diff[i]] = True
            if t + diff[i] <= M:
                tmp[t + diff[i]] = True
    vol = list(tmp)


def solve():
    for q in range(M, -1, -1):
        if vol[q]:
            return q

    return -1

print(solve())

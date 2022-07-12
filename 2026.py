import sys

K, N, F = map(int, sys.stdin.readline().split())

friend = {i+1: [] for i in range(N)}

for i in range(F):
    first, second = map(int, sys.stdin.readline().split())
    friend[first].append(second)
    friend[second].append(first)


def judge(plus_friend, members):
    for per in members:
        if per not in friend[plus_friend]:
            return False
    return True


def backtracking(per_cnt, cur_members):
    if per_cnt == K:
        for i in cur_members:
            print(i)
        exit(0)

    for i in range(cur_members[-1] + 1, N + 1):
        if judge(i, cur_members):
            backtracking(per_cnt + 1, cur_members + [i])

for i in range(1, N):
    backtracking(1, [i])

print(-1)

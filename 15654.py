import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

tmp = []


def result(start):
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(0, N):
        if num_list[i] not in tmp:
            tmp.append(num_list[i])
            result(i)
            tmp.pop()

result(0)

import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

num_list = list(set(num_list))
num_list.sort()

tmp = []


def result(start):
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(len(num_list)):
        if start == 0 or tmp[-1] <= num_list[i]:
            tmp.append(num_list[i])
            result(start + 1)
            tmp.pop()

result(0)

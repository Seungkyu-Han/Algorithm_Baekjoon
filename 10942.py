import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

result = [[-1] * N for i in range(N)]


def judge(start, end):
    if result[start][end] != -1:
        return result[start][end]

    if start == end:
        if nums[start] == nums[end]:
            result[start][end] = 1
            return 1
        else:
            result[start][end] = 0
            return 0

    if end - start == 1:
        if nums[start] == nums[end]:
            result[start][end] = 1
            return 1
        else:
            result[start][end] = 0
            return 0

    if nums[start] == nums[end]:
        result[start][end] = judge(start + 1, end - 1)
        return result[start][end]
    else:
        result[start][end] = 0
        return 0


cnt = int(sys.stdin.readline())
gogo = []

for i in range(cnt):
    left, right = map(int, sys.stdin.readline().split())
    tmp = judge(left - 1, right - 1)
    gogo.append(tmp)

for i in gogo:
    print(i)

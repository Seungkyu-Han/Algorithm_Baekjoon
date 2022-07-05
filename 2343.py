import sys

N, M = map(int, sys.stdin.readline().split())

video = list(map(int, sys.stdin.readline().split()))

total = sum(video)

left = max(video)
right = total


def solve(capacity):
    result = M
    cur = 0
    for i in video:
        if cur + i > capacity:
            cur = i
            result -= 1
        else:
            cur += i

    return True if result > 0 else False


while left <= right:
    mid = (left + right) // 2
    if solve(mid) and not solve(mid - 1):
        break
    elif not solve(mid):
        left = mid + 1
    else:
        right = mid - 1

print(mid)

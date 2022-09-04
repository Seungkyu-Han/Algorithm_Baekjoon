import sys

N = int(sys.stdin.readline())
squ = []

for i in range(N):
    squ.append(int(sys.stdin.readline()))


def solve(start, end):

    if start > end:
        return 0

    if start == end:
        return squ[start]

    mid = (start + end) // 2

    left = solve(start, mid)
    right = solve(mid + 1, end)

    result = squ[mid]
    height = squ[mid]

    le, r = mid, mid

    for q in range(end - start):
        if le == start:
            r += 1
            height = min(height, squ[r])
            result = max(result, (r - le + 1) * height)
            continue
        if r == end:
            le -= 1
            height = min(height, squ[le])
            result = max(result, (r - le + 1) * height)
            continue
        if squ[le - 1] > squ[r + 1]:
            le -= 1
            height = min(height, squ[le])
            result = max(result, (r - le + 1) * height)
            continue
        else:
            r += 1
            height = min(height, squ[r])
            result = max(result, (r - le + 1) * height)
            continue
    return max(left, right, result)

print(solve(0, N-1))

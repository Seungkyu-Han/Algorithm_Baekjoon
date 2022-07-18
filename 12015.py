import sys

N = int(sys.stdin.readline())
result = [0]

lis = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if lis[i] > result[-1]:
        result.append(lis[i])
    else:
        start, end = 0, len(result) - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2

            if result[mid] < lis[i] <= result[mid + 1]:
                break
            elif lis[i] > result[mid]:
                start = mid + 1
            else:
                end = mid - 1
        result[mid + 1] = lis[i]

print(len(result) - 1)

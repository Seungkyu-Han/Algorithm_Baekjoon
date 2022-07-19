import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

acc = [nums[0]]

result = acc[-1]

for i in range(1, n):
    acc.append(max(acc[-1] + nums[i], nums[i]))
    result = max(acc[-1], result)
print(result)

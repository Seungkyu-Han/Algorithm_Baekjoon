import sys

num = []
n = int(sys.stdin.readline())
result = 0

for i in range(n):
    num.append(1)
    tmp = float(sys.stdin.readline())
    for t in range(i + 1):
        num[t] = num[t] * tmp
        result = max(result, num[t])

print('%.3f'%result)

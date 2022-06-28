import sys

N = int(input())

lis = list(map(int, sys.stdin.readline().split()))

result = [None] * N

for i in range(N):
    tmp = [lis[i]]
    for t in range(i):
        if lis[i] > lis[t]:
            if len(tmp) < len(result[t]) + 1:
                tmp = result[t] + [lis[i]]
    result[i] = tmp

result.sort(key= lambda x : len(x))

print(len(result[-1]))
print(*result[-1])

import sys

N, M = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split()))

result = [0] * M

acc = 0

for i in range(N):
    acc += number[i]
    acc %= M
    result[acc] += 1

go = 0

for i in result:
    go += (i * (i - 1)) // 2

print(go + result[0])

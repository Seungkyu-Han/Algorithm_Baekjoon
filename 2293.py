import sys

N, K = map(int, sys.stdin.readline().split())

coin = []

for i in range(N):
    coin.append(int(sys.stdin.readline()))

result = [0] * (K + 1)
result[0] = 1

for i in range(N):
    for t in range(K - coin[i] + 1):
        result[t + coin[i]] += result[t]

print(result[-1])

import sys

N = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))

result = [0]

for i in range(1, N + 1):
    result.append(card[i - 1])
    for t in range(1, i):
        result[i] = max(result[i], result[t] + result[i-t])

print(result[-1])

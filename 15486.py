import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
cur = 0

for i in range(1, N + 1):
    cur = max(dp[i - 1], cur)
    T, P = map(int, sys.stdin.readline().split())

    if i + T - 1 > N:
        continue

    dp[i + T - 1] = max(cur + P, dp[i + T - 1])

print(max(dp))

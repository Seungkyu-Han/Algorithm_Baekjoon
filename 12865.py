import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K + 1) for i in range(N + 1)]
thing = [[0, 0]]

for i in range(N):
    thing.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    w = thing[i][0]
    v = thing[i][1]
    for t in range(1, K + 1):
        if t < w:
            dp[i][t] = max(dp[i-1][t], dp[i][t-1])
        else:
            dp[i][t] = max(dp[i-1][t], dp[i][t-1],dp[i-1][t-w] + v)



print(dp[-1][-1])

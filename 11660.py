import sys

N, M = map(int, sys.stdin.readline().split())

pan = []
hap = []

for i in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

for i in range(M):
    hap.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (N+1) for i in range(N+1)]

for n in range(N):
    for m in range(N):
        dp[n+1][m+1] = dp[n+1][m] + dp[n][m+1] - dp[n][m] + pan[n][m]


for i in range(M):
    start_n, start_m, end_n, end_m = hap[i]
    result = dp[end_n][end_m] - dp[end_n][start_m - 1] - dp[start_n - 1][end_m] + dp[start_n-1][start_m-1]
    print(result)

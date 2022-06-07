import sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))]
    dp = [[0, 0], [0, 0]]
    for t in range(n):
        case1 = max(dp[1][-1] + sticker[0][t], dp[1][-2] + sticker[0][t])
        case2 = max(dp[0][-1] + sticker[1][t], dp[0][-2] + sticker[1][t])
        dp[0].append(case1)
        dp[1].append(case2)
    print(max(dp[0][-1], dp[1][-1]))

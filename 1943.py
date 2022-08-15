import sys

for _ in range(3):
    N = int(sys.stdin.readline())

    coin = []
    sum_coin = 0

    for i in range(N):
        N, K = map(int, sys.stdin.readline().split())
        coin.append((N, K))
        sum_coin += (N * K)

    if sum_coin % 2 != 0:
        print(0)
        continue

    target = sum_coin // 2

    cur = [0] * (target + 1)
    cur[0] = 1

    for value, cnt in coin:
        for i in range(target, value - 1, -1):
            if cur[i - value]:
                for t in range(cnt):
                    if value * t + i <= target:
                        cur[value * t + i] = 1

    print(cur[target])

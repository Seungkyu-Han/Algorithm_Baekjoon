import sys

sys.setrecursionlimit(10 ** 6)

N, K = map(int, sys.stdin.readline().split())

combi = [[0] * (K + 1) for i in range(N + 1)]


def solve(n, k):
    if k == 0:
        combi[n][k] = 1
        return 1

    if k == 1:
        combi[n][k] = n
        return n

    if n == k:
        combi[n][k] = 1
        return 1

    if combi[n][k] != 0:
        return combi[n][k]

    combi[n][k] = (solve(n - 1, k) + solve(n - 1, k - 1)) % 10007

    return combi[n][k]


solve(N, K)

print(combi[N][K] % 10007)

import sys

sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

memo = dict()
memo[0] = 0
memo[1] = 1
memo[2] = 1
memo[3] = 2
memo[4] = 3


def fibo(cur):
    if cur < 5:
        tmp = [0, 1, 1, 2, 3]
        return tmp[cur]

    if cur % 2 == 0:
        if not (cur // 2 in memo):
            memo[cur // 2] = fibo(cur // 2)
        if not (cur // 2 - 1 in memo):
            memo[cur // 2 - 1] = fibo(cur // 2 - 1)
        case1 = memo[cur // 2]
        case2 = memo[cur // 2 - 1]
        return (case1 * (2 * case2 + case1)) % 1000000007
    else:
        tmp = cur + 1
        if not (tmp // 2 in memo):
            memo[tmp // 2] = fibo(tmp // 2)
        if not (tmp // 2 - 1 in memo):
            memo[tmp // 2 - 1] = fibo(tmp // 2 - 1)
        case1 = memo[tmp // 2]
        case2 = memo[tmp // 2 - 1]
        return (case1 ** 2 + case2 ** 2) % 1000000007


print(fibo(n))

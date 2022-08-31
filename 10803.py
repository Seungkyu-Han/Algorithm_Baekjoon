import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

n, m = (m, n) if n < m else (n, m)

squ = [[-1] * (m + 1) for i in range(n + 1)]


def solve(x, y):

    x, y = (y, x) if x < y else (x, y)

    if squ[x][y] != -1:
        return squ[x][y]

    if x == y:
        squ[x][y] = 1
        return squ[x][y]

    if y == 1:
        squ[x][y] = x
        return squ[x][y]

    if y == 2 and x % 2 == 0:
        squ[x][y] = x // 2
        return squ[x][y]
    
    if x >= 3 * y:
        squ[x][y] = 1 + solve(x - y, y)
        return squ[x][y]
    
    res = x * y

    for i in range(1, x // 2 + 1):
        target = solve(i, y) + solve(x - i, y)
        res = min(target, res)

    for i in range(1, y // 2 + 1):
        target = solve(x, i) + solve(x, y - i)
        res = min(target, res)

    squ[x][y] = res
    return squ[x][y]


solve(n, m)

print(squ[-1][-1])

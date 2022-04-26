def gogo(n, a, b):
    if n == 1:
        if a == 0 and b == 0:
            return 1
        elif a == 0:
            return 2
        elif b == 0:
            return 3
        else:
            return 4
    length = 2 ** (n - 1)
    cnt = length ** 2
    if a < length and b < length:
        cnt = 0
    elif a < length:
        pass
    elif b < length:
        cnt *= 2
    else:
        cnt *= 3
    return cnt + gogo(n - 1, a % length, b % length)


N, r, c = map(int, input().split())

print(gogo(N, r, c) - 1)

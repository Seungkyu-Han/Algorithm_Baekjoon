import sys

A, B, C = map(int, sys.stdin.readline().split())

def multi(a, n):
    if n == 1:
        return a % C
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return tmp * tmp % C
        else:
            return (tmp * tmp * a) % C


print(multi(A, B))

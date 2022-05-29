import sys


def result(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


num = int(input())
for i in range(num):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(result(M, N, x, y))

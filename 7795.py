import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()

    ptr = 0
    result = 0

    for t in range(N):
        while ptr < M and A[t] > B[ptr]:
            ptr += 1
        result += ptr

    print(result)

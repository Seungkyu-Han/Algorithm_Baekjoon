import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    CD = []
    result = 0
    ptr = 0

    for i in range(N):
        CD.append(int(sys.stdin.readline()))

    for i in range(M):
        tmp = int(input())
        left = ptr
        right = N

        while left <= right and left + right < 2 * N:
            mid = (left + right) // 2

            if CD[mid] == tmp:
                result += 1
                left = mid
                break

            if CD[mid] > tmp:
                right = mid - 1
            else:
                left = mid + 1


    print(result)

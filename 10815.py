import sys


def binary_search(list_a, search):
    left = 0
    right = len(list_a) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_a[mid] == search:
            return True
        if list_a[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return False


fir_num = int(sys.stdin.readline())
fir_list = list(map(int, sys.stdin.readline().split()))
fir_list.sort()

result = []

cnt = int(sys.stdin.readline())

ans = list(map(int, sys.stdin.readline().split()))

for i in ans:
    if binary_search(fir_list, i):
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end=' ')

import heapq
import sys

result = []
left = []
right = []

cnt = int(sys.stdin.readline())

flag = int(sys.stdin.readline())
result.append(flag)
heapq.heappush(left, flag * -1)

for i in range(1, cnt):
    num = int(sys.stdin.readline())
    if num > flag:
        heapq.heappush(right, num)
    else:
        heapq.heappush(left, num * -1)
    if len(left) < len(right):
        heapq.heappush(left, heapq.heappop(right) * -1)
    elif len(left) - 1 > len(right):
        heapq.heappush(right, heapq.heappop(left) * -1)
    flag = left[0] * -1
    result.append(flag)

for i in result:
    print(i)

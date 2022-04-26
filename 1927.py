import sys
import heapq

num = int(sys.stdin.readline())

data = []

for i in range(num):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        if data:
            print(heapq.heappop(data))
        else:
            print(0)
    else:
        heapq.heappush(data, input_num)



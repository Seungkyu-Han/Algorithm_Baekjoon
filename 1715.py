import heapq
import sys

N = int(input())

card = []

for i in range(N):
    tmp = int(sys.stdin.readline())
    heapq.heappush(card, tmp)

result = 0

for i in range(N - 1):
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    plus = first + second
    result += plus
    heapq.heappush(card, plus)
print(result)

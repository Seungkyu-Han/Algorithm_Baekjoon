import sys

num = int(input())

pred = [int(sys.stdin.readline()) for i in range(num)]

pred.sort()

result = 0

for i in range(1, num + 1):
    result += abs(pred[i - 1] - i)

print(result)

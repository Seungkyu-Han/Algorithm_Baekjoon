from collections import deque
import sys

N = int(sys.stdin.readline())

NGE = list(map(int, sys.stdin.readline().split()))

stack = deque()
result = [-1] * N

for i in range(len(NGE)):
    while stack and NGE[stack[-1]] < NGE[i]:
        result[stack.pop()] = NGE[i]
    stack.append(i)


print(*result)

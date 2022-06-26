import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

result = float('inf')
cur = numbers[0]

left, right = 0, 0

while right < N:
    if cur < S:
        right += 1
        if right >= N:
            break
        cur += numbers[right]
    else:
        cur -= numbers[left]
        if right - left + 1 < result:
            result = right - left + 1
        left += 1

if result == float('inf'):
    print(0)
else:
    print(result)

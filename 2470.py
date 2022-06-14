import sys

num = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()

left = 0
right = num - 1

result = [left, right]
result_value = float('inf')

while left < right:
    tmp_sum = liq[left] + liq[right]
    if abs(tmp_sum) < result_value:
        result = [left, right]
        result_value = abs(tmp_sum)
    if tmp_sum < 0:
        left += 1
    else:
        right -= 1

print(liq[result[0]], liq[result[1]])

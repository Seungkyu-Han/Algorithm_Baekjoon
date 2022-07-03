import sys

N = int(sys.stdin.readline())

liq = list(map(int, sys.stdin.readline().split()))

left = 0
right = N - 1
cur_con = abs(liq[0] + liq[-1])
cur_liq = [left, right]

while left < right:
    if cur_con > abs(liq[left] + liq[right]):
        cur_con = abs(liq[left] + liq[right])
        cur_liq = [left, right]
    if liq[left] + liq[right] > 0:
        right -= 1
    elif liq[left] + liq[right] == 0:
        break
    else:
        left += 1

print(liq[cur_liq[0]], liq[cur_liq[1]])

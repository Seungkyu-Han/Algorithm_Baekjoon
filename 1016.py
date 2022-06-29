import sys

mi, ma = map(int, sys.stdin.readline().split())

i = 2
result = [1] * (ma - mi + 1)

while i * i <= ma:
    target = i * i
    cur = mi // target - 1
    while cur * target <= ma:
        if mi <= cur * target <= ma:
            result[cur * target - mi] = False
        cur += 1
    i += 1

print(sum(result))

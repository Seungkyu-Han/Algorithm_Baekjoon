X = int(input())

target = 0
cur = 64
cnt = 0

while target != X:

    if target + cur > X:
        cur //= 2
        continue
    else:
        target += cur
        cnt += 1
        cur //= 2
        continue

print(cnt)
